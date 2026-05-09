---
title: "ION BOD 集成开发指南 - Infor 生态开放资源导航站"
description: "Infor ION 与 BOD（Business Object Document）集成开发资源汇总，包含教程、工具、最佳实践和社区讨论。"
---

# ION BOD 集成开发指南

> Infor ION（Intelligent Open Network）是 Infor 的技术中间件平台，基于 OAGIS 标准的 BOD（Business Object Document）实现系统间数据交换。本页面汇总 ION/BOD 相关的学习资源、开发工具和最佳实践。

---

## 📖 ION & BOD 基础

### 什么是 ION？

ION 是 Infor 的**企业服务总线（ESB）与集成平台**，提供：

- **BOD 消息路由**：基于 OAGIS 标准的 XML 消息（Business Object Document）
- **文档流（Document Flow）**：可视化配置消息路由规则，无需编码
- **连接器（ION Connect）**：预构建的 Infor 产品间连接器
- **API 网关**：REST/SOAP API 发布与管理
- **监控与追踪**：消息流转实时监控

### 什么是 BOD？

BOD（Business Object Document）是遵循 **OAGIS（Open Applications Group Integration Specification）** 标准的 XML 消息，用于在 Infor 系统间传递业务数据。

**常见 BOD 类型**：

| BOD 类型 | 说明 | 典型场景 |
|----------|------|----------|
| **SalesOrder** | 销售订单 | LN/M3 → CRM 订单同步 |
| **ItemMaster** | 物料主数据 | PLM → ERP 物料同步 |
| **PurchaseOrder** | 采购订单 | ERP → WMS 采购订单 |
| **Billing** | 开票 | ERP → 财务系统 |
| **Inventory** | 库存 | WMS → ERP 库存更新 |
| **WorkOrder** | 生产工单 | PLM → ERP → MES |

---

## 📚 官方文档与教程

