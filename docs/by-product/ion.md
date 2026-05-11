---
title: "Infor ION - Infor 生态开放资源导航站"
description: "Infor ION 集成平台资源导航，收录 ION 相关的顾问公司、BOD 开发工具、API 集成资源和实施指南。"
---

# Infor ION

> Infor ION 是 Infor 生态系统的核心集成中间件，以 BOD（Business Object Document）为标准消息格式，通过事件驱动架构连接 Infor 各产品及外部系统，实现真正的松耦合集成。

---

## 产品概述

| 项目 | 说明 |
|------|------|
| **产品类型** | 事件驱动集成平台（ESB / iPaaS） |
| **核心概念** | BOD（Business Object Document）标准消息格式 |
| **集成 ERP** | Infor LN、M3、CSI、WMS、HCM、EAM 等全产品线 |
| **部署方式** | 云部署（Infor OS/AWS） |
| **目标客户** | 使用 Infor 产品需要进行系统集成的企业 |

---

## 核心组件

### ION Gateway / API Gateway

- **API 管理**：REST/SOAP API 发布、策略控制、安全防护
- **代理端点（Proxy Endpoint）**：对外暴露标准化 API 接口
- **限流与鉴权**：API 调用频率限制、OAuth/SAML 鉴权
- **监控与日志**：API 调用日志、错误追踪、性能监控

### ION Connect

- **文档流（Document Flow）设计器**：可视化编排 BOD 的流转逻辑
- **转换器（Transformer）**：BOD 格式转换（XML↔JSON↔EDIFACT）
- **路由规则**：基于条件的 BOD 路由（按公司、供应商、单据类型等）
- **重发机制**：传输失败自动重试，保证消息送达

### ION Workflow

- **人工审批节点**：BOD 处理过程中的人工干预节点
- **业务规则引擎**：基于条件的自动决策（如三单匹配自动通过）
- **SLA 监控**：审批超时自动升级提醒
- **与 Infor OS Workflow 联动**：跨产品统一工作流体验

### ION Data Lake

- **ETL 数据整合**：从各 Infor 产品抽取数据到统一数据湖
- **BOD 归档**：历史 BOD 存档，支持审计追溯
- **与 Birst 集成**：数据湖直接作为 Birst 的数据源
- **数据血缘追踪**：BOD 从源头到终点的完整追踪

---

## BOD（Business Object Document）体系

BOD 是 ION 集成的核心通信协议。

### BOD 操作类型

| 操作 | 说明 | 典型场景 |
|------|------|----------|
| **Sync** | 同步主数据（Customer、Item、BOM） | 新建/更新物料主数据 |
| **Process** | 处理业务交易（SalesOrder、PurchaseOrder） | 创建销售订单 |
| **GET** | 查询请求 | 查询库存可用量 |
| **Show** | 查询结果返回 | 返回库存查询结果 |
| **Confirm** | 确认收到并处理 | 发货确认 BOD |
| **Cancel** | 取消之前的操作 | 取消销售订单 |

### 常见 BOD 类型

| BOD | 说明 |
|-----|------|
| **ItemMaster** | 物料主数据 |
| **SalesOrder** | 销售订单 |
| **PurchaseOrder** | 采购订单 |
| **Invoice** | 发票 |
| **Inventory** | 库存快照 |
| **GeneralLedger** | 总账凭证 |
| **BOM** | 物料清单 |
| **ProductionOrder** | 生产订单 |

### BOD 订阅模型

```
[发送方系统] --发布 BOD--> [ION Connect] --路由--> [订阅方系统]
   LN 发布 SalesOrder       规则匹配        M3 接收 SalesOrder
                             ↓
                      WMS 接收 SalesOrder
```

---

## 官方 BOD Schema 资源

Infor 在 `https://schema.infor.com/` 提供所有 BOD 的官方 XSD Schema 文件，供开发者下载并用于集成开发中的消息校验。

### Schema 版本目录

