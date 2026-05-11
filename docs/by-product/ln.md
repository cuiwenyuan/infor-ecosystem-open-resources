---
title: "Infor LN - Infor 生态开放资源导航站"
description: "Infor LN 资源导航，收录 LN 相关的顾问公司、技术博客、开发工具和社区论坛。"
---

# Infor LN

> Infor LN 是面向大型企业复杂离散制造需求的旗舰 ERP 解决方案，源自 Baan ERP，支持多站点、多实体运营。

---

## 产品概述

| 项目 | 说明 |
|------|------|
| **产品类型** | ERP 系统 |
| **前身** | Baan IV / Baan 5c / SSA ERP LN 6.1 |
| **历史名称** | Baan IV → Baan V → SSA ERP LN 6.1 → Infor ERP LN 6.1 → Infor LN 10.x |
| **目标客户** | 大型企业（500-10,000+ 员工） |
| **核心行业** | 汽车、工业制造、电子、金属加工 |
| **部署方式** | 云部署（Infor OS/AWS）、本地部署 |

---

## 版本历史

| 年份 | 版本 | 说明 |
|------|------|------|
| 1978 | Baan 公司成立 | Jan Baan 在荷兰创立 |
| ~1980s | Triton 1.0 / 2.0 / 3.0 | Baan 早期版本代号 |
| ~1990s | Baan IV (4.0) | 经典版本，国内仍有大量用户 |
| ~1990s末 | Baan V (5.0 / 5.1 / 5.2) | 后续演进版本 |
| 1995 | Baan IPO 上市 | 年销售增长 91%，威胁 SAP 市场地位 |
| 1998前后 | 被 Invensys 收购 | 英国工业自动化集团 Invensys 收购 Baan |
| 2003 | SSA ERP LN 6.1 | Invensys 以 $135M 出售 Baan 事业部给 SSA Global，产品更名 |
| 2006 | Infor ERP LN 6.1 | Infor 收购 SSA Global，纳入 Infor 产品线 |
| ~2008-2010 | LN 6.1 FP6 / FP7 | Feature Pack 增量更新 |
| ~2013 | **Infor LN 10.3** | 版本号从 6.1 跳跃至 10.3（待核实具体年份） |
| 2016年2月 | **Infor LN 10.4** | Installation Guide 标注日期 2016-02-29 |
| 2016年6-8月 | **Infor LN 10.5** | 官方宣布 2016-06-30 全球发布 |
| 2018年4月 | **Infor LN 10.6** | 新增项目调度工具、IFRS 财务能力 |
| 2019年3月 | **Infor LN 10.7** | 官方博客标注 2019-03-08 发布 |
| 2021年 | **Infor LN 10.8** | 云原生架构转型（另有来源记载 2023-03 CloudSuite 版发布，可能为持续更新机制） |

> 版本号从 6.1 跳跃至 10.3 是 Infor 产品线的统一品牌策略，与 Infor OS、Infor ION 等产品的版本号对齐。

---

## 技术架构

### 三层架构

| 层级 | 说明 |
|------|------|
| **UI 层** | 用户界面驱动，终端用户操作入口 |
| **VM 层（Bshell）** | 服务端虚拟机层（Baan Shell），处理业务逻辑 |
| **Database 层** | 数据存储层，支持 SQL Server / Oracle 等 |

### 核心概念

| 概念 | 说明 |
|------|------|
| **Package**（2字母） | 功能模块分组，如 `tf`（财务）、`td`（分销）、`tp`（项目）、`cp`（计划）、`wh`（仓库） |
| **Module**（3字母） | Package 下子功能，如 `tfacp`（应付）、`tfgld`（总账）、`tdsls`（销售）、`tdpur`（采购） |
| **VRC** | Version-Release-Customer 版本控制框架，支持基础版/更新版/本地化/定制版四层结构 |

### 程序脚本类型

4GL / 4GL Event Sessions / DAL2 / DLL

---

## 核心功能

### 制造管理
- 多级 BOM（物料清单）管理
- 工艺路线和工作中心管理
- 工作订单管理
- 物料需求计划（MRP）
- 高级计划和调度（APS）
- 工程变更管理（ECM）
- 配置到订单（CTO）的产品配置器
- 外协加工（分包制造）

