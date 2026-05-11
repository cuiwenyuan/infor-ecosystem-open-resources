---
title: "M3 / ION 错误代码 - 故障排查"
description: "Infor M3、ION、WMS 常见错误代码和排查方法。"
---

# Infor M3 / ION / WMS 错误代码

> M3、ION、WMS 常见错误代码速查手册（社区贡献，仅供参考）。

---

## M3 错误代码

### MI 事务错误

| 错误码 | 严重度 | 简介 | 解决方案 |
|--------|--------|------|----------|
| **MI 500** | ❌ 错误 | MI 事务内部服务器错误 | 检查 MI 事务日志，验证输入参数 |
| **MI 401** | ❌ 错误 | MI 事务未授权 | 检查用户权限和 M3 授权 |
| **MI 400** | ❌ 错误 | MI 事务请求无效 | 验证请求格式和必填字段 |
| **MI 404** | ⚠️ 警告 | MI 事务不存在 | 检查 MI 事务名称拼写 |

### XtendM3 错误

| 错误类型 | 简介 | 解决方案 |
|-----------|------|----------|
| **Script compilation error** | Groovy 脚本编译失败 | 检查语法，查看 XtendM3 日志 |
| **Before/After hook error** | 钩子函数执行失败 | 检查返回值，确保调用 `context.proceed()` |
| **M3 API call failed** | M3 API 调用失败 | 检查网络连接，验证 API 权限 |

**参考**：
- [XtendM3 文档](https://infor-cloud.github.io/xtendm3/docs/documentation)
- [XtendM3 Error Handling - Community](https://community.infor.com/discussion/11750/coding-xtendm3-error-handling/p1)

---

## ION 错误代码

### BOD 错误

| 错误类型 | 简介 | 解决方案 |
|-----------|------|----------|
| **BOD Validation Error** | BOD 数据验证失败 | 检查 BOD XML 是否符合 XSD 规则 |
| **BOD Transformation Error** | BOD 转换失败 | 检查映射规则，查看转换日志 |
| **Error BOD Generated** | 系统生成错误 BOD | 在 ION Desk 查看错误详情，修复后重新提交 |

### ION API 错误

| HTTP 状态码 | 简介 | 解决方案 |
|---------------|------|----------|
| **401 Unauthorized** | OAuth2 认证失败 | 检查 Client ID/Secret，确保 Access Token 未过期 |
| **403 Forbidden** | 权限不足 | 检查 OAuth2 Scope 配置 |
| **404 Not Found** | 端点不存在 | 检查 API 路径，参考 schema.infor.com |
| **500 Internal Server Error** | ION API Gateway 内部错误 | 查看 ION API 日志，联系 Infor 支持 |

**参考**：
- [ION Error BOD 处理](https://community.infor.com/discussion/34897/infor-ion-error-bod-confirm-bod-resubmit-original-message/p1)
- [ION API 管理指南](https://docs.infor.com/ionapi/2021-x/en-us/ionapiag_cloud/default.html)
- [ION 开发指南（PDF）](https://support.infor.com/esknowbase/root/DLPublic/47748/ion_12.0.x_ionopdg_en-us.pdf)

---

## WMS 错误代码

### REST API 错误

| HTTP 状态码 | 简介 | 解决方案 |
|---------------|------|----------|
| **400 Bad Request** | 请求参数错误 | 检查请求体和查询参数格式 |
| **401 Unauthorized** | 认证失败 | 检查 API Key 或 OAuth2 Token |
| **404 Not Found** | 资源不存在 | 检查 URL 路径和资源 ID |
| **500 Internal Server Error** | WMS 内部错误 | 查看 WMS 日志，联系 Infor 支持 |

### 集成错误

| 错误类型 | 简介 | 解决方案 |
|-----------|------|----------|
| **IFD (Infor Fabric Data) 错误** | 数据导入失败 | 检查 IFD 文件格式，查看错误日志 |
| **EDI 错误** | EDI 报文处理失败 | 检查 EDI 格式，验证业务规则 |

**参考**：
- [Infor WMS 文档](https://docs.infor.com/wms/latest/en-us/)
- [Stack Overflow - infor-wms 标签](https://stackoverflow.com/questions/tagged/infor-wms)

---

## 通用排查技巧

### 日志分析

| 产品 | 日志位置 | 说明 |
|------|----------|------|
| **Infor LN** | `$BSE/log/ln.log` | LN 应用日志 |
| **Infor M3** | ION Desk → Logs | M3 云日志 |
| **Infor ION** | ION Desk → Error BODs | ION 集成错误 |
| **Infor WMS** | WMS 管理控制台 → 日志 | WMS 应用日志 |

### 性能诊断

| 问题 | 排查步骤 |
|------|----------|
| **慢查询** | 1. 检查 SQL 执行计划 2. 查看索引使用 3. 分析 LN/DAL 代码 |
| **API 超时** | 1. 检查网络延迟 2. 查看 API 响应时间 3. 优化查询条件 |
| **内存不足** | 1. 检查 JVM 堆内存 2. 查看 GC 日志 3. 优化数据结构 |

### 网络排查

```bash
# 测试 API 连通性
curl -v https://your-tenant.infor.com/api/v1/health

# 检查 OAuth2 Token 是否有效
curl -H "Authorization: Bearer $TOKEN" https://your-tenant.infor.com/api/v1/userinfo

# 查看网络延迟
ping your-tenant.infor.com
traceroute your-tenant.infor.com  # Linux
tracert your-tenant.infor.com   # Windows
```

---

## 官方文档

| 产品 | 官方文档链接 |
|------|--------------|
| **Infor LN** | [LN 错误消息文档](https://docs.infor.com/ln/10.5/en-us/lnolh/help/tt/errors/overview.html) |
| **Infor M3** | [M3 核心文档](https://docs.infor.com/m3/core/latest/en-us/useradminlib_cloud/default.html) |
| **Infor ION** | [ION API 管理指南](https://docs.infor.com/ionapi/2021-x/en-us/ionapiag_cloud/default.html) |
| **Infor WMS** | [WMS 文档库](https://docs.infor.com/wms/latest/en-us/) |

---

## 社区资源

- [Infor Global Community](https://community.infor.com/) - 官方社区（需登录）
- [Stack Overflow - baan 标签](https://stackoverflow.com/questions/tagged/baan) - LN/Baan 问答
- [Stack Overflow - infor-m3 标签](https://stackoverflow.com/questions/tagged/infor-m3) - M3 问答
- [Stack Overflow - infor-ion 标签](https://stackoverflow.com/questions/tagged/infor-ion) - ION 问答

---

> ⚠️ **免责声明**：本页面内容为社区贡献，仅供参考。错误代码的解决方案可能因环境不同而有所差异，请在生产环境操作前充分测试。

**最后更新**：2026-05-11
