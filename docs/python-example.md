# Pandas 参考脚本：实际功能与边界

代码：[examples/generated/clean_sales.py](../examples/generated/clean_sales.py)

## 运行

```bash
pip install -r requirements.txt
python examples/generated/clean_sales.py --input examples/samples/sales.csv --output-dir out
```

支持 `csv`/`xlsx` 输入，按文本读取，尝试 CSV 编码 UTF-8-SIG 与 GB18030，支持中文列名。输出目录有同名结果时拒绝覆盖（除非明确加 `--overwrite`）。不会删除原始记录。

## 这份演示数据的预期统计（5 条记录）

| 检查项 | 预期 |
|---|---:|
| 输入记录数 | 5 |
| 输出记录数 | 5 |
| 重复订单号涉及记录数 | 2 |
| 金额解析失败记录数 | 1 |
| 日期解析失败记录数 | 1 |
| 金额负值待确认记录数 | 1 |
| 异常明细记录数 | 3（去重后的异常行数；多种问题可以落在同一行） |

## 安全边界

- **标识列**：CSV 前导零保留；如原始 Excel 单元格已经存成数值且丢失前导零，程序无法凭空恢复。
- **数据不修改**：清洗字段作为新列写出；不对原输入文件做保存。
- **输出 CSV 的 Excel 公式防护**：可疑文本会附加转义前缀。输出用于查看/检查，不是原始数据字节级备份。跨不同表格软件时仍应采用可靠的文本导入方式。
- **异常类型**：已标记不等于认定为错误，负数可能是退款。
- **不保证任意数据通用**：当前脚本假设列名 `订单号、商品名称、金额、下单日期`，需根据实际业务调整。

## 可选的自动检查

```bash
python -m unittest discover -s tests -v
```

这验证的是参考脚本和 Skill 文件的基础结构，**不是每个模型在不同平台的回答质量**。
