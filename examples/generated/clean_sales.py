"""销售 CSV/XLSX 清洗示例：零删除、中文注释、Excel 安全导出。Python >= 3.10。"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ["订单号", "商品名称", "金额", "下单日期"]
OUTPUT_NAMES = ["clean.csv", "exceptions.csv", "summary.json"]


def read_input(path: Path, sheet: str) -> tuple[pd.DataFrame, str]:
    """读取全部字段为文本，保留订单号等标识的前导零。"""
    if path.suffix.lower() == ".csv":
        for enc in ("utf-8-sig", "gb18030"):
            try:
                return pd.read_csv(path, dtype=str, keep_default_na=False, encoding=enc), enc
            except UnicodeDecodeError:
                continue
        raise ValueError("无法按 UTF-8-SIG 或 GB18030 解析 CSV，请确认源文件编码")
    if path.suffix.lower() == ".xlsx":
        sheet_name: str | int = int(sheet) if sheet.isdigit() else sheet
        return pd.read_excel(
            path, sheet_name=sheet_name, dtype=str, keep_default_na=False, engine="openpyxl"
        ), "xlsx"
    raise ValueError("仅支持 .csv 和 .xlsx 文件（暂不支持旧 .xls）")


def parse_dates(column: pd.Series) -> pd.Series:
    """在不覆盖原日期文本的情况下，识别几种常用的年月日表示。"""
    cleaned = (
        column.astype("string")
        .str.strip()
        .str.replace("年", "-", regex=False)
        .str.replace("月", "-", regex=False)
        .str.replace("日", "", regex=False)
        .str.replace("/", "-", regex=False)
    )
    # 明确要求 yyyy-mm-dd，避免美国式月/日歧义
    return pd.to_datetime(cleaned, format="%Y-%m-%d", errors="coerce")


def safe_excel_text(value: object) -> object:
    """为 Excel 打开 CSV 的场景对可疑字符串加单引号。

    输出用于人工查看；机器系统如需还原，请从保留的原始数据文件读取。
    金额等数值列在清洗中已单独解析，这里避免转义纯负数字面量。
    """
    if not isinstance(value, str):
        return value
    probe = value.lstrip(" \t\r\n")
    if not probe:
        return value
    is_negative_number = bool(re.fullmatch(r"-\d+(?:\.\d+)?", probe))
    if probe[0] in "=+-@" and not is_negative_number:
        return "'" + value
    return value


def safe_for_excel(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """仅处理字符串字段，保留数字和布尔列类型。"""
    result = df.copy()
    changed = 0
    for column in result.columns:
        if pd.api.types.is_object_dtype(result[column]) or pd.api.types.is_string_dtype(result[column]):
            original = result[column]
            converted = original.map(safe_excel_text)
            changed += int((original.fillna("") != converted.fillna("")).sum())
            result[column] = converted
    return result, changed


def clean(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"缺少必需的列：{', '.join(missing)}；实际列名：{list(df.columns)}")
    if df.empty:
        raise ValueError("数据表没有任何数据行，无法完成清洗")

    original_rows = len(df)
    output = df.copy(deep=True)
    # 保留原始字段；仅创建派生列，不覆盖订单号或金额文本
    output["商品名称_clean"] = output["商品名称"].astype("string").str.strip()
    output["金额_num"] = pd.to_numeric(output["金额"].str.strip(), errors="coerce")
    output["下单日期_parsed"] = parse_dates(output["下单日期"]).dt.strftime("%Y-%m-%d")
    blank_amount = output["金额"].str.strip().eq("")
    blank_date = output["下单日期"].str.strip().eq("")

    output["__issue_金额缺失"] = blank_amount
    output["__issue_金额解析失败"] = (~blank_amount) & output["金额_num"].isna()
    output["__issue_金额负值待确认"] = output["金额_num"].lt(0).fillna(False)
    output["__issue_日期缺失"] = blank_date
    output["__issue_日期解析失败"] = (~blank_date) & output["下单日期_parsed"].isna()
    output["__issue_订单号为空"] = output["订单号"].str.strip().eq("")
    output["__issue_订单号重复"] = (~output["__issue_订单号为空"]) & output["订单号"].duplicated(keep=False)
    output["__issue_商品名为空"] = output["商品名称_clean"].eq("")

    flags = [c for c in output.columns if c.startswith("__issue_")]
    exceptions = output.loc[output[flags].any(axis=1)].copy()

    # 三项关键校验：不删行、保留订单号、异常行可由布尔标记追踪
    assert len(output) == original_rows, "清洗过程意外改变了行数"
    assert output["订单号"].tolist() == df["订单号"].tolist(), "订单号被意外修改"
    assert len(exceptions) == int(output[flags].any(axis=1).sum()), "异常记录不一致"

    summary = {
        "scenario": "销售报表",
        "input_rows": original_rows,
        "output_rows": len(output),
        "exception_rows": len(exceptions),
        "flags": {c: int(output[c].sum()) for c in flags},
        "policy": "不删除记录；负值/重复号仅标记；源数据不覆盖",
    }
    return output, exceptions, summary


def main() -> int:
    parser = argparse.ArgumentParser(description="中文销售数据清洗（默认不覆盖输出）")
    parser.add_argument("--input", required=True, help="源 CSV/XLSX 文件路径")
    parser.add_argument("--output-dir", default="out", help="输出文件夹，默认 out")
    parser.add_argument("--sheet", default="0", help="XLSX 工作表名或序号，默认 0")
    parser.add_argument("--overwrite", action="store_true", help="明确允许覆盖先前输出文件")
    args = parser.parse_args()

    try:
        source = Path(args.input).expanduser().resolve()
        outdir = Path(args.output_dir).expanduser().resolve()
        if not source.is_file():
            raise FileNotFoundError(f"输入文件不存在：{source}")
        targets = {name: outdir / name for name in OUTPUT_NAMES}
        if source in targets.values():
            raise ValueError("输出目录中的文件名与输入文件冲突，请指定其他 --output-dir")
        if not args.overwrite:
            conflicts = [str(p) for p in targets.values() if p.exists()]
            if conflicts:
                raise FileExistsError("已有同名输出文件，拒绝覆盖：" + ", ".join(conflicts))

        df, encoding = read_input(source, args.sheet)
        clean_df, issue_df, summary = clean(df)
        clean_export, changed_clean = safe_for_excel(clean_df)
        issue_export, changed_issues = safe_for_excel(issue_df)
        summary["csv_encoding_read"] = encoding
        summary["excel_safe_cells_clean"] = changed_clean
        summary["excel_safe_cells_exceptions"] = changed_issues
        summary["csv_export_note"] = "文本中潜在 Excel 公式前缀会加单引号；请勿把 CSV 当作无损的原始备份"
        outdir.mkdir(parents=True, exist_ok=True)
        clean_export.to_csv(targets["clean.csv"], index=False, encoding="utf-8-sig")
        issue_export.to_csv(targets["exceptions.csv"], index=False, encoding="utf-8-sig")
        targets["summary.json"].write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"完成：共 {summary['input_rows']} 行，异常 {summary['exception_rows']} 行，输出目录：{outdir}")
        return 0
    except (OSError, ValueError, KeyError, ImportError, pd.errors.ParserError) as exc:
        print(f"清洗失败：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
