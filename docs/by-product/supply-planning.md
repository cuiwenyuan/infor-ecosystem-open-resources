---
title: "Infor Supply Planning - Infor 生态开放资源导航站"
description: "Infor Supply Planning 供应链计划资源导航，收录需求计划、供应计划、库存优化和相关实施资源。"
---

# Infor Supply Planning

> Infor Supply Planning 是 Infor 供应链计划（SCP）套件的核心组件，提供需求预测、供应平衡、库存优化和 S&OP（销售与运营计划）能力，与 Infor LN、M3 等 ERP 深度集成。

---

## 产品概述

| 项目 | 说明 |
|------|------|
| **产品类型** | 供应链计划（SCP） |
| **所属套件** | Infor Supply Chain Planning（含 Demand、Supply、Inventory 模块） |
| **集成 ERP** | Infor LN、Infor M3、CloudSuite Industrial |
| **部署方式** | 云部署（Infor Industry Cloud） |
| **目标客户** | 中大型制造企业、分销企业 |
| **核心目标** | 平衡需求与供应，优化库存，提升服务水平 |

---

## 核心功能

### 需求计划（Demand Planning）

- **多维度预测**：按产品、客户、地区、渠道等维度建模
- **预测算法库**：时间序列、因果分析、机器学习预测模型
- **新产品预测**：基于类似产品历史数据，预测新产品需求
- **促销与事件管理**：将促销、季节性因素纳入预测模型
- **协同需求计划（CPFR）**：与客户/分销商协同预测

### 供应计划（Supply Planning）

- **主生产计划（MPS）**：平衡需求与产能，制定可行的生产计划
- **物料需求计划（MRP）**：基于 MPS 展开 BOM，计算物料需求
- **产能计划（Capacity Planning）**：考虑设备、人力、模具等约束条件
- **多工厂协同计划**：跨工厂的供应网络优化
- **What-if 场景模拟**：多方案对比，支持决策

### 库存优化（Inventory Optimization）

- **安全库存计算**：基于服务水平目标和需求波动科学计算
- **库存目标设定**：按 SKU 分类（ABC 分析）设定差异化库存策略
- **在途库存（In-transit）可视化**：降低库存盲区
- **库存周转分析**：识别呆滞库存，优化库存结构

### S&OP（销售与运营计划）

- **统一计划流程**：销售、市场、生产、采购、财务一体化协作
- **S&OP 会议仪表板**：高层决策所需的一页视图（One-page View）
- **财务集成**：将运营计划转化为财务预测

---

## 与 Infor 生态集成

| Infor 产品 | 集成方式 |
|-------------|----------|
| [Infor LN](ln.md) | 需求→MRP→采购/生产订单，计划结果直接驱动 ERP 执行 |
| [Infor M3](m3.md) | 流程制造的计划与排产，与 M3 生产模块深度集成 |
| [Infor WMS](wms.md) | 库存实际 vs 计划对比，WMS 实时库存反馈到计划层 |
| [Infor Nexus](nexus.md) | 供应商协同，将供应计划传递给供应商 |
| Infor OS | 统一数据模型，ION 事件驱动计划刷新 |
| Infor Birst | 计划 KPI 仪表板，预测准确率分析 |

---

## 第三方资源速查

### 顾问与实施公司

| 公司 | 地区 | 说明 |
|------|------|------|
| [PCG Services](../resources/consultants.md) | 北美 | 2025 Infor 年度制造合作伙伴，Supply Planning 与 LN 集成实施 |
| [NexGen Technologies](../resources/consultants.md) | 北美 | Infor 年度合作伙伴，SCM/S&OP 实施 |
| [Columbus Global](../resources/consultants.md) | 欧洲/全球 | M3 实施专家，含 S&OP 计划咨询 |
| [mashfrog Group](../resources/consultants.md) | 欧洲 | M3、WMS、SCM 全栈实施 |
| [Sama Consulting](../resources/consultants.md) | 北美 | Infor 全产品线架构优化，含计划模块 |

### 博客与教程

| 资源 | 说明 |
|------|------|
| [Infor Supply Chain Planning 官方文档](https://docs.infor.com/) | Infor 官方文档门户（需登录 Infor Xtreme 支持门户）|
| [Infor Customer Community](../resources/forums.md) | Infor 官方用户社区 S&OP 讨论区 |

### 工具与插件

| 工具 | 说明 |
|------|------|
| [Infor Supply Planning](../resources/tools.md) | 需求计划、供应计划、库存优化套件 |
| [Infor ION](../resources/tools.md) | 计划系统与 ERP 之间的集成中间件 |
| [Infor Birst](../resources/tools.md) | 计划准确率分析仪表板 |

---

## 适用场景

**适合**：
- 多工厂/多仓库的制造企业，需要统一的 S&OP 流程
- 需求波动大（季节性、促销驱动），需要精准预测的行业（时尚、消费品）
- 库存成本高，需要科学设定安全库存和库存目标的企业
- 已使用 Infor LN/M3，希望计划与执行一体化的企业

**不适合**：
- 需求稳定、产品单一的小型制造企业（→ 使用 ERP 内置 MRP 即可）
- 已深度使用第三方 APS（如 Oracel Demantra、SAP APO）且无替换计划的企业

---

## 相关产品

- [Infor LN](ln.md) — 离散制造 ERP，Supply Planning 的主要集成目标
- [Infor M3](m3.md) — 流程制造 ERP，含捕获式计划（Capture Planning）
- [Infor WMS](wms.md) — 仓库执行层，计划与执行的闭环
- [Infor Nexus](nexus.md) — 供应链协同网络，供应商交付承诺
- [Infor Birst](birst.md) — 计划 KPI 分析与预测准确率监控

---

**最后更新**：2026-05-10
