# Grok / 其他通用 AI：复制 Prompt 即可

这份项目**不假设 Grok 网页版有与 WorkBuddy 同名的“上传 SKILL.md”原生入口**。最稳妥的跨平台使用方式是复制纯 Prompt。

## 方法

1. 打开 [Prompt ①](../prompts/data-quality-audit.md)，全选复制，发到 Grok 或其他聊天 AI 中。
2. 再贴下面的虚构问卷样本；如果当前版本支持上传附件，也可上传 [survey.csv](../examples/samples/survey.csv)。
3. 将生成的报告交给 [Prompt ②](../prompts/smart-cleaning-advisor.md)；需要完整脚本时交给 [Prompt ③](../prompts/pandas-cleaning-generator.md)。

```text
场景：问卷满意度统计，满意度范围 1~5。
字段：问卷ID,城市,满意度,反馈
Q01,北京,5,无
Q02,上海,未填,服务好
Q03,  北京  ,4, 还行
Q04,广州,6,N/A
注意：“无”代表没有建议，是有效反馈值；城市列去两端空格；
请先做只读数据质量诊断，不能编造全量用户的比例。
```

## 应该看到什么？

“满意度=6”越界；“未填”为满意度缺失占位符；城市“  北京  ”需要标准化；反馈“无”**不是**全局空值。所有判断只能基于这 4 行样本。

> 其他 AI（通义、豆包、Kimi 等）也可参考该通用方式；**这里不声称它们都具备原生 SKILL.md 安装能力**。不同平台隐私政策各异，真实数据先脱敏。
