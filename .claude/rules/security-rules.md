# 安全规范

## 认证与授权

- 所有 API 接口必须应用认证中间件
- 访问资源时必须校验所属权（防止**越权访问 IDOR**）
- 必须校验 JWT / 会话令牌是否过期
- 权限校验仅在服务端执行，**不信任客户端权限判断**

```typescript
// 不推荐：只在前端做权限判断
if (user.role === 'admin') showAdminPanel();

// 推荐：服务端校验权限后再返回数据
// API: GET /admin/dashboard（由中间件校验角色）
```

## 输入校验

- 所有用户输入必须在服务端进行校验
- SQL 查询：仅使用参数绑定，**禁止字符串拼接**
- HTML 输出：必须做转义处理以防范 XSS 攻击
- 文件上传：同时校验后缀名、MIME 类型、文件大小
- URL 输入：屏蔽内网 IP 网段，防止 SSRF 攻击

```typescript
// 不推荐：存在 SQL 注入漏洞
const query = `SELECT * FROM users WHERE id = '${userId}'`;

// 推荐：使用参数绑定
const query = `SELECT * FROM users WHERE id = $1`;
await db.query(query, [userId]);
```

## OWASP Top 10 检查清单

新建 API 接口时，必须逐项检查以下风险项。

| 序号 | 安全威胁 | 检查事项 |
|---|------|---------|
| 1 | Injection | 防止 SQL/NoSQL/OS 命令注入 |
| 2 | Broken Authentication | 确认无法绕过登录认证 |
| 3 | Sensitive Data Exposure | 敏感数据加密 / 掩码脱敏处理 |
| 4 | XXE漏洞 | 关闭 XML 解析器外部实体引用|
| 5 | Broken Access Control | 拦截无权限用户访问私有资源 |
| 6 | Security Misconfiguration | 关闭默认配置、关闭调试模式 |
| 7 | XSS 跨站脚本 | 对用户输入做转义过滤 |
| 8 | Insecure Deserialization | 禁止对不可信数据进行反序列化 |
| 9 | Known Vulnerabilities | 依赖包漏洞扫描（npm audit） |
| 10 | Insufficient Logging | 记录登录失败、权限越轨等操作日志 |

## 密钥管理

- 严禁硬编码密钥 → 统一使用环境变量
- 禁止提交 `.env` 文件到代码仓库，必须加入 `.gitignore`
- 禁止在日志中打印密钥、令牌等敏感信息
- API 密钥仅允许在服务端使用，**禁止暴露到客户端**

```typescript
// 不推荐
const API_KEY = "sk-1234567890abcdef";

// 推荐
const API_KEY = process.env.API_KEY;
```

## 数据保护

- 敏感数据禁止明文存储（密码使用 bcrypt /argon2 加密）
- 全站仅使用 HTTPS 通信
- CORS 策略：仅放行必要域名，**禁止配置通配符 `*`**
- 启用接口限流（尤其登录、认证相关接口）
- 配置 HTTP 安全响应头（CSP、HSTS、X-Frame-Options 等）

## 上线前检查清单

```
[ ] 全部接口已统一接入认证/授权中间件
[ ] 已配置接口限流（全局 + 认证接口单独限流）
[ ] 已配置 HTTP 安全响应头
[ ] 已校验 CORS 允许跨域域名
[ ] 确认 .env 已加入 .gitignore 不被提交
[ ] 错误信息不暴露服务器内部细节
[ ] 依赖包漏洞已扫描修复（npm audit / pip audit）
[ ] 项目调试模式已关闭
```
