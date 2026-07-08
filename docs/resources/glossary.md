---
title: "Infor 术语表 / Glossary - Infor 生态开放资源导航站"
description: "Infor 生态术语表，收录 Infor 产品名称、技术概念、平台组件和行业术语的中英文释义，帮助用户快速理解 Infor 生态系统。"
---

# Infor 术语表 / Glossary

> 本术语表收录 Infor 生态中的专有术语、产品名称、技术概念和行业术语，帮助用户快速理解 Infor 生态系统。
>
> **使用说明**：按英文字母排序，中文术语附在英文条目下方。可通过页面搜索（Ctrl+F）快速查找。

---

## A

| 术语 | 全称 | 释义 |
|------|------|------|
| **APS** | Advanced Planning and Scheduling | 高级计划与排程。利用算法优化生产计划和调度，平衡产能、物料和交期约束。 |
| **AWS** | Amazon Web Services | Amazon 云计算平台。Infor 的主要云基础设施合作伙伴，CloudSuite 产品部署于 AWS 上。 |
| **Baan** | — | 荷兰 ERP 软件公司，2003 年被 Infor 收购。Baan IV/Baan 5c/Baan LN 是 Infor LN 的前身。 |
| **BOD** | Business Object Document | 业务对象文档。Infor ION 集成框架中的标准数据交换格式，基于 OAGIS 标准，用于系统间传递业务数据（如订单、发票、库存等）。 |
| **Birst** | — | Infor 旗下的云 BI（商业智能）平台，支持自助式数据分析、仪表盘和报表，2010 年被 Infor 收购。 |
| **BWC** | Baan Webtop Components | Baan Webtop 组件。LN 早期的 Web UI 框架，提供基于浏览器的用户界面，已被 Infor Ming.le 替代。 |
| **CPQ** | Configure, Price, Quote | 配置、定价、报价。帮助销售团队根据客户需求配置产品方案、自动计算价格并生成报价单的软件。 |

## C

| 术语 | 全称 | 释义 |
|------|------|------|
| **CloudSuite** | — | Infor 的云端 ERP 产品系列总称。基于 AWS 部署，采用多租户架构，包含 CloudSuite LN、CloudSuite M3、CloudSuite Industrial 等。 |
| **CloudSuite Enterprise** | — | Infor 面向大型企业的综合 ERP 云套件，基于 Infor OS 平台，统一了 LN、M3 等核心产品。 |
| **Infor AI（原 Coleman AI）** | — | Infor 的企业级 AI 平台（名称源自 Coleman AI，2026 年起演进为 Infor AI / Industry AI Agents），内嵌于 Infor OS，提供预测分析、智能自动化、自然语言处理等能力。 |
| **CTO** | Configure to Order | 按订单配置。制造模式之一，根据客户订单从预定义的选项中配置最终产品，区别于 MTO（按订单生产）和 MTS（按库存生产）。 |

## D

| 术语 | 全称 | 释义 |
|------|------|------|
| **DAL** | Data Access Layer | 数据访问层。LN 的核心数据操作框架，封装了对数据库表的操作，自动触发数据校验和业务规则。分为 DAL1（旧版）和 DAL2（扩展版，推荐）。 |
| **DAL1** | Data Access Layer (Legacy) | 旧版 DAL。使用 `dal.new()` / `dal.update()` / `dal.delete()` 等函数，不支持字段依赖和完整的 Hook 触发。 |
| **DAL2** | Extended Data Access Layer | 扩展版 DAL（推荐）。使用 `dal.new.object()` / `dal.change.object()` / `dal.set.field()` / `dal.save.object()` 等函数，支持字段依赖、完整 Hook 链和 4GL 引擎自动交互。 |

## E

| 术语 | 全称 | 释义 |
|------|------|------|
| **EAM** | Enterprise Asset Management | 企业资产管理。管理设备的全生命周期（采购、维护、巡检、报废），在制造业、公共事业等行业广泛使用。Infor EAM 已出售给 Hexagon，现为 HxGN EAM。 |
| **EDI** | Electronic Data Interchange | 电子数据交换。企业间标准化的业务文档交换方式（如 ANSI X12、EDIFACT），常用于订单、发货通知、发票等场景。 |
| **ERP** | Enterprise Resource Planning | 企业资源计划。整合企业核心业务流程（财务、采购、销售、生产、库存等）的管理软件系统。 |

## F

| 术语 | 全称 | 释义 |
|------|------|------|
| **FSM** | Field Service Management | 现场服务管理。管理现场服务人员的派工、排程、工单、知识库和客户反馈，常用于设备维修、安装等场景。 |

## G

