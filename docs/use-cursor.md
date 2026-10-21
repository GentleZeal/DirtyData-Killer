# Cursor：将 Skill 放进项目目录

Cursor 的官方 Skills 使用 `SKILL.md` 描述专业工作流；当前文档支持 `.cursor/skills/` 和 `.agents/skills/` 等路径。参考：https://cursor.com/help/customization/skills

## 安装（手动，无需 ZIP）

将本仓库里 `skills/` 的三个子目录复制到**你正在用 Cursor 打开的项目**的 `.cursor/skills/` 下：

```text
你的数据分析项目/
├── .cursor/
│   └── skills/
│       ├── data-quality-audit/SKILL.md
│       ├── smart-cleaning-advisor/SKILL.md
│       └── pandas-cleaning-generator/SKILL.md
└── sales.csv
```

在 Cursor Agent 聊天使用 `/data-quality-audit`，也可以输入 `@` 选择 Skill 或用自然语言请求。不同版本可用选项可能略有不同。

## 操作示例

```text
使用 data-quality-audit 对当前工作区的 sales.csv 做只读检查。
请说明是否真正读取了文件；输出含行数、证据、严重度、P0~P3 的中文报告。
不要删除或修改 sales.csv。
```

如果让 Agent 生成代码，使用第三个 Skill；在它提出执行或写文件前审查脚本和输出目录。**Skill 告诉 Agent 怎么做，不等于已授权它执行破坏性操作。**
