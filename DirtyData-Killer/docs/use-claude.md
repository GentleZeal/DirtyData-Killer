# Claude 网页版与 Claude Code 使用

## Claude 网页版（推荐：上传单技能 ZIP）

1. 下载 `dist/data-quality-audit-v0.1.0.zip`（不是整个 GitHub 项目 ZIP）。
2. 打开 Claude，进入「自定义（Customize）→ Skills/技能」，如果该功能已经为账号启用，选择「+ → 创建技能 → 上传技能」。
3. 上传 ZIP，确认技能启用。
4. 上传 [sales.csv](../examples/samples/sales.csv)，发送“请用数据质量检查 Skill 诊断这份销售 CSV，并标明证据范围和风险等级”。
5. 要继续执行清洗建议/代码生成，分别上传其独立 ZIP 并调用。

官方：[在 Claude 中使用技能](https://support.claude.com/zh-CN/articles/12512180-在-claude-中使用技能)。界面与可用性以实际账号为准；也能不用 ZIP，直接粘贴 [Prompt](../prompts/data-quality-audit.md)。

## Claude Code（本地代码助手）

把三个技能目录复制到项目目录：

```text
你的项目/
└── .claude/skills/
    ├── data-quality-audit/SKILL.md
    ├── smart-cleaning-advisor/SKILL.md
    └── pandas-cleaning-generator/SKILL.md
```

然后在 Claude Code 里说：

```text
使用 data-quality-audit 对 examples/samples/sales.csv 做只读诊断；
先确认样本行数，不得覆盖文件，也不要执行自动删除。
```

如果让助手执行 Python，先检查权限和本地路径。更多使用差异可查 [Anthropic 帮助中心](https://support.claude.com/zh-CN/articles/12512198-如何创建自定义技能)。
