---
name: git-commit
description: 基于代码变更生成规范提交信息的 Git 提交消息生成器
---

# Git Commit

> Git 提交信息生成技能，根据代码变更自动生成规范的 commit message。

## 什么时候使用

当用户请求以下操作时使用此 skill：
- 生成 commit message
- 写提交信息
- 提交代码
- 描述代码变更

## 操作说明

### 提交信息格式

遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 类型

| 类型 | 说明 |
|------|---------------------|
| feat | 新功能 |
| fix | 修复 bug |
| docs | 文档变更 |
| style | 格式调整 |
| refactor | 重构 |
| perf | 性能优化 |
| test | 测试相关 |
| chore | 构建/工具 |

### 生成步骤

1. **分析变更** - 查看 `git diff` 或 `git status`
2. **确定类型** - 根据变更内容选择合适的类型
3. **提取范围** - 确定影响的模块或组件
4. **撰写主题** - 用简洁的语言描述变更（50 字符内）
5. **添加正文** - 如需要，详细说明变更原因和影响

### 规则
- 提交信息使用简体中文
- 主题行不超过 50 个字符
- 主题行结尾不加句号
- 正文每行不超过 72 个字符

## 示例

### 示例 1：新功能

```
feat(auth): 新增 OAuth2 登录支持

- 新增对 Google OAuth2 的登录支持
- 新增对 GitHub OAuth2 的登录支持
- 更新登录页面，添加社交登录按钮
```

### 示例 2：修复 Bug

```
fix(api): 修复用户服务中的空指针异常问题

- 修复了在用户不存在时的空指针异常问题

关闭了问题 #123
```

### 示例 3：文档更新

```
docs(readme): 更新安装说明

新增了 Docker 设置指南和澄清了环境变量的作用.
```

### 示例 4：重构

```
refactor(database): 异步代码从回调模式迁移至 async/await

将所有数据库操作转换为 async/await 模式，以提高可读性和错误处理能力.
```
