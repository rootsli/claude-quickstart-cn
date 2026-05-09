# 编码风格规范

## 文件结构
每个文件遵循单一职责原则，职责拆分做到可独立替换。
- 组件：仅负责 UI 渲染
- 自定义钩子：负责状态管理与业务逻辑
- 工具函数: 纯函数（无副作用）
- 类型: 类型定义（遵循单一数据源）

## 命名规范
- 变量 / 函数：小驼峰 camelCase（示例：getUserName）
- 组件 / 类型：大驼峰 PascalCase（示例：UserProfile）
- 常量：大写蛇形 UPPER_SNAKE_CASE（示例：MAX_RETRY_COUNT）
- 布尔值：统一使用 is/has/should 前缀（示例：isLoading）

## 不可变性原则
禁止直接修改对象和数组，采用新建副本方式处理。

```typescript
// 不推荐
user.name = newName;
items.push(newItem);

// 推荐写法
const updated = { ...user, name: newName };
const newItems = [...items, newItem];
// 数组转换优先使用 map、filter、reduce。
// 禁止使用 push、splice、sort 等直接变更原数组的方法。
```

## 条件判断规范
- 使用 early return 减少嵌套（guard clause）
```typescript
// 不推荐：深层嵌套
function process(user: User | null) {
  if (user) {
    if (user.isActive) {
      return doWork(user);
    }
  }
  return null;
}

// 推荐：guard clause
function process(user: User | null) {
  if (!user) return null;
  if (!user.isActive) return null;
  return doWork(user);
}
```

## 基础错误处理
- 禁止忽略异常（不允许空 catch 捕获）
```javascript
// 不推荐：静默失败
try { doSomething(); } catch (e) {}

// 推荐：处理异常或向上抛出
try {
  doSomething();
} catch (error) {
  console.error('操作失败:', error.message);
  // 向用户弹窗提示 或 执行兜底逻辑
}
```
- 调试结束后必须删除 `console.log`
- 错误信息中禁止暴露内部敏感信息（数据库结构、服务器路径等）

## TypeScript 基本规则
- 拒绝使用 `any`，优先使用精确类型；不确定类型时用 `unknown`
- 尽量减少 `as` 类型断言，优先通过 typeof、instanceof 做类型收窄
```typescript
// 不推荐
const data = response as UserData;

// 推荐：类型守卫校验
if (typeof response === 'object' && 'name' in response) {
  const data = response; // 自动完成类型收窄
}
```

## TypeScript 严格模式
- `tsconfig.json` 中必须设置 `strict: true`
- 在编译阶段拦截空值引用、类型不匹配、隐式 any 等问题
- 关闭严格模式会导致大量只能在运行时才能发现的 Bug 不断累积

## 安全编码规范
- 避免直接操作 DOM 元素，使用 React 组件库
- 将用户输入插入 HTML 时必须做转义处理
- URL 参数、表单数据、Cookie 值全部视为不可信输入
- 认证令牌优先使用 HttpOnly Cookie 或服务端会话管理，**不建议存储在 localStorage**
```typescript
// 不推荐：存在 XSS 漏洞
element.innerHTML = userInput;

// 推荐：安全的文本插入
element.textContent = userInput;
```

## import 顺序规范
1. 第三方依赖包（react、next 等）
2. 项目内部模块（@/components 等别名路径）
3. 相对路径模块（./utils 等）
