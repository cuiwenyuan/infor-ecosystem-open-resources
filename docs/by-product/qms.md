---
title: "Infor QMS - Infor 生态开放资源导航站"
description: "Infor QMS 质量管理系统资源导航，收录 QMS 相关的顾问公司、实施资源和合规管理指南。"
---

# Infor QMS

> Infor QMS（质量管理系统）提供完整的供应商质量管理、内部质量控制、审计管理和合规追踪能力，与 Infor LN、M3、EAM 等产品深度集成，支持 ISO 9001、FDA 21 CFR Part 11 等合规标准。

---

## 产品概述

| 项目 | 说明 |
|------|------|
| **产品类型** | 质量管理系统（QMS / QM） |
| **集成 ERP** | Infor LN、Infor M3、Infor EAM |
| **部署方式** | 云部署（Infor Industry Cloud） |
| **目标客户** | 需严格质量管控的制造企业（汽车、电子、医药、食品） |
| **核心标准** | ISO 9001、IATF 16949、FDA 21 CFR Part 11、ISO 13485 |

---

## 核心功能

### 供应商质量管理（SQM）

- **供应商审核（Supplier Audit）**：审核计划、 Checklist、审核报告、不符合项跟踪
- **来料检验（Incoming Inspection）**：基于 AQL 抽样计划的来料检验
- **供应商纠正措施（SCAR）**：供应商端不符合项的发起、跟踪与关闭
- **供应商评分卡**：质量、交期、服务等维度综合评分

### 内部质量控制

- **检验计划（Inspection Plan）**：按物料/工序配置检验项目和质量特性
- **质量控制（Quality Control）**：入库检验、在制品检验、成品检验
- **不合格品管理（Nonconformance / NCR）**：不合格品记录、处置决策（退货/返工/报废）、根本原因分析
- **纠正预防措施（CAPA）**：纠正措施、预防措施、效果验证、8D 报告

### 审计管理（Audit Management）

- **审计计划**：年度审计计划、审计日程管理
- **审计执行**：审计 Checklist、证据采集、审计发现（Findings）
- **审计跟踪**：审计结果跟踪、整改验证、审计报告生成
- **合规审计**：支持 ISO、IATF、FDA 等标准审计模板

### 统计过程控制（SPC）

- **控制图**：Xbar-R、Xbar-S、P 图、C 图、I-MR 图
- **过程能力分析**：Cp、Cpk、Pp、Ppk 计算与解读
- **实时报警**：过程异常自动触发报警和调查流程
- **SPC 报表**：过程能力趋势分析、审计准备报表

### 文档与培训管理

- **质量文档控制**：SOP、WI、检验标准等文档的版本控制和分发
- **培训记录管理**：员工资质、培训记录、证书到期提醒
- **电子签名**：符合 FDA 21 CFR Part 11 的电子签名审计轨迹

---

## 与 Infor 生态集成

| Infor 产品 | 集成方式 |
|-------------|----------|
| [Infor LN](ln.md) | 质量模块原生集成，检验结果回写采购收货/生产订单 |
| [Infor M3](m3.md) | 质量模块原生集成，批次检验、留样管理 |
| [Infor PLM](plm.md) | 设计变更 → 质量影响评估 → CAPA 发起 |
| [Infor EAM](eam.md) | 设备维护质量记录、校准管理 |
| Infor OS | 统一工作流，质量事件跨产品通知 |

---

## 第三方资源速查

### 顾问与实施公司

| 公司 | 地区 | 说明 |
|------|------|------|
| [Sama Consulting](../resources/consultants.md) | 北美 | Infor 全产品线（含 QMS）架构优化与集成 |
| [PCG Services](../resources/consultants.md) | 北美 | 2025 Infor 年度制造合作伙伴，QMS 与 LN 集成实施 |
| [NexGen Technologies](../resources/consultants.md) | 北美 | Infor 年度合作伙伴，质量管理模块实施 |
| [Godlan](../resources/consultants.md) | 北美 | CloudSuite 质量模块实施咨询 |

### 博客与教程

| 资源 | 说明 |
|------|------|
| [Infor QMS 官方文档](https://docs.infor.com/) | Infor 官方文档门户（需登录 Infor Xtreme 支持门户）|
| [Infor Customer Community](../resources/forums.md) | 官方用户社区 QMS 讨论区 |

### 工具与插件

| 工具 | 说明 |
|------|------|
| [Infor QMS](../resources/tools.md) | 质量管理系统，含 SPC/CAPA/审计管理 |
| [Infor LN Quality](../resources/tools.md) | LN 内置质量管理模块（轻量级 QMS） |
| [Infor M3 Quality](../resources/tools.md) | M3 内置质量管理模块（批次检验/留样） |

---

## 适用场景

**适合**：
- 汽车/电子行业（IATF 16949、ISO 9001 强制要求）使用 Infor LN/M3 的企业
- 医药/医疗器械行业（FDA 21 CFR Part 11、ISO 13485）需要电子签名和审计轨迹
- 需要 SPC 统计过程控制和 CAPA 管理的制造企业
- 供应商质量管理（SQM）需求强烈的品牌制造企业

**不适合**：
- 无强制质量合规需求的小型制造企业（→ 使用 ERP 内置检验功能即可）
- 已深度使用第三方 QMS（如 ETQ Reliance、MasterControl）且无替换计划的企业

---

## 相关产品

- [Infor PLM](plm.md) — 设计变更与质量影响评估联动
- [Infor EAM](eam.md) — 设备校准与维护质量管理
- [Infor LN](ln.md) — 离散制造 ERP，QMS 主要集成目标
- [Infor M3](m3.md) — 流程制造 ERP，批次检验与留样管理

---

**最后更新**：2026-05-10
