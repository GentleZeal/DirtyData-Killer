"""不依赖 pytest：python -m unittest discover -s tests -v。"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "examples" / "generated" / "clean_sales.py"
INPUT = ROOT / "examples" / "samples" / "sales.csv"


class SalesCleanTests(unittest.TestCase):
    def test_run_and_protect_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "out"
            before = INPUT.read_bytes()
            args = [sys.executable, str(SCRIPT), "--input", str(INPUT), "--output-dir", str(out)]
            result = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(INPUT.read_bytes(), before)
            s = json.loads((out / "summary.json").read_text(encoding="utf-8"))
            self.assertEqual(s["input_rows"], 5)
            self.assertEqual(s["output_rows"], 5)
            self.assertEqual(s["flags"]["__issue_订单号重复"], 2)
            self.assertEqual(s["flags"]["__issue_金额解析失败"], 1)
            self.assertEqual(s["flags"]["__issue_日期解析失败"], 1)
            # 不带 overwrite 时拒绝覆盖结果
            again = subprocess.run(args, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertIn("拒绝覆盖", again.stderr)

    def test_missing_columns(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "bad.csv"
            src.write_text("订单号,金额\n0001,1\n", encoding="utf-8")
            r = subprocess.run([sys.executable, str(SCRIPT), "--input", str(src),
                                "--output-dir", str(Path(tmp) / "out")], capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("缺少必需的列", r.stderr)


if __name__ == "__main__":
    unittest.main()
