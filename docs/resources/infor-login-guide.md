---
description: Infor 登录指南：Ming.le / Infor OS Portal 租户地址、SSO 与 MFA 登录步骤、常见登录故障排查（找不到入口、密码错误、角色缺失等）
---

# Infor 登录指南（Ming.le / Infor OS Portal）

> 💡 **最重要的一个事实**：Infor **没有统一的公开登录入口**。每个客户租户（tenant）都有**各自独立的 URL**，所以直接搜「infor login」几乎不可能找到你的入口——正确地址在你公司的入职邮件、内网书签，或直接问贵司 IT。

## 你应该在哪里登录

大多数云部署下，**统一入口是 Infor OS Portal（也叫 Ming.le）**，典型地址形如：

```
https://mingle-portal.inforcloudsuite.com/<租户ID>/<...>
```

登录一次 Portal 后，即可从门户内打开你被授权的所有应用（CloudSuite、ION Desk、Document Management、Factory Track、CPQ 等），无需二次登录。

## 员工登录步骤（SSO 环境）

1. **使用贵司提供的租户 URL**——用 IT 发的书签或链接，警惕来源不明的邮件链接
2. **选择公司登录方式**——若出现"企业身份提供商 vs 本地账号"选项，通常选企业选项
3. **输入工作凭据**——SSO 环境下就是你的邮箱 / 域账号密码
4. **完成多因素认证（MFA）**——推送确认、验证码或安全密钥
5. **从门户打开应用**——在 Portal 中点击需要的应用磁贴（HR 自助、财务、报表等）

**外包与临时用户**可能使用 Infor 本地账号（非 SSO），此时密码重置走登录页上的 Forgot Password 链接。

## 租户首次开通流程（管理员视角）

- 客户需指定一名 **bootstrap 管理员**，并把邮箱报给 Infor 代表
- Infor 发送激活邮件（**48 小时内有效**）→ 设置 Ming.le 账号密码 → 创建账户
- 随后 Infor 再发"Welcome"邮件，内含各应用的访问 URL 清单
- bootstrap 管理员负责给其他用户开号并分配角色

## 常见登录故障排查

| 症状 | 可能原因 | 处理建议 |
|------|---------|---------|
| 页面 404 / 证书告警 | URL 错误或书签过期 | 向 IT 索要最新租户地址，删除旧书签 |
| 密码被拒 | 目录密码过期 | 走贵司密码自助门户重置后再试 |
| 登录成功但看不到应用磁贴 | 角色或安全组未分配 | 找管理员在 Infor 中为你的账号申请角色 |
| 无限重定向循环 | 浏览器残留 Cookie / 混用了个人账号 | 清理该站点 Cookie，或用隐私窗口 / 独立浏览器 Profile |
| MFA 验证收不到 | 换了手机或验证器未注册 | 联系服务台重新注册 MFA 因子 |
| 提示浏览器不受支持 | 浏览器过旧 | 更新到受支持的现代浏览器 |

**服务台高频案例**：同一个浏览器里登录过个人 Microsoft / Google 账号，会被错误身份"劫持"跳转——用隐私窗口或为工作账号单开一个浏览器 Profile 通常即可解决。

## 管理员建议（HR / IT）

- 将 Infor 接入**公司身份提供商（IdP）**：入职即开通、离职即回收
- 把**目录组映射到 Infor 安全角色**，岗位变动时权限自动跟随
- 服务账号（API / 集成）与人类用户分开管理（参见 [ION API](ion-integration.md) 与 [ION 产品页](../by-product/ion.md)）
- 涉及 HR / 薪酬数据的租户，建议按 NIST SP 800-63B 思路提升认证强度（MFA 必备，优先防钓鱼因子）

## 相关资源

- [Infor OS](../by-product/infor-os.md) · [ION](../by-product/ion.md)
- [官方文档索引](official-docs.md) · [排错手册](../troubleshooting/index.md)
- 找不到入口？先看[常见问题](infor-faq.md)，再联系贵司 IT

---

**最后更新**：2026-11-04
**维护者**：崔文远 Troy Cui
