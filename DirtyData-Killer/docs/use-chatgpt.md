# ChatGPT：不安装也能使用

**个人账号最稳妥**的方式：将 `prompts/` 里的指令作为消息，再上传虚构或脱敏 CSV/XLSX。项目功能取决于账号和工具权限；生成的文本报告不意味着自动执行了 Python。

## 方式一：普通对话（最简单）

1. 打开 [第一个 Prompt](../prompts/data-quality-audit.md)，**复制全文**到 ChatGPT 新对话并发送。
2. 上传 [sales.csv](../examples/samples/sales.csv)（或直接粘贴 5 行数据），然后发送：

```text
请按上一条“数据质量检查 Skill”指令检查刚上传的销售数据。
输出中文结构化质量报告；明确数据来源是完整读取还是仅有样本；
重复组数和重复行数分别报告，引用 CSV 文件行号时计入表头。
不修改原文件、不编造统计，最后输出 schema_version: '0.1' 的 YAML。
```

3. 要后续清洗建议，复制 [第二个 Prompt](../prompts/smart-cleaning-advisor.md) 与第一步报告到新对话。
4. 要生成脚本，复制 [第三个 Prompt](../prompts/pandas-cleaning-generator.md) 与第二步方案到新对话；审阅后才运行。

## 方式二：ChatGPT 项目（适合长期复用）

1. 左侧栏选择「新建项目」，例如命名「数据干净计划」。
2. 在项目中添加相关 `SKILL.md` 或纯 Prompt 文本作为参考资料。也可在「项目设置」填入本项目的通用使用约定。
3. 新建项目内聊天，明确说“按 `data-quality-audit` 的指令执行”，再上传脱敏 CSV。
4. 多 Skill 使用时**明确指出使用哪份指令**，避免上下文混乱。

**提醒：** 在项目里添加 Skill 文件，属于“作为资料/指令使用”，不是原生 Skill 安装机制。官方 [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)。

## 方式三：原生 ChatGPT Skills（仅当你的账号有入口）

截至 2026-10，官方文件说明原生 Skills 面向合资格的 **Business / Enterprise / Healthcare / Edu** 工作空间，受管理员权限限制。若左侧栏有「插件 → Skills」，可使用「Create → Upload from your computer」上传单 Skill 包。个人 Free / Go / Plus / Pro 账号**不应默认假定有这个入口**。官方 [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)。

## 建议先用的测试场景

- 成绩：`001` 前导零、`105` 超范围、`002` 重复。
- 销售：`-10` 退货候选、`abc` 类型错误、`0002` 重复、非法日期。
- 问卷：回答 `无` 应保留，`未填` 需要按字段解释，满意度 `6` 越界。

参考：[三步连用](workflow.md) / [案例清单](../examples/data-quality-audit.md) / [文件上传官方说明](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt)。
