# 多平台使用总览（更新于 2026-10-21）

Skill 本体 = 一个目录里的 `SKILL.md`（含 YAML 元数据和中文指令）。**平台之间“可以按说明用”不等于每个平台都已通过自动/人工兼容测试**。当前版本未实测全部平台的原生导入。

| 平台 | 用法 | 入口 |
|---|---|---|
| WorkBuddy | 原生技能包上传（支持时） | [详细步骤](use-workbuddy.md) |
| ChatGPT 个人账号 | 聊天 / 项目中的 Prompt + 附件 | [详细步骤](use-chatgpt.md) |
| ChatGPT 合资格工作空间 | 原生 Skills（如管理员允许）或 Prompt | [详细步骤](use-chatgpt.md) |
| Claude 网页版 | 上传单技能 ZIP / 粘贴 Prompt | [详细步骤](use-claude.md) |
| Claude Code | 复制至 `.claude/skills/` | [详细步骤](use-claude.md) |
| Cursor | 复制至 `.cursor/skills/` | [详细步骤](use-cursor.md) |
| Grok 或其他聊天 AI | 粘贴 `prompts/` 的正文 | [详细步骤](use-grok.md) |

## 官方资料（平台可能更改界面，以官方实时说明为准）

- WorkBuddy：https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market
- WorkBuddy Skill 结构：https://open.workbuddy.cn/docs/skill
- ChatGPT Projects：https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- ChatGPT Skills（目前限合资格工作空间）：https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- ChatGPT 文件上传：https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt
- Claude 自定义技能：https://support.claude.com/zh-CN/articles/12512180-在-claude-中使用技能
- Cursor Skills：https://cursor.com/help/customization/skills
- GitHub 网页上传：https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

## 常见兼容性问题

- **没有上传 Skill 的入口**：请复制 `prompts/<name>.md` 正文使用，勿将 ZIP 直接当数据上传后假设系统自动安装。
- **安装后没有调用**：在对话里明确写“请调用 data-quality-audit Skill”。先到技能列表确认其已启用。
- **报告自称已扫描全量**：要求展示实际统计依据；未提供工具能力时只能标注样本或描述推测。
- **代码生成后不能运行**：完整错误信息 + 最小虚构数据发到 GitHub Issue，不要上传商业或个人隐私。