| 版本 | 说明 | 链接 |
|------|------|------|
| **9.0（最新）** | 当前主流版本，覆盖全部 BOD 类型 | [schema.infor.com/9.0/](https://schema.infor.com/9.0/) |
| 2.15.x | 维护迭代版本 | [schema.infor.com/2.15.x/](https://schema.infor.com/2.15.x/) |
| 2.14.x | 维护迭代版本 | [schema.infor.com/2.14.x/](https://schema.infor.com/2.14.x/) |
| 2.13.x | 维护迭代版本 | [schema.infor.com/2.13.x/](https://schema.infor.com/2.13.x/) |
| 2.12.x | 维护迭代版本 | [schema.infor.com/2.12.x/](https://schema.infor.com/2.12.x/) |
| 更早版本（2.1~2.11） | 历史版本，逐步淘汰 | [查看全部版本](https://schema.infor.com/) |

> ⚠️ 建议始终使用 Infor LN/M3/ION 当前版本对应的最低 Schema 版本，以确保 BOD 字段兼容性。

### 目录结构说明

每个版本目录下包含：
```
/{version}/
├── BODs/
│   ├── Developer/     ← 面向开发者的 BOD XSD 文件（最常用）
│   └── Standalone/    ← 独立版本 BOD XSD 文件
└── Resources/         ← 配套说明文档、示例代码
```

### 各操作类型 BOD XSD 文件速查（9.0 版本）

| 操作类型 | 典型 BOD（XSD 文件名） | 说明 |
|----------|---------------------------|------|
| **Acknowledge** | AcknowledgeSalesOrder, AcknowledgePurchaseOrder, AcknowledgeInvoice, AcknowledgeProductionOrder, AcknowledgeItemMaster 等 | 确认类，响应处理结果的回执 |
| **Cancel** | CancelSalesOrder, CancelPurchaseOrder, CancelProductionOrder, CancelInvoice, CancelRequisition 等 | 取消类，撤销已提交的业务对象 |
| **Change** | ChangeSalesOrder, ChangePurchaseOrder, ChangeProductionOrder, ChangeInvoice, ChangeItemMaster 等 | 变更类，修改已存在业务对象的字段 |
| **Get** | GetSalesOrder, GetPurchaseOrder, GetItemMaster, GetBOM, GetInventoryBalance, GetProductionOrder 等 | 单对象查询，返回单条业务对象详情 |
| **GetList** | GetListSalesOrder, GetListPurchaseOrder, GetListItemMaster, GetListProductionOrder 等 | 列表查询，返回满足条件的对象列表 |
| **List** | ListSalesOrder, ListItemMaster, ListPurchaseOrder, ListProductionOrder 等 | 列表类，与 GetList 类似，独立操作分类 |
| **Load** | LoadActualLedger, LoadBudgetLedger, LoadInvoiceLedgerEntry, LoadPayable, LoadReceivable 等 | 加载类，用于财务数据加载 |
| **Post** | PostJournalEntry, PostCostingActivity, PostMatchDocument 等 | 过账类，用于财务/成本数据过账 |
| **Process** | ProcessSalesOrder, ProcessPurchaseOrder, ProcessProductionOrder, ProcessInvoice, ProcessRequisition 等 | 处理类，触发业务逻辑执行 |
| **Respond** | RespondSalesOrder, RespondPurchaseOrder, RespondProductionOrder, RespondQuote 等 | 响应类，返回处理响应给调用方 |
| **Show** | ShowSalesOrder, ShowPurchaseOrder, ShowItemMaster, ShowBOM, ShowInventoryBalance 等 | 展示类，返回查询结果给调用方 |
| **Sync** | SyncItemMaster, SyncBOM, SyncSalesOrder, SyncPurchaseOrder, SyncCustomerPartyMaster 等 | 同步类，用于主数据跨系统同步 |
| **Update** | UpdateSalesOrder, UpdatePurchaseOrder, UpdateProductionOrder, UpdateInvoice 等 | 更新类，更新对象状态或字段 |
| **Create** | CreateProductionOrder, CreateMaintenanceOrder, CreateRequisition 等 | 创建类，生成新的业务对象 |
| **Receive** | ReceivePurchaseOrder, ReceiveProductionOrder, ReceiveMoveInventory 等 | 接收类，接收外部系统传来的 BOD |
| **Process ConfirmWIP / Change ConfirmWIP** | ProcessConfirmWIP, ChangeConfirmWIP, RespondConfirmWIP, UpdateConfirmWIP 等 | WIP（在制品）确认相关 BOD（LN 制造核心） |

> 📂 **完整文件列表**：请访问 [schema.infor.com/9.0/BODs/Developer/](https://schema.infor.com/9.0/BODs/Developer/) 查看全部 XSD 文件，每个 BOD 对应一个 `.xsd` 文件。

### 使用建议

1. **集成开发前**：从对应版本的 `BODs/Developer/` 目录下载所需 BOD 的 XSD 文件
2. **XML 校验**：在 ION Connect 的 Transformer 中使用 XSD 对 BOD XML 进行校验
3. **版本匹配**：BOD XSD 版本需与 ION / Infor ERP 版本保持一致，避免字段缺失导致解析失败
4. **优先使用标准 BOD**：Infor 预置 200+ 标准 BOD，仅在标准 BOD 无法满足时再自定义扩展

---

## 与 Infor 生态集成

| Infor 产品 | ION 集成方式 |
|-------------|---------------|
| [Infor LN](ln.md) | LN 原生发布/订阅 BOD，涉及销售/采购/生产/财务全流程 |
| [Infor M3](m3.md) | M3 原生 BOD 支持，与 ION 深度集成 |
| [Infor WMS](wms.md) | WMS 接收采购入库 BOD、发货 BOD，库存变动发布 BOD |
| [Infor Nexus](nexus.md) | Nexus 通过 ION 接收订单 BOD，发货状态回写 |
| [Infor Birst](birst.md) | ION Data Lake 作为 Birst 数据源 |
| [Infor OS](infor-os.md) | ION 运行在 Infor OS 之上，共享 IAM 身份 |

---

## 第三方系统集成为例

### 与外部系统集成

| 外部系统 | 集成方式 |
|----------|----------|
| **Salesforce / CRM** | ION API Gateway 暴露 REST API，CRM 调用创建销售订单 |
| **Shopify / 电商** | 电商订单通过 ION 转换为 SalesOrder BOD 传入 ERP |
| **银行/支付** | 付款确认 BOD 回写 ERP 应收/应付 |
| **EDI / EDIFACT** | ION Connect 转换器，EDIFACT ↔ BOD 双向转换 |
| **SFTP / 文件** | ION 支持文件监听，XML/JSON 文件转 BOD |

---

## 第三方资源速查

### 顾问与实施公司

| 公司 | 地区 | 说明 |
|------|------|------|
| [mashfrog Group](../resources/consultants.md) | 欧洲 | M3、WMS、OS、**ION**、RPA 全栈实施 |
| [Sama Consulting](../resources/consultants.md) | 北美 | Infor 全产品线（含 ION/BOD）架构优化 |
| [PCG Services](../resources/consultants.md) | 北美 | 2025 Infor 年度制造合作伙伴，ION 集成实施 |
| [Tarento](../resources/consultants.md) | 亚太 | PLM/M3/LN 全产品线，ION 集成服务 |
| [Netray](../resources/consultants.md) | 中国 | ION BOD 二次开发、API 集成专项 |

### 博客与教程

| 资源 | 说明 |
|------|------|
| [Infor ION 官方文档](https://docs.infor.com/) | 官方 ION 产品文档（需登录 Infor Xtreme 支持门户）|
| [Infor 官方 BOD Schema 资源](https://schema.infor.com/) | 所有版本 BOD XSD Schema 文件官方下载站（无需登录）|
| [Infor Customer Community - ION](../resources/forums.md) | 官方用户社区 ION/BOD 讨论区 |
| [ION BOD 处理指南](../resources/tools.md) | BOD 消息处理开发指南 |

### 工具与插件

| 工具 | 说明 |
|------|------|
| [Infor ION](../resources/tools.md) | 集成平台，含 Gateway/Connect/Workflow/Data Lake |
| [ION API SDK](../resources/tools.md) | Java SDK，用于编程调用 ION API Gateway |
| [ION Development Guide](../resources/tools.md) | ION 开发指南，BOD 扩展与自定义 |
| [Infor ION Grid](../resources/tools.md) | ION 底层运行容器和管理控制台 |

---

## ION 实施最佳实践

### BOD 设计原则

1. **优先使用标准 BOD**：Infor 已预置 200+ 标准 BOD，优先复用
2. **自定义 BOD 需谨慎**：仅在标准 BOD 无法满足时扩展，遵循 OAGIS 标准
3. **BOD 粒度要合理**：过细导致消息风暴，过粗导致耦合度高

### 常见 Pitfalls

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| BOD 重复处理 | 多个订阅方重复触发 | 在 ION Connect 设置去重规则 |
| BOD 处理超时 | 目标系统响应慢 | 设置异步处理和重试机制 |
| BOD 版本不兼容 | ERP 升级后 BOD XSD 变化 | 在 ION Connect 加版本映射转换器 |

---

## 适用场景

**适合**：
- 已使用多款 Infor 产品，需要它们之间数据打通
- 需要将 Infor ERP 与外部系统（CRM、电商、EDI）集成
- 需要统一集成监控和错误追踪的企业

**不适合**：
- 仅使用单一 Infor 产品，无外部集成需求
- 已深度使用其他 iPaaS（MuleSoft、Dell Boomi）且无迁移意愿

---

## 相关产品

- [Infor OS](infor-os.md) — ION 运行平台，统一身份管理
- [Infor Nexus](nexus.md) — 供应链协同，通过 ION 与 ERP 集成
- [Infor Birst](birst.md) — ION Data Lake 作为 Birst 数据源
- [Infor LN](ln.md) / [Infor M3](m3.md) — ION 最主要的 BOD 发布方和订阅方

---

**最后更新**：2026-05-11
