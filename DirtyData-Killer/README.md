# 🧹 数据干净计划 · DirtyData Killer

> **先找出脏数据，再决定怎么改。** 面向中文 Excel / CSV 场景的开源 Skill 套装。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-v0.1.0-green.svg)](CHANGELOG.md)

这是一个以**中文 Prompt 驱动**的数据质量项目，服务于学生成绩、销售订单、问卷、运营报表等常见任务。它把一件事拆成三步：**诊断 → 建议 → 生成安全的 Pandas 代码**。

> **版本边界**：v0.1.0 有三个可复制的 Skill、一份可运行的 Pandas 销售清洗示例、九组虚构但贴近真实场景的中文案例。它**不是**自动执行任意 Excel/CSV 的通用数据清洗 Agent；大模型能否读取附件/执行 Python 取决于所在平台权限。各平台的原生 Skill 兼容性尚未逐一完成实测，请按平台文档安装，遇到问题欢迎反馈。

## 🌟 为什么做这个项目？

数据常常不是“空值删掉”那么简单。学号 `001` 不能变 `1`；`105` 分不能直接改成 `100`；`-10` 元可能是退货；问卷里的“无”可能是有效回答。错误的自动清洗会比原始脏数据更危险。

**原则：保留原始值、先标记再确认、明确证据范围、禁止编造统计、输出可复核。** 真实数据请先脱敏。

## 🧩 三个 Skill

| Skill | 解决什么问题 | 输出 | 直接阅读 |
|:--|:--|:--|:--|
| ① 数据质量检查 `data-quality-audit` | 哪里有问题？ | 中文质量报告（严重度 / P0-P3 / 证据 / YAML） | [SKILL.md](skills/data-quality-audit/SKILL.md) |
| ② 智能清洗建议 `smart-cleaning-advisor` | 怎么清洗更稳妥？ | A/B/C 分级的清洗方案与代码思路 | [SKILL.md](skills/smart-cleaning-advisor/SKILL.md) |
| ③ 清洗代码生成 `pandas-cleaning-generator` | 如何生成可运行脚本？ | 完整 Pandas 代码、异常报告与运行说明 | [SKILL.md](skills/pandas-cleaning-generator/SKILL.md) |

每个 Skill 是单独目录，`SKILL.md` 包含角色、输入约定、执行规则、固定输出格式与示例。普通对话模型可直接复制 [prompts/](prompts/) 中去掉元数据的 Prompt。

## 🚀 30 秒上手（不写 Python）

**方式 A：ChatGPT / Grok / 其他聊天 AI**

1. 打开 [数据质量检查 Prompt](prompts/data-quality-audit.md)，复制全文到新对话。
2. 再发这段演示数据（虚构）：

```text
请按刚才的规则生成中文数据质量诊断报告，只依据下列4行样本判断，不要编造全校统计。
场景：期末成绩；成绩范围：0~100；学号为字符串，学号重复需核查是否补考。
字段：学号,姓名,班级,成绩,考试日期
001,张同学,一班,98,2026/09/01
002,李同学,一班,105,2026年9月1日
002,李同学,一班,,2026-09-01
003,王同学,二班,0,2026-09-02
```

3. 检查是否识别：`105` 越界、`002` 重复、成绩空值、日期混写；不能擅自把 `0` 判为缺失。
4. 将结果给第二个 Prompt，再将清洗方案给第三个 Prompt。详见 [三步连用指南](docs/workflow.md)。

**方式 B：WorkBuddy / Claude / Cursor 的 Skill 模式**：优先下载 [dist/](dist/) 下对应的**单个 Skill ZIP** 或复制整个 `skills/<name>` 目录到支持的 Skills 位置。**不要把整个 GitHub 仓库 ZIP 当作一个 Skill。** 安装细节见下表。

## 🖥️ 平台使用教程（中文图文步骤）

| 平台 | 建议方式 | 教程 |
|---|---|---|
| **腾讯 WorkBuddy** | 技能页面上传单 Skill ZIP（如账号界面支持） | [WorkBuddy 安装与调用](docs/use-workbuddy.md) |
| **ChatGPT 个人账号** | 项目资料 / 新对话中添加 Prompt + CSV 文件 | [ChatGPT 使用](docs/use-chatgpt.md) |
| **ChatGPT 合资格工作空间** | 如 Skills 功能已开放，可原生上传单技能包 | [ChatGPT 使用](docs/use-chatgpt.md) |
| **Claude 网页版** | 自定义技能中上传单 Skill ZIP；功能取决于账户开关 | [Claude 使用](docs/use-claude.md) |
| **Claude Code** | `.claude/skills/<name>/SKILL.md` | [Claude 使用](docs/use-claude.md) |
| **Cursor** | `.cursor/skills/<name>/SKILL.md` | [Cursor 使用](docs/use-cursor.md) |
| **Grok / 其他 AI** | 直接粘贴 `prompts/`，上传脱敏样本 | [Grok 与通用 AI](docs/use-grok.md) |

