# 调试分析报告

**日期**: {{date}}
**错误类型**: `{{error_type}}`
**严重性**: {{severity}}

---

## 错误概述

### 错误描述

{{error_description}}

### 错误消息

```
{{error_message}}
```

### 堆栈跟踪

```
{{stack_trace}}
```

---

## 根本原因分析

### 直接原因

{{direct_cause}}

### 潜在问题

{{#each underlying_issues}}
{{@index}}. {{this}}
{{/each}}

---

## 受影响代码

**File**: `{{file_path}}`
**Line**: {{line_number}}

```{{language}}
{{code_snippet}}
```

---

## 修复方案

{{#each fixes}}

### 选项 {{@index}}: {{title}}

**方法**: {{approach}}

**代码修改**:
```{{language}}
{{code}}
```

**优点**:
{{#each pros}}
- {{this}}
{{/each}}

**缺点**:
{{#each cons}}
- {{this}}
{{/each}}

---

{{/each}}

## 预防建议

{{#each prevention}}
- [ ] {{this}}
{{/each}}

---

## 相关资源

{{#each resources}}
- [{{title}}]({{url}})
{{/each}}

---

## 验证步骤

应用修复后验证:

{{#each verification_steps}}
{{@index}}. {{this}}
{{/each}}