### 供应链管理
- 采购管理
- 库存管理
- 质量管理
- 序列号和批次跟踪

### 财务管理
- 总账（GL）、应付账款（AP）、应收账款（AR）
- 现金管理、固定资产

---

## 第三方资源速查

### 论坛与社区

| 资源 | 说明 |
|------|------|
| [LN ERP Customer Community](../resources/forums.md) | Infor 官方 LN 用户社区 |
| [LN NAUG (北美用户组)](../resources/forums.md) | 北美 LN 用户组，含知识库和年会 |
| [WIUG (荷兰用户组)](../resources/forums.md) | 荷兰 Infor 用户组（覆盖 LN、M3 等） |
| [r/Infor](../resources/forums.md) | Reddit 社区（英文讨论） |

### 顾问与实施公司

| 公司 | 地区 | 说明 |
|------|------|------|
| [Sama Consulting](../resources/consultants.md) | 北美 | LN 实施、架构优化、ION 集成 |
| [PCG Services](../resources/consultants.md) | 北美 | LN & CSI 实施与升级 |
| [NexGen Technologies](../resources/consultants.md) | 北美 | LN 实施与支持 |
| [Xencore Global](../resources/consultants.md) | 欧洲 | LN & M3 实施顾问 |
| [Tarento](../resources/consultants.md) | 亚太 | LN & M3 PLM & Factory Track |
| [Coserve Solutions](../resources/consultants.md) | 亚太 | LN & CloudSuite 实施 |
| [润数信息](../resources/consultants.md) | 中国 | LN、WMS、CPQ 实施 |
| [拓创数字](../resources/consultants.md) | 中国 | LN 实施与定制开发 |

### 博客与教程

| 资源 | 说明 |
|------|------|
| [Reinforce Tech Blog](../resources/blogs.md) | LN/LX/Baan 实施与运维实践 |
| [FullOnBaan LN Playbook](../resources/blogs.md) | LN/ION/Infor OS 知识库（4GL、DAL、BOD 等） |
| [FullOnBaan 视频课程](../resources/blogs.md) | LN 各模块视频培训（开发、管理、财务） |
| [Crossroads RMC](../resources/blogs.md) | LN 实用技巧与 ION 集成 |
| [SamA Consulting Blog](../resources/blogs.md) | LN 架构优化、ION、WMS、EAM、HCM 深度技术文章 |
| [CSDN LN 教程](../resources/blogs.md) | 中文 LN 学习笔记（腾讯云） |

### 工具与插件

| 工具 | 说明 |
|------|------|
| [LN DevTools (VS Code)](../resources/tools.md) | VS Code 扩展，浏览和管理 LN 构件 |
| [LN Studio](../resources/tools.md) | LN 官方应用开发工具 |
| [PMC](../resources/tools.md) | 产品维护和控制工具（功能包管理） |
| [LN Reporting (SSRS)](../resources/tools.md) | LN 报表开发工具 |
| [ION BOD 处理工具](../resources/tools.md) | ION BOD 消息处理指南 |

---

## 适用场景

**适合**：大型离散制造商（500+ 员工）、多站点多实体运营、复杂制造需求

**不适合**：小型企业（→ CloudSuite Industrial）、流程制造（→ Infor M3）

---

## 历史背景

Infor LN 的前身是荷兰 Baan 公司（1978年创立）开发的 Baan ERP，历经 Baan IV、Baan V 等版本。1998年 Baan 被英国 Invensys 收购，2003年 Invensys 将 Baan 事业部以 $135M 出售给 SSA Global，产品更名为 SSA ERP LN 6.1。2006年 Infor 收购 SSA Global，产品纳入 Infor 产品线并更名为 Infor ERP LN，后续演进为当前的 Infor LN 10.x 系列。国内用户习惯将 Infor LN 统称为"Baam"或"LN"。

---

## 相关产品

- [Infor M3](m3.md) — 流程制造版本
- [CloudSuite Industrial](csi.md) — 中端离散制造版本
- [Infor OS](infor-os.md) — 运行平台

---

**最后更新**：2026-05-11