| 术语 | 全称 | 释义 |
|------|------|------|
| **GTMS** | Global Trade Management System | 全球贸易管理系统。Infor 的国际贸易合规解决方案，管理海关报关、进出口合规、关税计算等。 |

## H

| 术语 | 全称 | 释义 |
|------|------|------|
| **HCM** | Human Capital Management | 人力资本管理。管理员工招聘、薪酬、绩效、培训、时间考勤等全生命周期。Infor HCM 已出售给 KKR，现为 PeopleStreme。 |
| **Hook** | — | 钩子。DAL 中的预定义回调函数，在特定操作（新建/修改/删除/保存等）发生时自动触发，用于实现数据校验和业务规则。 |

## I

| 术语 | 全称 | 释义 |
|------|------|------|
| **IDM** | Infor Document Management | Infor 文档管理系统。在 Infor OS 中管理业务文档（采购订单、发票、合同等），支持版本控制、OCR、审批流程。 |
| **ION** | Infor Open Network | Infor 开放网络。Infor 的企业集成平台，基于消息总线和 BOD 标准，实现 LN/M3/WMS 等产品之间以及与外部系统的数据交换。 |
| **Infor OS** | Infor Operating System | Infor 操作系统。Infor 的统一云平台（原 Ming.le），提供单点登录、导航、文档管理、BI、工作流、AI 等基础设施服务。 |

## J

| 术语 | 全称 | 释义 |
|------|------|------|
| **JIT** | Just In Time | 准时制生产。精益生产方式，按需生产、按需送货，最大限度减少库存浪费。 |

## K

| 术语 | 全称 | 释义 |
|------|------|------|
| **KPI** | Key Performance Indicator | 关键绩效指标。衡量业务目标达成情况的核心指标。 |

## L

| 术语 | 全称 | 释义 |
|------|------|------|
| **LN** | — | Infor LN（Logistics & Manufacturing Network），Infor 的旗舰 ERP 产品，面向大型离散制造企业，源自 Baan ERP。支持多站点、多币种、多语言。 |
| **Lawson** | — | 美国 ERP 软件公司，2011 年被 Infor 收购。其产品 Lawson M3（现为 Infor M3）和 Lawson S3（现已融入 Infor HCM）至今仍是 Infor 产品线的重要组成部分。 |

## M

| 术语 | 全称 | 释义 |
|------|------|------|
| **MES** | Manufacturing Execution System | 制造执行系统。连接计划层（ERP）和控制层（PLC/SCADA），管理车间生产的实时执行。Infor 的 MES 产品为 Factory Track。 |
| **Ming.le** | — | Infor 早期社交化企业协作平台，后演变为 Infor OS。提供社交化工作流、文件共享和业务上下文信息。 |
| **MPS** | Master Production Schedule | 主生产计划。根据销售订单和预测，确定最终产品的生产计划。 |
| **MRP** | Material Requirements Planning | 物料需求计划。根据 BOM 和主生产计划，计算需要采购和生产的物料数量及时间。 |
| **MRP II** | Manufacturing Resource Planning | 制造资源计划。MRP 的扩展版本，涵盖整个制造过程，包括产能计划、车间控制和财务集成。 |
| **MTO** | Make to Order | 按订单生产。收到客户订单后才开始生产，适用于定制化程度高的产品。 |
| **MTS** | Make to Stock | 按库存生产。根据需求预测提前生产并存入仓库，适用于标准化产品。 |

## N

| 术语 | 全称 | 释义 |
|------|------|------|
| **Nexus** | Infor Nexus | Infor 的供应链协同平台（原 GT Nexus），提供供应链可视化、物流管理、贸易合规和供应商协同。2015 年被 Infor 收购。 |

## O

