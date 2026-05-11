---
title: "WMS 错误代码 - 故障排查"
description: "Infor WMS 常见错误代码，包括 REST API 错误、集成错误、波次规划错误等。"
---

# Infor WMS 错误代码

> Infor WMS 常见错误代码速查手册（社区贡献，仅供参考）。

---

## REST API 错误

### 400 Bad Request

**产品**：Infor WMS  
**严重度**：⚠️ 警告  
**描述**：REST API 请求参数错误。

**原因**：
- 请求体（Body）JSON 格式错误
- 必填字段缺失
- 字段值类型不匹配（如字符串传给数字字段）

**解决方案**：
1. 验证 JSON 格式（使用 [JSONLint](https://jsonlint.com/)）
2. 查看 API 文档，确认必填字段
3. 使用 Postman 或 curl 测试请求

**示例（正确请求格式）**：
```json
{
  "itemId": "10001",
  "quantity": 10,
  "uom": "EA"
}
```

---

### 401 Unauthorized

**产品**：Infor WMS  
**严重度**：❌ 错误  
**描述**：认证失败，API Key 或 Token 无效。

**原因**：
- API Key 错误或未激活
- OAuth2 Token 过期
- 用户未授权访问 WMS API

**解决方案**：
1. 检查 API Key 是否正确（在 WMS 管理控制台中查看）
2. 重新获取 OAuth2 Token
3. 检查用户权限（是否授权访问 WMS API）

---

### 404 Not Found

**产品**：Infor WMS  
**严重度**：⚠️ 警告  
**描述**：资源不存在（如物料、订单、库位等）。

**原因**：
- 资源 ID 拼写错误
- 资源已被删除
- 租户（Tenant）配置错误

**解决方案**：
1. 验证资源 ID 是否正确
2. 使用 GET 请求先查询资源是否存在
3. 检查租户配置

---

### 500 Internal Server Error

**产品**：Infor WMS  
**严重度**：❌ 错误  
**描述**：WMS 内部服务器错误。

**原因**：
- WMS 服务异常
- 数据库连接有问题
- 代码 Bug

**解决方案**：
1. 查看 WMS 管理控制台 → 日志
2. 联系 Infor 支持（Support Case）
3. 提供请求 ID（Request ID）和错误详情

---

## 波次规划（Wave Planning）错误

### Wave Planning Failed

**产品**：Infor WMS  
**严重度**：⚠️ 警告  
**描述**：波次规划失败，无法生成波次。

**原因**：
- 订单行无法满足（库存不足）
- 波次规则配置错误
- 库位不可用

**解决方案**：
1. 检查库存是否充足
2. 查看波次规则配置（Wave Template）
3. 检查库位状态（是否被锁定或不可用）
4. 查看波次规划日志（WMS → Wave Planning → Logs）

---

### No Available LPN

**产品**：Infor WMS  
**严重度**：⚠️ 警告  
**描述**：没有可用的 LPN（Logistics Product Number）用于分配。

**原因**：
- LPN 已用完（需要生成新 LPN）
- LPN 状态不正确（如已锁定）

**解决方案**：
1. 生成新 LPN：`WMS → LPN Management → Generate LPN`
2. 检查 LPN 状态：`WMS → LPN Management → View LPN Status`
3. 解锁 LPN（如需要）

---

## 集成错误

### IFD (Infor Fabric Data) 错误

**产品**：Infor WMS  
**严重度**：❌ 错误  
**描述**：通过 Infor Fabric（IFD）导入数据失败。

**原因**：
- IFD 文件格式错误
- 字段映射不正确
- 数据验证失败

**解决方案**：
1. 查看 IFD 错误日志（`WMS → Integration → IFD → Error Logs`）
2. 验证 IFD 文件格式（CSV/Excel）
3. 修复数据错误，重新导入

---

### EDI 错误

**产品**：Infor WMS  
**严重度**：⚠️ 警告  
**描述**：EDI 报文处理失败。

**原因**：
- EDI 格式错误（不符合 X12/EDIFACT 标准）
- 业务规则验证失败
- 合作伙伴配置错误

**解决方案**：
1. 使用 EDI 验证工具验证报文
2. 查看 EDI 错误日志（`WMS → Integration → EDI → Error Logs`）
3. 检查合作伙伴配置（Partner Profile）

---

## 调试技巧

### 查看 WMS 日志

1. **WMS 管理控制台 → 监控 → 日志**
   - 应用日志（Application Log）
   - 集成日志（Integration Log）
   - 性能日志（Performance Log）

2. **启用调试日志**
   - `WMS → System Configuration → Logging → Enable Debug Mode`
   - 查看详细的 API 请求/响应

### 测试 REST API

```bash
# 1. 测试连通性
curl -v https://your-wms-tenant.infor.com/wms/api/v1/health

# 2. 查询物料
curl -H "Authorization: Bearer YOUR_TOKEN" \
  https://your-wms-tenant.infor.com/wms/api/v1/items/10001

# 3. 创建出库订单
curl -X POST https://your-wms-tenant.infor.com/wms/api/v1/orders/outbound \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d @order.json
```

---

## 官方文档

| 资源 | 链接 |
|------|------|
| **Infor WMS 文档库** | [访问](https://docs.infor.com/wms/latest/en-us/) |
| **WMS REST API 文档** | [查看](https://developer.infor.com/hub/apis) |
| **WMS 集成指南** | [查看](https://docs.infor.com/wms/latest/en-us/) |

---

## 社区资源

- [Infor Global Community - WMS User Group](https://community.infor.com/) - 官方社区
- [Stack Overflow - infor-wms 标签](https://stackoverflow.com/questions/tagged/infor-wms) - 问答
- [WMS 波次规划优化](https://www.infor.com/) - 最佳实践

---

> ⚠️ **免责声明**：本页面内容为社区贡献，仅供参考。错误代码的解决方案可能因环境不同而有所差异，请在生产环境操作前充分测试。

**最后更新**：2026-05-11
