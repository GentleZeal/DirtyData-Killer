# Skill 交接 YAML 约定（schema_version 0.1）

这是**提示词输出约定**，还不是机器执行器接口。只有当未来 v0.2 真的做了解析和校验，才会把它称为正式的数据契约。

## 诊断报告 → 清洗建议

```yaml
schema_version: '0.1'        # 交接格式版本，不能因为修改报告升成0.2
report_version: 'v2'        # 报告内容改过才更新

dataset: 'sales.csv'
evidence_scope: 'complete'   # complete / sample / description
record_count: 5             # 仅在有证据时写具体值；无法确认则 null
issues:
  - id: 'Q01'
    column: '金额'
    category: '类型'
    observed: 'abc 无法解析为金额'
    severity: '高'
    priority: 'P1'
    status: '已验证'
    proposed_action: '保留原值，在派生列解析并标记失败'
    requires_confirmation: true
```

## 清洗建议 → 代码生成

```yaml
schema_version: '0.1'
scenario: '销售数据分析'
input_columns: ['订单号', '商品名称', '金额', '下单日期', '备注']
policy: 'non_destructive'
actions:
  - issue_id: 'Q01'
    column: '金额'
    action: '解析金额到金额_num，记录解析失败'
    auto_execute: true
    confirmation_needed: 'abc 的真实金额是多少？'
outputs: ['clean.csv', 'exceptions.csv', 'summary.json']
```

## 重要约定

- **`schema_version`**：协议版本，当前固定 `0.1`。
- **`report_version`**：人工报告迭代版本，可 `v1 → v2`，不改变 `schema_version`。
- **`record_count`**：记录条数，通常 CSV 不含表头。引用 Excel 行号与 CSV 物理行号时应单独说明。
- **`status`**：必须区分已验证 / 样本观察 / 待确认。
- **`auto_execute`**：仅表示清洗动作的默认建议；它**不是用户已经批准执行**，更不表示模型真的运行了代码。
- **异常数口径**：重复组数≠重复涉及记录数；问题项数≠异常行数。
