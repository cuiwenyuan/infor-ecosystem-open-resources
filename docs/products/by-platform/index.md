---
title: "按技术平台分类 - Infor 生态开放资源导航站"
description: "按技术平台分类浏览 Infor 产品与资源，涵盖 Infor OS、ION、Birst、Coleman AI、AWS/Azure 云基础设施等。"
---

# 按技术平台分类

> 从技术架构角度梳理 Infor 生态系统的各层技术平台、开发框架和基础设施组件，帮助开发者和技术决策者理解技术栈全貌。
>
> **适用场景**：技术评估、架构设计、二次开发、系统集成、云迁移规划等技术相关工作。

---

## Infor OS（Operating Service）

Infor OS 是 Infor 所有云产品的统一云原生基础设施平台。

| 项目 | 详情 |
|------|------|
| **定位** | Infor 云原生操作系统 / 应用平台 |
| **基础设施** | **AWS 独家**（Infor 与 AWS 战略合作） |
| **核心能力** | 统一的用户体验(UX)、身份与访问管理(IAM)、应用生命周期管理、集成中枢、数据湖、AI 服务 |

### 关键组件

| 组件 | 说明 |
|------|------|
| **Infor OS Portal** | 统一入口，替代旧版 Ming.le，支持单点登录(SSO)和个性化仪表板 |
| **Identity & Access Management** | 统一身份认证，支持 LDAP/SAML/OAuth |
| **Document Management** | 全局文档服务，跨产品文档存储与搜索 |
| **Data Lake** | 集中式数据湖，汇聚来自各 Infor 应用的数据 |
| **AI Services** | 内置 Coleman AI 服务，可被所有上层应用调用 |
| **Workflow Engine** | 跨应用的统一工作流引擎 |

**相关资源**：
- [Infor OS 产品页](../../by-product/infor-os.md)
- [OS/ION 专长顾问](../../resources/consultants.md) — mashfrog, Sama Consulting

---

## Infor ION — 事件驱动集成平台

Infor ION 是连接 Infor 各产品以及外部系统的核心集成中间件。

### 架构概览

| 组件 | 说明 |
|------|------|
| **ION Gateway / API Gateway** | API 管理、策略控制、代理端点、安全防护 |
| **ION Connect** | 文档流(Document Flow)设计和管理工具 |
| **ION Workflow** | 业务流程编排引擎，支持人工审批节点 |
| **ION Data Lake** | 数据湖服务，ETL 数据整合 |
| **BOD (Business Object Document)** | 标准化的业务事件消息格式，是 ION 集成的核心概念 |

### BOD（Business Object Document）体系

BOD 是 ION 集成的核心通信协议，定义了标准的业务事件格式：

- **通用 BOD**：Sync/Promise/Confirm/Process/CANCEL/GET 等操作类型
- **业务对象**：SalesOrder、PurchaseOrder、Inventory、Invoice、GeneralLedger 等
- **发布/订阅模式**：应用通过发布(publishing)和订阅(subscribing) BOD 进行松耦合集成
- **文档流(Document Flow)**：可视化编排 BOD 的流转逻辑和转换规则

**相关资源**：
- [ION BOD 处理工具](../../resources/tools.md) — BOD 消息处理指南
- [ION 开发指南](../../resources/tools.md) — ION Development Guide
- [ION API SDK](../../resources/tools.md) — Java SDK 用于集成开发

---

## Infor AI（Coleman）

| 项目 | 详情 |
|------|------|
| **原名** | Coleman AI Platform |
| **现名** | Infor AI |
| **定位** | 嵌入 Infor OS 的企业 AI 平台 |

### 核心能力

| 能力 | 说明 |
|------|------|
| **对话式 AI (Conversational AI)** | 自然语言查询 Infor 数据，类似"上季度销售额是多少" |
| **预测性分析 (Predictive Analytics)** | 构建机器学习模型进行销量预测、需求预测、流失预警 |
| **流程自动化 (Process Automation)** | AI 驱动的自动化工作流，减少手动干预 |
| **行业预置模型** | 针对各行业的预训练模型（如制造质量预测、零售需求预测） |

**相关资源**：
- [AI 工具与指南](../../resources/tools.md) — Coleman AI User Guide、数据表

---

## Infor Birst — 云端商务智能

| 项目 | 详情 |
|------|------|
| **定位** | 基于 SaaS 的现代 BI 和网络化分析(Networked Analytics)平台 |
| **核心技术** | 内存计算、自动数据建模、语义层、可视化仪表板 |

### 关键特性

| 特性 | 说明 |
|------|------|
| **网络化 BI** | 跨组织的分析内容共享和复用，打破数据孤岛 |
| **嵌入式分析** | 将 Birst 仪表板嵌入 Infor ERP 界面中 |
| **自动数据精炼** | 自动化 ETL，减少手工数据准备 |
| **多租户** | 支持大规模企业部署 |

**相关资源**：[BI/AI 工具](../../resources/tools.md)

---

## AWS 基础设施 (AWS Infrastructure)

Infor 与 AWS 建立了独家战略合作，所有 Infor 云产品均运行在 AWS 上。

| 方面 | 说明 |
|------|------|
| **云平台** | AWS（独家），不支持 Azure/GCP 作为 Infor Cloud 主平台 |
| **部署区域** | 全球多区域部署，满足数据驻留要求 |
| **托管服务** | Infor 提供 Managed Services（IMS），客户无需直接管理 AWS 资源 |
| **混合部署** | 支持本地部署 + 云端扩展的混合模式 |
| **关键技术** | EC2、RDS、S3、Lambda、API Gateway 等 |

---

## Infor Marketplace

