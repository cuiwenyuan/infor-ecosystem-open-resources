---
title: "Infor d/EPM - Infor 生态开放资源导航站"
description: "Infor d/EPM 企业绩效管理资源导航，收录预算编制、财务合并、报表分析相关资源和实施顾问。"
---

# Infor d/EPM

> Infor d/EPM（企业绩效管理）是 Infor 的财务规划、预算编制、合并报表和财务分析平台，与 Infor LN、M3 等 ERP 深度集成，提供基于场景的预算建模和多维度财务分析。

---

## 产品概述

| 项目 | 说明 |
|------|------|
| **产品类型** | 企业绩效管理（EPM / CPM） |
| **前身** | Infor d/EPM（原 Infor EPM） |
| **部署方式** | 云部署（Infor Industry Cloud） |
| **目标客户** | 中大型企业，多实体/多币种/多会计准则集团 |
| **核心目标** | 预算编制、财务合并、管理报表、滚动预测 |

---

## 核心功能

### 预算编制（Budgeting）

- **多版本预算建模**：支持按部门、产品、地区、项目等多维度编制
- **滚动预测（Rolling Forecast）**：基于实际数据动态调整预测
- **假设场景建模（What-if）**：多方案对比，支持驱动因子建模
- **审批工作流**：预算编制 → 部门审核 → 财务审核 → 批准发布
- **与 ERP 集成**：实际 vs 预算差异分析，数据自动拉取

### 财务合并（Financial Consolidation）

- **多实体合并**：自动抵消分录（IC Eliminations）、股权抵消
- **多币种折算**：期末汇率、平均汇率、历史汇率灵活配置
- **会计准则转换**：IFRS / US GAAP / 中国会计准则 并行处理
- **合并调整分录**：合并层面调整，不影响单体账
- **合并报表输出**：资产负债表、利润表、现金流量表自动生成

### 管理报表与分析

- **管理报表（Management Reporting）**：利润中心 P&L、EBITDA 分析
- **KPI 仪表板**：ROE、ROA、毛利率、营运资本周转率等
- **责任中心会计**：成本中心、利润中心、投资中心绩效评估
- **Birst 集成**：将 d/EPM 数据推送到 Birst 做可视化分析

### 合规与审计追踪

- **审计轨迹（Audit Trail）**：所有预算/实际调整全程可追溯
- **SOX 合规支持**：访问控制、审批留痕、数据不可篡改
- **版本控制**：预算编制各版本完整保留，支持回溯对比

---

## 与 Infor 生态集成

| Infor 产品 | 集成方式 |
|-------------|----------|
| [Infor LN](ln.md) | GL/AP/AR 实际数据自动拉取，预算 vs 实际差异分析 |
| [Infor M3](m3.md) | 多实体合并，支持 M3 多公司架构 |
| [Infor SunSystems](sunsystems.md) | 多公司财务合并，SunAccounts 数据集成 |
| [Infor Birst](birst.md) | EPM 数据推送到 Birst，可视化仪表板 |
| Infor OS | 统一身份认证，跨产品工作流 |

---

## 第三方资源速查

### 顾问与实施公司

| 公司 | 地区 | 说明 |
|------|------|------|
| [Sama Consulting](../resources/consultants.md) | 北美 | Infor 全产品线（含 d/EPM）架构优化与财务合并实施 |
| [PCG Services](../resources/consultants.md) | 北美 | 2025 Infor 年度制造合作伙伴，d/EPM 与 LN 集成实施 |
| [NexGen Technologies](../resources/consultants.md) | 北美 | Infor 年度合作伙伴，d/EPM 预算编制实施 |
| [Godlan](../resources/consultants.md) | 北美 | CloudSuite 财务模块 + d/EPM 实施 |

### 博客与教程

| 资源 | 说明 |
|------|------|
| [Infor d/EPM 官方文档](https://docs.infor.com/) | Infor 官方文档门户（需登录 Infor Xtreme 支持门户）|
| [Infor Customer Community](../resources/forums.md) | 官方用户社区 d/EPM 讨论区 |

### 工具与插件

| 工具 | 说明 |
|------|------|
| [Infor d/EPM](../resources/tools.md) | 企业绩效管理平台，预算/合并/报表 |
| [Infor Birst](../resources/tools.md) | EPM 数据可视化分析 |

---

## 适用场景

**适合**：
- 多实体/多币种/跨国运营集团，需要统一预算和合并报表
- 已使用 Infor LN/M3，希望预算与实际一体化
- 需要滚动预测和多版本场景模拟的企业
- SOX 合规要求高的上市企业

**不适合**：
- 单实体中小企业（→ 使用 ERP 内置预算功能即可）
- 已深度使用 Hyperion / OneStream 且无替换计划的企业

---

## 相关产品

- [Infor Birst](birst.md) — EPM 数据可视化分析平台
- [Infor LN](ln.md) — 离散制造 ERP，d/EPM 主要数据来源
- [Infor M3](m3.md) — 流程制造 ERP，多实体合并场景
- [Infor SunSystems](sunsystems.md) — 多实体财务管理，与 d/EPM 互补

---

**最后更新**：2026-05-10
