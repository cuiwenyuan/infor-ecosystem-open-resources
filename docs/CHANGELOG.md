# Changelog

本页面记录 Infor 生态开放资源导航站的重大更新。

## 2026-11-05
- **`resources/ln-sessions.md` v2 大升级**：Session 由 1,299 条扩至 **12,125 条**（23 包 / 208 模块组，约 9.3 倍）；合并 10.8 / 2024.x Cloud / 2025.x Cloud 官方 Sitemap 全量 + 10.7 zh-cn 联机帮助采集，中文描述 10,626 条
- 新增「文档版本」切换：10.6 / 10.7 / 10.8 / 2024.x Cloud / 2025.x Cloud 五个官方文档版本，按官方集合严格标注可用版本避免死链（10.5 库不全，仅给文档库入口）；按包分片 JSON 增至 23 个
- 考证补全 9 个新包元数据，FM 包名修正为 Freight Management（原误标 Food）
- 两篇待发公众号文章（LN Session 介绍、站点介绍）数据口径同步至 12,125 条 / 23 包 / 208 模块组 / 多版本，二维码卡片重渲
- 新增「站点介绍」公众号文章全套物料（完整版 + 纯净版 HTML、封面、首页二维码、言序 payload）

## 2026-11-04
- **新增 `resources/ln-sessions.md`（LN Session 速查）**：基于 docs.infor.com LN 10.7 官方中文文档 BFS 采集 1,299 条 Session（14 包 / 86 模块组，含 tt 工具包 48 条常用功能），中文/英文描述双语，支持模糊搜索与包/模块筛选，按包分片 JSON 懒加载 + 官方文档直达链接，紧凑表格样式
- **长尾关键词工程**：Bing 种子矩阵扩采（4,039 词），新增 `resources/long-tail-keywords.md`（1,739 条长尾词，可搜索/筛选，附站内承接页直达）
- 新增 5 个针对性页面：`infor-faq.md`、`infor-pricing-tco.md`、`infor-login-guide.md`、`infor-consultant-career.md`、`ln-planning-guide.md`
- mkdocs.yml 新增「选型与实用指南」导航组
- 行业动态页（`resources/news.md`）大扩充：Gartner CPQ / 劳动力管理技术双领导者认可、Infor + Kinaxis 供应链计划合作、Enterprise AI Adoption Impact Index 第 2 版、Velocity Week 2026 充实、新客户落地与成效表、IBM i（XA/LX/System21）现代化路径、Agentic Enterprise 网络研讨
- Velocity Suite 架构增补（`by-product/infor-os.md`）：Industry AI Agents 扩为 LN 12+ 角色矩阵，Agentic Orchestrator 补 AWS Bedrock 运行时与护栏
- 版本动态（`resources/release-notes.md`）：2026.10 Industry AI Agents 矩阵扩至完整清单
- 产品页完善：`cpq.md` 新增 Gartner CPQ 2026 领导者认可；`wms.md` / `csi.md` 补充客户案例
- 仓库文档同步：README 结构树与里程碑更新至 v6.0、TODO 头部日期更新

## 2026-10-10
- 新增 `by-product/mes.md`（Infor MES 制造运营管理平台），并补全与 Factory Track / QMS 的交叉引用网络

## 2026-10-08
- 新增 `resources/hot-keywords.md`（基于 Bing 数据的 757 条 Infor 热门搜索关键词索引）
- 行业动态与版本动态同步：Velocity Suite / Industry AI、Gartner 多项领导者认可、分析师视窗
- 新增 6 个产品专题页（Velocity Suite 相关）与 Accure 工具收录
- 收录 .NET Baan 库、`ln-product-ids.md`（SLM 授权码）、`ln-package-codes.md`（包代码）

## 2026-05-09
- 新建 4 个薄弱产品页面：`fsm.md`、`nexus.md`、`sunsystems.md`、`cpq.md`
- 重写 `resources/consultants.md`，新增 9 家顾问公司
- 新建 `resources/case-studies.md`（客户案例聚合）
- 新建 `resources/ion-integration.md`（ION BOD 开发指南）
- 新建 `resources/release-notes.md`（版本动态追踪）
- 新建 `resources/certification-guide.md`（认证考试指南）
- 新建 `resources/jobs.md`（招聘求职资源）

## 2026-05-08
- 项目初始化
- 搭建 MkDocs + Material for MkDocs 框架
- 完成 `resources/` 下各分类文件基础结构
