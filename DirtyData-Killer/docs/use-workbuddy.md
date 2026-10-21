# 腾讯 WorkBuddy：安装与使用（零代码）

> 当前使用方式参照 [WorkBuddy 技能说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) 与 [Skill 格式](https://open.workbuddy.cn/docs/skill)。不同版本界面按钮名称可能变动。本项目不声称已经在所有 WorkBuddy 版本上测试成功。

## 一、安装第一个 Skill

1. 在 GitHub 打开 `dist/`，下载 `data-quality-audit-v0.1.0.zip`，**单个 ZIP 不要解压**。
2. 打开 WorkBuddy → 左侧「专家·技能·连接器」→「技能」。
3. 找到「添加技能」→「上传技能」（如果看不到，请参考官方说明或使用通用 Prompt 方式）。
4. 选择下载好的**单个 Skill ZIP**，等待平台提示完成，再到「已安装」查看并启用。
5. **不要上传整个 `DirtyData-Killer` GitHub 仓库压缩包当作一个 Skill。**

## 二、复制这段话进行演示

上传 [销售样本](../examples/samples/sales.csv)，在新对话里发送：

```text
请调用 data-quality-audit（数据质量检查）Skill，对我上传的 sales.csv 做中文诊断。
请注明读取的是完整文件还是样本；给出数据记录数（不含表头）、字段数；
检查订单号重复、金额无法解析、日期无效、中文日期混写、商品名称空格、CSV 公式风险。
负数可能是退货，0元可能是赠品；不得直接删除。
每项问题给严重度、P0~P3优先级、证据和待确认项；交接摘要 schema_version 固定为0.1。
输出前核对“总行数”和“证据行号”能否对上。
```

**预期检查点：** 示例有 5 条记录，5 个字段，订单号 `0002` 重复 2 行，金额 `abc` 无法解析 1 行，日期 `2026-13-01` 无效 1 行。切记：**具体结果属于本仓库演示数据，不代表其他文件都一样。**

## 三、接着使用第二、第三个 Skill

依次导入：

- `dist/smart-cleaning-advisor-v0.1.0.zip`：贴入第一步诊断报告，要求根据 Q01... 给 A/B/C 分级方案，**不执行清洗**。
- `dist/pandas-cleaning-generator-v0.1.0.zip`：贴入第二步方案，要求生成 Python 3.10+/Pandas 2.x 可运行代码；**默认不删除或覆盖数据**。

完整可复制的衔接话术见 [三步连用](workflow.md)。

## 四、导入失败怎么办？

- 核对 ZIP 内层结构是 `data-quality-audit/SKILL.md`，不能是多层套娃；`SKILL.md` 必须位于技能文件夹根部。
- 导入时看不到新技能，确认“已安装”里的启用开关。
- 仍失败，把错误文字、WorkBuddy 版本、ZIP 文件名发到 Issue；**不要上传个人或公司敏感数据**。
- 提供的 `prompts/data-quality-audit.md` 可直接粘贴到聊天，不需要安装；但这不算原生 Skill 安装成功。

## 五、这份项目曾遇到的实际反馈

首次演示中，报告把 5 行错数为 4 行，后来修订。这个典型问题和改进策略整理在 [WorkBuddy 纠错案例](../examples/workbuddy-review.md)。证明 AI 报告需要核对，**不能因生成了漂亮的 Markdown 就认定结果准确**。
