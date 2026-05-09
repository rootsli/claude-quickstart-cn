#!/usr/bin/env python3
"""
PRD 关键词检测钩子 (用户提交提示词时触发)

当检测到用户输入中包含 PRD 相关关键词时
返回引导使用 /prd-create 能力的提示信息。

-- 关键词修改说明 --
正向关键词(POSITIVE_KEYWORDS)：包含任意一个就弹出 PRD 创作引导
反向关键词(NEGATIVE_KEYWORDS)：包含任意一个则跳过引导提示
可根据需求自行增删关键词列表。
"""

import json
import sys
import re

# 正向关键词：命中任意一个即触发 PRD 引导
POSITIVE_KEYWORDS = [
    "prd",
    "需求文档",
    "产品需求",
    "产品文档",
    "企划书",
    "服务规划",
    "产品规划",
    "想做",
    "做应用",
    "做APP",
    "做产品",
    "做服务",
    "开发一款",
    "创建一个",
    "设计一个",
    "产品概念",
    "创意想法",
    "需求分析",
    "功能设计",
    "product requirement",
    "product spec",
]

# 反向关键词：命中任意一个则不弹出引导
NEGATIVE_KEYWORDS = [
    "修改prd",
    "更新prd",
    "修改代码",
    "热修复",
    "bug",
    "已有 prd",
    "有 prd",
    "已有产品",
    "已有文档",
    "已有需求",
]

def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
    except (json.JSONDecodeError, KeyError):
        return

    prompt = data.get("prompt", "").lower()
    if not prompt:
        return

    # 包含反向关键词则直接退出，不提示
    for neg in NEGATIVE_KEYWORDS:
        if neg in prompt:
            return

    # 匹配正向关键词
    matched = False
    for pos in POSITIVE_KEYWORDS:
        if pos in prompt:
            matched = True
            break

    if not matched:
        return

    # 匹配成功则输出引导文案
    result = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": (
                "[已检测到PRD需求] 识别到新的产品/APP创意想法。"
                "可以输入 /prd-create 命令开始撰写标准化PRD文档。"
                "如果已经在编写PRD或进行其他开发工作，请忽略本条提示。"
            ),
        }
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
