---
description: Infor 常见问题解答：Infor 是什么、LN 与 Baan 的关系、LN 全称、能否本地部署、M3 什么语言写的、适合谁用等高频问题
---

# Infor 常见问题（FAQ）

> 本页汇总搜索引擎中围绕 Infor 及其产品最常见的提问，给出简明答案，并链接到站内深度页面。

## 关于 Infor 公司

### Infor 是什么公司？
Infor 是全球领先的**行业云应用软件**厂商，为制造、分销、酒店、时尚、医疗、公共事业等行业提供行业专属的 ERP 与边缘应用，所有产品运行在 Infor 云平台（多租户，AWS 基础设施）之上，全球客户约 6 万+。**Infor 是 Koch Industries 的独立子公司**（2017 年 Koch 投资，2020 年完成全资收购），总部在美国佐治亚州亚特兰大，为私人持股公司。

### Infor 与 SAP、Oracle 有什么区别？
一句话：**Infor 卖"行业专属"，SAP/Oracle 卖"通用平台"**。Infor 的每个 CloudSuite 都为特定行业深度预配置（60+ 微垂直），强调开箱即用的行业逻辑；SAP/Oracle 生态更大、跨行业覆盖更广，但行业深度常靠附加模块实现。站内对比详见 [LN vs SAP](../competitor/ln-vs-sap.md)、[M3 vs SAP](../competitor/m3-vs-sap.md)、[LN vs Oracle](../competitor/ln-vs-oracle.md)。

## 关于 Infor LN

### Infor LN 和 Baan 是同一个东西吗？
**是同一产品线的延续**。沿革：Baan IV / Baan V →（SSA Global 收购后）SSA ERP LN →（Infor 2006 年收购后）Infor ERP LN → 今天的 Infor LN 10.x / CloudSuite 版。会话命名（如 `tdsls4101m000`）、数据模型与大量平台概念直接承袭自 Baan，这也是老 Baan 顾问的知识仍然值钱的原因。从业者日常仍把两个名字混用。

### Infor LN 的全称是什么？
LN 是**产品名而非缩写**，没有官方的"LN = 某某"展开。人们通常写 **Infor ERP LN**（Infor Enterprise Resource Planning LN）。历史上见过的写法还有 ERP LN、ERPLN、LN ERP、SSA ERP LN。

### Infor LN 适合什么样的企业？
**复杂离散制造**：多工厂 / 多法人 / 多币种、ETO（按订单设计）/ MTO / CTO 生产模式、项目型制造、强追溯合规行业（航空航天与国防、汽车、高科电子、工业装备）。单工厂、简单备货型生产的企业用 CloudSuite Industrial（SyteLine）通常更快更省。详见 [LN 产品页](../by-product/ln.md)。

### Infor LN 和 CloudSuite Industrial（SyteLine）怎么选？
LN 面向**企业级复杂度**（多站点、多立法实体、跨国法规），CSI/SyteLine 面向**中型离散制造**（更快上线、更低 TCO）。详细对比见 [LN vs CSI](../competitor/ln-vs-csi.md)。

## 关于 Infor M3

### Infor M3 是什么语言写的？
**Java**。这也是 M3 历史上能跨多种操作系统与硬件平台运行的原因之一；现版本以 AWS 上的多租户云形态交付。

### Infor M3 和 CloudSuite Food & Beverage 什么关系？
CloudSuite Food & Beverage 是**构建在 M3 之上的行业垂直层**，增加了保质期管理（FEFO/FIFO）、配方与配方管理、营养标签与食品安全合规（BRC、IFS Food、FSSC 22000）等食品饮料专属能力。

## 关于部署与支持

### 还能在本地（On-Premise）运行 Infor 吗？
**可以**。存量的 M3、LN、SyteLine 本地部署仍在支持期内，官方未给出停止支持日期。但要注意：**新功能与 AI 能力云优先甚至云专属**，本地部署在功能上会逐渐落后；新客户销售也以多租户云为主。

### Infor CloudSuite 跑在哪家云上？
**AWS**。Infor CloudSuite 是构建在 AWS 之上的多租户 SaaS，季度级持续更新。见 [Infor OS](../by-product/infor-os.md)。

### 忘记密码 / 无法登录 Infor 怎么办？
Infor 没有统一的公开登录入口——**每个客户租户有各自的 URL**（通常是 Infor OS Portal / Ming.le）。请找贵司 IT 获取正确的租户地址；SSO 环境下密码重置走贵司自己的账号体系。详见[登录指南](infor-login-guide.md)。

## 关于价格与实施

### Infor 多少钱？
Infor 不公布价目表，全部定制报价。第三方 2026 年估算：订阅约 **$150–400/用户/月**（按角色分层），中型实施 **$200K–$600K**，100 用户三年 TCO 约 **$92 万–$240 万**。详见[定价与 TCO 指南](infor-pricing-tco.md)。

### 实施 Infor 要多久？
第三方口径：CSI 约 14–18 个月，M3 约 18–24 个月，LN 约 20–24 个月；单站点中型项目可显著缩短。分期上线是控制周期与风险的常见做法。

## 学习与职业

### 怎么学习 Infor LN / 怎么成为 Infor 顾问？
站内已成体系：[LN 4GL 技巧](ln-4gl-tips.md)、[LN DAL 指南](ln-dal-guide.md)、[LN 开发手册](ln-dev-cookbook.md)、[认证考试指南](certification-guide.md)、[如何成为 Infor LN 顾问](infor-consultant-career.md)。

### Infor 相关岗位薪资如何？
中国高级 LN 实施顾问招聘口径约 **15–25K/月**（2026 杭州示例），美国高级功能顾问年薪约 **$110K–$153K**，伙伴顾问费率 $150–300/小时。详见[顾问职业路径页](infor-consultant-career.md)。

## 更多问题

- **术语**：先查[术语表](glossary.md)
- **报错**：[LN / M3 / ION / WMS 错误码](../troubleshooting/index.md)
- **版本动态**：[版本发布追踪](release-notes.md) · [行业动态](news.md)

---

**最后更新**：2026-11-04
**维护者**：崔文远 Troy Cui
