"""最小结构校验：3 个 Skill 可发现、路径和元数据正确。"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('data-quality-audit', 'smart-cleaning-advisor', 'pandas-cleaning-generator')


class SkillStructureTests(unittest.TestCase):
    def test_skill_frontmatter(self):
        for name in NAMES:
            with self.subTest(skill=name):
                content = (ROOT / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8')
                self.assertTrue(content.startswith('---\n'))
                header = content.split('---', 2)[1]
                self.assertIn(f'name: {name}', header)
                for key in ('description:', 'description_zh:', 'description_en:', 'author:', 'version:'):
                    self.assertIn(key, header)
                self.assertIn('## 输入格式', content)
                self.assertIn('##', content)

    def test_three_examples_each(self):
        for name in NAMES:
            text = (ROOT / 'examples' / f'{name}.md').read_text(encoding='utf-8')
            for n in (1, 2, 3):
                self.assertIn(f'例 {n}', text)
            self.assertIn('输入', text)
            self.assertIn('期望输出', text)


if __name__ == '__main__':
    unittest.main()
