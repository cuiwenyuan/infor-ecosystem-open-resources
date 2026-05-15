---
title: "ION 集成错误代码 - 故障排查"
description: "Infor ION 集成常见错误代码，包括 BOD 错误、API 错误、OAuth2 认证错误等。"
---

# Infor ION 集成错误代码

> ION 集成常见错误代码速查手册（社区贡献，仅供参考）。

---

## BOD 错误

### BOD Validation Error

**产品**：Infor ION  
**严重度**：⚠️ 警告  
**描述**：BOD 数据验证失败，XML 不符合 XSD 规则。

**原因**：
- BOD XML 缺少必填字段
- 字段格式不正确（日期、数字格式）
- 字段值超出允许范围
- 枚举值无效

**解决方案**：
1. 使用 XSD 验证 BOD XML（工具：`xmllint --schema schema.xsd data.xml`）
2. 查看 ION Desk → Error BODs 查看详细错误
3. 修复 BOD 数据，重新提交

**示例（正确 BOD 格式）**：
```xml
<ItemMaster>
  <Item>
    <ItemID>10001</ItemID>  <!-- 必填 -->
    <ItemName>Steel Pipe</ItemName>
    <UOM>EA</UOM>
  </Item>
</ItemMaster>
```

**参考**：
- [schema.infor.com](https://schema.infor.com/) - 官方 BOD Schema 资源
- [ION BOD 处理指南](https://www.netray.co/resources/infor-ion-bod-message-processing)

---

### BOD Transformation Error

**产品**：Infor ION  
**严重度**：⚠️ 警告  
**描述**：BOD 转换规则执行失败。

**原因**：
- 转换规则（XSLT）语法错误
- 源 BOD 结构变更，转换规则未更新
- XPath 表达式错误

**解决方案**：
1. 在 ION Desk → BOD Transformation 测试转换规则
2. 使用 XSLT 调试工具（如 Oxygen XML Editor）
3. 更新转换规则以匹配新的 BOD 结构

---

### Error BOD Generated

**产品**：Infor ION  
**严重度**：⚠️ 警告  
**描述**：系统生成错误 BOD，表示处理失败。

**原因**：
- 目标应用返回错误
- BOD 数据验证失败
- 网络超时

**解决方案**：
1. 在 ION Desk → Error BODs 查看错误详情
2. 修复根本原因（目标应用错误、数据错误等）
3. 使用"Resubmit"功能重新提交原始 BOD

**参考**：
- [ION Error BOD 处理 - Community](https://community.infor.com/discussion/34897/infor-ion-error-bod-confirm-bod-resubmit-original-message/p1)
- [Fail a BOD to generate Error BOD](https://community.infor.com/discussion/399/is-it-possible-for-fail-a-bod-so-it-will-generate-error-bod)

---

## ION API 错误

### 401 Unauthorized

**产品**：Infor ION API Gateway  
**严重度**：❌ 错误  
**描述**：OAuth2 认证失败，Access Token 无效或过期。

**原因**：
- Client ID 或 Client Secret 错误
- Access Token 过期（通常 1 小时）
- 未正确配置 OAuth2 Scope

**解决方案**：
1. 重新获取 Access Token：
   ```bash
   curl -X POST https://your-tenant.infor.com/InforIONAPI/oauth2/token \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET"
   ```
2. 检查 Token 过期时间（通常 3600 秒）
3. 在 ION API Gateway 配置中检查 Scope 设置

---

### 403 Forbidden

**产品**：Infor ION API Gateway  
**严重度**：❌ 错误  
**描述**：权限不足，OAuth2 Scope 不包含所需权限。

**原因**：
- OAuth2 Scope 配置不正确
- 应用未授权访问目标 API

**解决方案**：
1. 在 ION API Gateway 中添加所需 Scope
2. 重新获取 Access Token（包含新 Scope）
3. 测试 API 调用

**参考**：
- [ION API 管理指南](https://docs.infor.com/ionapi/2021-x/en-us/ionapiag_cloud/default.html)

---

### 404 Not Found

**产品**：Infor ION API Gateway  
**严重度**：⚠️ 警告  
**描述**：API 端点不存在或路径错误。

**原因**：
- API 路径拼写错误
- API 版本不正确
- 租户（Tenant）配置错误

**解决方案**：
1. 查看 [schema.infor.com](https://schema.infor.com/) 确认正确路径
2. 检查 API 版本（如 `/api/v1/` vs `/api/v2/`）
3. 确认租户 URL 正确（`https://your-tenant.infor.com/`）

---

## ION Workflow 错误

### Workflow Instance Failed

**产品**：Infor ION Workflow  
**严重度**：⚠️ 警告  
**描述**：工作流实例执行失败。

**原因**：
- 自定义活动（Custom Activity）代码错误
- 用户任务（User Task）超时
- 连接器（Connector）配置错误

**解决方案**：
1. 在 ION Desk → Workflow Monitoring 查看失败实例
2. 查看错误详情和堆栈跟踪
3. 修复代码或配置，重新启动工作流实例

---

## 调试技巧

### 查看 ION 日志

1. **ION Desk → Monitoring → Logs**
   - 查看 API 调用日志
   - 查看 BOD 处理日志
   - 查看 Workflow 执行日志

2. **启用调试日志**
   - 在 ION API Gateway 中启用"Debug Mode"
   - 查看详细的请求/响应报文

### 测试 BOD 处理

```bash
# 1. 使用 Postman 发送测试 BOD
curl -X POST https://your-tenant.infor.com/InforIONAPI/bod \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/xml" \
  -d @test-bod.xml

# 2. 查看 BOD 处理状态
curl -X GET https://your-tenant.infor.com/InforIONAPI/bod/status/{bod-id} \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 相关资源

- [ION API 开发](../developer/ion-api.md) - ION API 开发资源
- [ION BOD 集成](../resources/ion-integration.md) - ION BOD 集成指南
- [故障代码百科首页](../troubleshooting/index.md) - 按产品线浏览

---

> ⚠️ **免责声明**：本页面内容为社区贡献，仅供参考。错误代码的解决方案可能因环境不同而有所差异，请在生产环境操作前充分测试。

**最后更新**：2026-05-11