完整概览和官方链接见 [docs/platforms.md](docs/platforms.md)。**注意：“聊天里粘贴 Prompt”和“平台原生安装 Skill”是两种不同接入方式。**

## 📁 三组核心样本与九组使用案例

| 场景 | 样本数据 | Skill ① 输入和期望 | Skill ② 输入和期望 | Skill ③ 输入和期望 |
|---|---|---|---|---|
| 成绩单 | [grades.csv](examples/samples/grades.csv) | [诊断案例](examples/data-quality-audit.md#例-1期末成绩表) | [建议案例](examples/smart-cleaning-advisor.md#例-1成绩统计) | [生成代码案例](examples/pandas-cleaning-generator.md#例-2成绩单清洗) |
| 电商销售 | [sales.csv](examples/samples/sales.csv) | [诊断案例](examples/data-quality-audit.md#例-2电商销售报表) | [建议案例](examples/smart-cleaning-advisor.md#例-2销售业务) | [生成代码案例](examples/pandas-cleaning-generator.md#例-1电商销售清洗有可运行参考实现) |
| 问卷 | [survey.csv](examples/samples/survey.csv) | [诊断案例](examples/data-quality-audit.md#例-3问卷满意度) | [建议案例](examples/smart-cleaning-advisor.md#例-3问卷分析) | [生成代码案例](examples/pandas-cleaning-generator.md#例-3问卷清洗) |

案例是*用于教学的虚构数据*，**预期输出**不代表所有模型已通过自动验收。还有一份 [WorkBuddy 销售诊断 v1 → v2 纠错案例](examples/workbuddy-review.md)，展示如何发现“总行数与引用行号不一致”问题。

## 🐼 运行一份已有的 Python 清洗示例（可选）

这里只提供**一个有完整实现的参考脚本**：[clean_sales.py](examples/generated/clean_sales.py)，不是三种业务的通用脚本。运行需要 Python 3.10+。

```bash
pip install -r requirements.txt
python examples/generated/clean_sales.py --input examples/samples/sales.csv --output-dir out
```

生成 `out/clean.csv`、`out/exceptions.csv`、`out/summary.json`；不覆盖输入。为了避免覆盖旧结果，第二次运行可换 `--output-dir out2`（或显式 `--overwrite`）。具体数据口径及安全注意见 [运行示例与限制](docs/python-example.md)。

## 📦 仓库结构

```text
DirtyData-Killer/
├── README.md                    # 中文首页
├── CONTRIBUTING.md / LICENSE / CHANGELOG.md
├── skills/                      # 三个独立的 SKILL.md
├── prompts/                     # 可直接复制的纯中文 Prompt
├── dist/                        # 分开导入的三个 Skill ZIP
├── examples/
│   ├── samples/                 # grades / sales / survey（虚构数据）
│   ├── generated/clean_sales.py # 参考脚本（非通用 Agent）
│   ├── preview/                 # 参考脚本样例结果
│   └── *.md                     # 九组输入与期望输出、WorkBuddy 复盘
├── docs/                        # 平台、三步连用、上架、常见问题
├── tests/                       # 可选的脚本与结构检查
└── .github/                     # Issue 模板和 CI 工作流
```

## 🛠️ 参与贡献 / 反馈问题

欢迎提交脱敏业务场景、中文字段兼容问题、格式误判、Prompt 改进和代码测试。请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [Issue 模板](.github/ISSUE_TEMPLATE/bug_report.md)。**报告应附：平台、模型/版本（若已知）、输入样本、期望、实际、是否实际执行文件。** 不要贴真实客户信息或未经授权的敏感数据。

## 🗺️ Roadmap

- **v0.1.0（当前）**：三个 Prompt Skill + 示例与跨平台文档；销售参考清洗脚本
- **v0.2**：Python 规则检测核心（真正计算全量质量指标），稳定结构化报告协议
- **v0.3**：Streamlit 页面（上传 → 预览 → 检查 → 勾选 → 导出）
- **v0.4**：可选 LLM Agent（建议、解释、调用安全的规则引擎）

见 [路线图](docs/roadmap.md)、[报告协议](docs/report-schema.md)。

## 🛡️ 隐私 / 免责声明

请勿直接将真实手机号、身份证号、学号、订单隐私及公司内部敏感文件上传到公开 AI 服务或 GitHub。生成的建议或代码需先在**已备份、脱敏**数据上检查。输出 CSV 面向 Excel 查看时对可疑公式文本做转义，**这会改变展示文件中的文本值，不能把它当作无损原始备份**。

## 📜 开源许可证

[MIT](LICENSE)。欢迎 Fork / Star / 提交 Issue；感谢所有贡献者。项目不是任何 AI 平台的官方产品。
