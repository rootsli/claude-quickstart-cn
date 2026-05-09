# 日期计算规则

## 核心规则：日期计算必须通过 Bash 或 Python 执行

大模型的日期 / 时间推理结果不可靠。凡是需要日期相关计算时，必须使用编程工具处理。

### Bash 使用示例
```bash
# 获取今天日期
date +%Y-%m-%d

# N天之后 / N天之前
date -d "+7 days" +%Y-%m-%d
date -d "-30 days" +%Y-%m-%d

# 查询指定日期星期几
date -d "2025-03-15" +%A

# 计算两个日期相差天数
echo $(( ($(date -d "2025-12-31" +%s) - $(date -d "2025-01-01" +%s)) / 86400 ))
```

### Python 使用示例
```python
from datetime import datetime, timedelta

# 获取今天日期
today = datetime.now().strftime("%Y-%m-%d")

# N天之后 / N天之前
future = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

# 计算两个日期相差天数
d1 = datetime(2025, 1, 1)
d2 = datetime(2025, 12, 31)
diff = (d2 - d1).days
```

### 禁止事项
- 禁止靠人工心算日期后给出答案
- 禁止使用「大概」「约」等模糊估算日期
- 禁止自行判断闰年、每月天数 → 必须用工具校验
- 禁止手动计算时区转换 → 需使用 pytz /zoneinfo 库