| 资源 | 类型 | 链接 |
|------|------|------|
| **Infor ION 官方文档** | 官方文档中心 | [访问](https://docs.infor.com/) |
| **Infor ION 快速参考指南** | Knowledge Base 文章 | [访问](https://community.infor.com/kb/articles/20-infor-ion) |
| **Infor BOD 开发系列（PDF）** | FullOnBaan 培训材料 | [预览下载](https://training.fullonbaan.com/preview/preview_BOD.pdf) |
| **Infor Developer Portal - ION 教程** | 官方开发者教程 | [访问](https://developer.infor.com/tutorials) |
| **Infor Documentation Central** | 官方文档入口 | [访问](https://docs.infor.com/zh-cn/) |

---

## 📝 第三方教程与博客

| 资源 | 类型 | 说明 | 链接 |
|------|------|------|------|
| **Sama Integrations - BOD 详解** | 技术博客 | 详解 BOD 是什么及如何在 ION 中驱动集成 | [访问](https://samaintegrations.com/what-are-infor-bods-and-how-do-they-power-integration-in-ion/) |
| **Sama Consulting - ION 集成指南** | 技术博客 | ION 架构、集成实施步骤、真实场景、2025 最佳实践 | [访问](https://samaconsultinginc.com/blogs/infor-ion-integration-guide-streamlining-enterprise-systems-for-2025/) |
| **Netray - ION BOD 消息处理** | 技术指南 | BOD 消息处理配置、XML 映射、转换规则、错误处理 | [访问](https://www.netray.co/resources/infor-ion-bod-message-processing) |
| **FullOnBaan - BOD 开发系列** | PDF 培训材料 | BOD 开发完整系列，含 OAGIS 标准详解 | [访问](https://training.fullonbaan.com/) |
| **Crossroads RMC - ION 集成实战** | 技术博客 | LN 与第三方系统集成实战经验 | [访问](https://www.crossroadsrmc.com/) |

---

## 🔧 开发工具

| 工具 | 类型 | 说明 | 链接 |
|------|------|------|------|
| **ION 开发工具包** | 官方工具 | ION 开发、测试与部署工具集 | [Infor Marketplace](https://marketplace.infor.com/) |
| **ION API Gateway** | 官方工具 | REST API 发布与管理 | [Infor 官文](https://docs.infor.com/) |
| **BOD 测试工具** | 社区工具 | BOD 消息生成与验证 | [FullOnBaan](https://training.fullonbaan.com/) |
| **XML 映射工具** | 第三方工具 | ION Document Flow XML 映射配置 | [Netray 指南](https://www.netray.co/resources/infor-ion-bod-message-processing) |

---

## 📋 开发流程

### BOD 开发与部署流程

```
1. 确定业务场景 → 选择 BOD 类型（SalesOrder/ItemMaster/...）
        ↓
2. 在 ION 中创建 Document Flow
        ↓
3. 配置源系统（发布 BOD）和目的系统（接收 BOD）
        ↓
4. 配置 XML 映射（XSLT）和转换规则
        ↓
5. 测试 BOD 消息（使用 BOD 测试工具）
        ↓
6. 部署到生产环境
        ↓
7. 监控消息流转（ION Monitoring）
```

### 常用 BOD 操作

| 操作 | BOD Verb | 说明 |
|------|----------|------|
| **创建** | `Add` | 新增业务数据 |
| **更新** | `Change` | 修改现有数据 |
| **删除** | `Delete` | 删除数据 |
| **查询** | `Get` | 查询数据 |
| **同步** | `Sync` | 批量同步 |

---

## 🌐 OAGIS 标准

| 资源 | 说明 | 链接 |
|------|------|------|
| **OAGIS 官方标准** | OAGIS Integration Specification 标准文档 | [访问 OAGIS](https://www.oasis-open.org/) |
| **Infor BOD 开发指南** | 基于 OAGIS 的 BOD 开发详解 | [FullOnBaan PDF](https://training.fullonbaan.com/preview/preview_BOD.pdf) |
| **BOD XML Schema** | BOD XSD 架构文件 | [Infor 官文](https://docs.infor.com/) |

---

## 💬 社区与支持

| 资源 | 类型 | 链接 |
|------|------|------|
| **Infor Community - ION 板块** | 官方社区 | [访问](https://community.infor.com/) |
| **Infor Global Community - ION** | 用户讨论 | [访问](https://community.infor.com/) |
| **FullOnBaan - ION/BOD 知识库** | 第三方知识库 | [访问](https://training.fullonbaan.com/) |
| **Stack Overflow - Infor ION** | 开发者问答 | [访问](https://stackoverflow.com/) |

---

## 📌 ION/BOD 学习路径

### 初学者（0-3 个月）

1. 阅读 [Infor ION 官方文档](https://docs.infor.com/) 了解基础概念
2. 学习 [Sama Integrations - BOD 详解](https://samaintegrations.com/what-are-infor-bods-and-how-do-they-power-integration-in-ion/)
3. 在测试环境创建第一个 Document Flow
4. 使用 [BOD 开发系列 PDF](https://training.fullonbaan.com/preview/preview_BOD.pdf) 系统学习

### 进阶（3-12 个月）

1. 深入 OAGIS 标准和 BOD XML Schema
2. 学习 XSLT 映射和转换规则（[Netray 指南](https://www.netray.co/resources/infor-ion-bod-message-processing)）
3. 实施复杂集成场景（跨产品、跨系统）
4. 参与 [Infor Community - ION 板块](https://community.infor.com/) 讨论

---

## 🔗 相关资源

- [Infor OS](../by-product/infor-os.md) — ION 运行平台
- [Infor LN 开发系列](ln-4gl-tips.md) — LN 与 ION 集成开发
- [工具与插件](tools.md) — ION 开发工具
- [博客与教程](blogs.md) — 更多 ION 集成教程

---

**最后更新**：2026-05-09