| 术语 | 全称 | 释义 |
|------|------|------|
| **OAGIS** | Open Applications Group Integration Specification | 开放应用集团集成规范。定义业务文档（BOD）的标准 XML Schema，是 Infor ION 数据交换的基础标准。当前版本为 v2.15.x。 |
| **OS** | — | 参见 [Infor OS](#i)。 |

## P

| 术语 | 全称 | 释义 |
|------|------|------|
| **PI** | Public Interfaces | 公共接口。LN 提供的标准业务功能方法，可在 Extension 中调用实现标准功能复用，升级不受影响。如 `Common.ConvertAmount()`、`Sales.CalculatePlannedDeliveryDate()` 等。 |
| **PLM** | Product Lifecycle Management | 产品生命周期管理。管理产品从概念设计、研发、量产到退市的全过程。 |
| **Process Extension** | — | 流程扩展。LN 的业务扩展机制，由系统在指定扩展点自动调用（如"Before Sales Order Approve"），与需主动调用的 Public Interfaces 不同。 |

## R

| 术语 | 全称 | 释义 |
|------|------|------|
| **RPA** | Robotic Process Automation | 机器人流程自动化。通过软件机器人自动执行重复性业务流程。Infor RPA 已转型为 Infor Intelligent Automation。 |
| **RTF** | Rich Text Format | 富文本格式。Infor 报表中常用的文本格式。 |

## S

| 术语 | 全称 | 释义 |
|------|------|------|
| **SCP** | Supply Chain Planning | 供应链计划。Infor 的供应链计划解决方案，覆盖需求预测、库存优化、生产排程和物流计划。 |
| **Smart Office** | — | Infor M3 的桌面客户端，基于 Jython/Java 脚本进行 UI 定制和自动化。M3 用户的主要工作界面。 |
| **SSRS** | SQL Server Reporting Services | SQL Server 报表服务。LN 常用的报表开发工具，支持复杂报表设计。 |
| **STP** | Service Tier Platform | 服务层平台。LN 的服务层，处理 DAL 与 UI 之间的交互。 |
| **SubDAL** | Sub Data Access Layer | 子数据访问层。嵌套在其他 DAL 中的 DAL，用于处理子表数据。 |
| **SyteLine** | — | 原 AIS（Applied Systems Intelligence）公司的 ERP 产品，面向中小离散制造企业。后被 Infor 收购，现为 CloudSuite Industrial (CSI)。 |

## T

| 术语 | 全称 | 释义 |
|------|------|------|
| **UI** | User Interface | 用户界面。LN 支持多种 UI：BWC（Web）、Ming.le（HTML5）、Infor OS（现代 Web）。 |
| **UE** | User Exit | 用户退出。LN 早期的定制化机制，在标准程序预留的扩展点插入自定义代码。功能有限，已被 Extension 机制取代。 |
| **UTP** | Unit Testing Platform | 单元测试平台。LN 的单元测试框架，用于对 DAL 和 4GL 函数进行自动化测试。 |

## V

| 术语 | 全称 | 释义 |
|------|------|------|
| **VMI** | Vendor Managed Inventory | 供应商管理库存。供应商根据协议管理客户的库存水平和补货。 |

## W

| 术语 | 全称 | 释义 |
|------|------|------|
| **WMS** | Warehouse Management System | 仓储管理系统。管理仓库的入库、出库、拣选、盘点、波次管理等操作。Infor WMS 在 Gartner 魔力象限中处于领导者地位。 |
| **Worfklow** | — | 工作流。Infor OS 中的业务流程自动化引擎，支持审批流、通知和任务分配。 |

## X

| 术语 | 全称 | 释义 |
|------|------|------|
| **XTendM3** | — | 基于 Java 的 M3 开源开发框架，提供 M3 API 调用、数据访问和扩展开发能力，活跃于 GitHub 社区。 |

---

## 常见缩写对照表

| 缩写 | 含义 | 所属领域 |
|------|------|----------|
| DAL | Data Access Layer | LN 开发 |
| BOD | Business Object Document | ION 集成 |
| PI | Public Interfaces | LN 开发 |
| UE | User Exit | LN 开发 |
| STP | Service Tier Platform | LN 架构 |
| FSM | Field Service Management | 产品线 |
| SCP | Supply Chain Planning | 产品线 |
| GTMS | Global Trade Management System | 产品线 |
| MPS | Master Production Schedule | 生产管理 |
| MRP | Material Requirements Planning | 生产管理 |
| APS | Advanced Planning and Scheduling | 生产管理 |
| MES | Manufacturing Execution System | 制造执行 |
| PLM | Product Lifecycle Management | 产品管理 |
| EDI | Electronic Data Interchange | 数据交换 |
| VMI | Vendor Managed Inventory | 库存管理 |
| CTO | Configure to Order | 制造模式 |
| MTO | Make to Order | 制造模式 |
| MTS | Make to Stock | 制造模式 |
| JIT | Just In Time | 生产方式 |
| KPI | Key Performance Indicator | 绩效管理 |
| SSRS | SQL Server Reporting Services | 报表工具 |
| RPA | Robotic Process Automation | 流程自动化 |

---

## 相关资源

- **Infor 产品术语详情**：参见 [按产品浏览](../by-product/ln.md)
- **LN 开发技术术语**：参见 [LN 4GL 开发技巧](ln-4gl-tips.md)
- **Infor ION BOD 术语**：参见 [官方文档导航](official-docs.md)

---

*最后更新：2026-05-08*

> 💡 如有术语遗漏或释义需要补充/修正，欢迎通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new) 反馈！