| 项目 | 详情 |
|------|------|
| **规模** | **150+** 应用程序和解决方案 |
| **定位** | Infor 官方应用市场，连接 Infor 生态中的 ISV 和开发者社区 |
| **内容** | 行业加速器、垂直解决方案、连接器(Connectors)、扩展应用 |

---

## 开发框架 (Development Frameworks)

Infor 为不同产品线提供了各自的开发和定制框架。

### XtendM3 — Infor M3 扩展框架

| 项目 | 详情 |
|------|------|
| **语言** | Groovy (JVM) |
| **用途** | 在不修改标准代码的前提下实时修改 M3 业务逻辑 |
| **特点** | 热加载(Hot Reload)、AOP 编程模型、事件驱动 |
| **开源** | 是，GitHub: [infor-cloud/xtendm3](https://github.com/infor-cloud/xtendm3) |

**相关资源**：[XtendM3 工具](../../resources/tools.md)

### LN Studio / DevTools — Infor LN 开发工具链

| 工具 | 说明 |
|------|------|
| **LN Studio** | 官方 IDE，支持安装配置、基于活动的开发、调试、4GL 脚本编辑 |
| **LN DevTools (VS Code)** | VS Code 扩展，浏览和管理 LN 构件（表、Session、脚本、DAL 等） |
| **LN 4GL** | LN 的专用编程语言（基于 Baan Tools） |
| **DAL (Data Access Layer)** | LN 数据访问层，标准化数据读写接口 |
| **PMC** | 功能包(Product Package)管理工具，管理软件更新 |

**相关资源**：[LN 开发工具](../../resources/tools.md)

### M3 H5 SDK — Infor M3 Web 开发

| 项目 | 详情 |
|------|------|
| **技术栈** | HTML5 / JavaScript / CSS3 |
| **用途** | 构建 M3 的自定义 Web 扩展页面和 Widget |
| **开源** | 是，GitHub: [infor-cloud/m3-h5-sdk](https://github.com/infor-cloud/m3-h5-sdk) |

**相关资源**：[M3 H5 SDK](../../resources/tools.md)

### ION API SDK — 集成开发

| 项目 | 详情 |
|------|------|
| **语言** | Java |
| **用途** | 通过编程方式调用 ION API Gateway，构建集成应用 |
| **开源** | 是，GitHub: [infor-cloud/ion-api-sdk](https://github.com/infor-cloud/ion-api-sdk) |

**相关资源**：[ION 开发工具](../../resources/tools.md)

### Landmark Technology — HCM / FSM 底层平台

| 项目 | 详情 |
|------|------|
| **应用产品** | Infor HCM (Lawson), Infor FSM (S3) |
| **编程语言** | Landmark 4GL (专有语言) |
| **特点** | 表单驱动开发、屏幕 painter、事务处理引擎 |
| **学习曲线** | 相对陡峭，但社区有丰富的经验和最佳实践 |

**相关资源**：
- [HCM/Lawson 专长顾问](../../resources/consultants.md) — Blue Eagle Consulting, RPI Consultants（深耕 Landmark 多年）

---

## 开源组件 (Open Source Components)

Infor 技术栈广泛采用了成熟的开源技术和标准。

| 层面 | 技术 |
|------|------|
| **操作系统** | Linux（服务器端） |
| **后端语言** | Java (JEE)、Groovy (XtendM3)、C/C++ (LN Core) |
| **前端技术** | HTML5、CSS3、JavaScript、TypeScript |
| **数据库** | PostgreSQL、Oracle、SQL Server、MongoDB |
| **中间件** | JBoss/WildFly、Apache Tomcat |
| **集成协议** | REST API、SOAP、XML/JSON、EDIFACT/X12 (EDI) |
| **容器化** | Docker、Kubernetes（Infor OS 云原生部署） |

### Infor GitHub 开源项目

Infor 官方在 GitHub 上维护了大量开源项目：

| 仓库 | 说明 |
|------|------|
| **[infor-cloud](https://github.com/infor-cloud)** | Infor 官方组织，含 13+ 个公开项目 |
| **xtendm3** | M3 云扩展框架 (Groovy) |
| **m3-h5-sdk** | M3 HTML5 SDK (JavaScript) |
| **ion-api-sdk** | ION API Gateway SDK (Java) |
| **infor-eam-rest-api** | EAM REST API 示例 |

**相关资源**：[官方开源项目](../../resources/tools.md)

---

## 技术架构全景

```
┌─────────────────────────────────────────────┐
│              应用层 (Applications)            │
│   LN │ M3 │ CSI │ FSM │ HCM │ WMS │ EAM ...  │
├─────────────────────────────────────────────┤
│          Infor OS (Operating Service)        │
│  Portal │ IAM │ Document │ Workflow │ AI     │
├─────────────────────────────────────────────┤
│              Infor ION Layer                 │
│  API Gateway │ BOD │ Connect │ Data Lake     │
├─────────────────────────────────────────────┤
│         Analytics & Intelligence             │
│      Birst (BI) │ Infor AI (Coleman)         │
├─────────────────────────────────────────────┤
│           AWS Infrastructure                │
│    EC2 │ RDS │ S3 │ Lambda │ Networking      │
└─────────────────────────────────────────────┘
```

---

## 📎 其他分类视角

- **[按业务功能浏览 →](../by-function/index.md)** — 根据业务需求查找对应产品
- **[按产品线浏览 →](../by-product-line/index.md)** — 以 Infor 产品线为主线了解各产品
- **[按行业浏览 →](../by-industry/index.md)** — 根据您的行业定位推荐产品组合

---

**最后更新**：2026-05-08
