# Changelog

本页面记录 Infor 生态开放资源导航站的重大更新。

## 2026-11-12
- **行业动态页（`resources/news.md`）新增「2026 年 11 月生态速览」章节**：Gartner 2026 云 ERP 魔力象限（11-02 报告 / 11-06 官宣连续第 6 年 Leader）、2030 两条预测、ERX 术语溯源、2026.10 三条产品线 AI 落地细节、瓦努阿图政府签约、商业与生态侧信号，全部附来源链接
- **修正分析师认可表**：Cloud ERP MQ 由「2025 连续第 5 年」更新为「2026 连续第 6 年」，新增 2026 Critical Capabilities「2 个 Use Cases 得分最高」，补齐 WMS / WFM 公告日期与 Gartner 免责声明
- **主时间线补 6 行**：11-02 Gartner MQ、11-03 瓦努阿图签约、11-04 三条产品线详解、11-06 连续第 6 年 Leader，以及 10-27 之后的排序整理
- **版本动态页（`resources/release-notes.md`）补 2026-11-04 官方博客细节**：Automotive / Distribution / CPQ 能力表，MCP 6,000+ OData API、100+ → 12 domain agents、A2A 协议、100+ 新增 API 等架构数字，并加可用性中立提示
- **口径与去重**：标注 ERX 早在 2026-07 已提出、AI「发布」不等于「可启用」、中国区 11 月无新增本土客户官宣；剔除亿富智能装备与英富曼等同名干扰项

## 2026-11-11
- **新增「2026 中国区新客户与新项目」双平台图文物料**（`xiaohongshu-draft/2026-11-11-cn-2026-projects/`）：9 张 1080×1440（3:4）品牌红图文，附 `note.md` 文案方案与 `copy.txt` 纯文本发布稿
- 内容取自行业动态页同题专题，覆盖 4 家本土新客户、2 个海外交付节点、1 个跨年度项目与 2 个组织信号，全部标注来源与引用口径
- 双平台适配：小红书 01–08（不投放二维码页）、微信小绿书 01–09（第 9 张为**双入口**：国内镜像站与 GitHub Pages 各配 360px 独立二维码 + 完整网址，ECC-H 高容错、49 模块，并注明国内访问更快）
- 合规校验：标题 19 字符、小红书正文 881 字符、微信描述 962 字符，均在平台限制内；全文无旧站名简称

## 2026-11-10
- **「行业动态」新增「2026 中国区新客户与新项目」专题**（`resources/news.md`）：以时间线 + 分类展开的方式，补齐 Infor 中国区 2026 年可公开核实的新签、启动与上线项目，全部附来源链接
- 收录 **4 个中国本土新客户**：中秦兴龙工业集团（2026-03-04 启动）、苏州英赛斯（04-01 启动，计划下半年上线）、易开迪 EKT（04-13 启动）、德生堂壹壹壹智慧云仓（07-25 投运，Infor WMS）
- 收录 **2 个中国实施商交付的海外项目**：Toyo 东南亚工厂（03-13 启动）与美国工厂（07-01 Go-Live）
- 收录 **1 个跨年度延续项目**：凯斯纽荷兰 CNH（2025-10-31 签约，ERP + WMS 三地仓库，2026 推进）
- 补充 **中国区组织侧变化**：2026-02-04 APJ 领导层调整（大中华区并入 SENA）、2026-08-21 恩富软件（中国）法定代表人变更；并说明 CloudSuite 无中国大陆 Region 带来的 PIPL 数据驻留约束
- 明确标注信息来源与局限：中国区官方新闻稿缺位、动态多由实施伙伴发布、"公开可见 ≠ 全部签约"，并对 Toyo 主体存疑、中秦兴龙未披露产品版本等给出引用口径建议

## 2026-11-07
- **国内镜像站 `infor-ecosystem-open-resources.cuiwenyuan.cn` 正式上线**：GitHub Actions 新增 `deploy-cn` job，与 GitHub Pages 的 `deploy` job 并行、失败隔离；`push main` 一次触发双站自动更新
- 新增 `mkdocs.cn.yml`（`INHERIT` 主配置 + 独立 `site_url`），主 `mkdocs.yml` 零改动；canonical / `sitemap.xml` / JSON-LD 按 `.cn` 域名生成（实测 178 条全为 `.cn`，0 条 github.io）
- **国内访问优化**：国内站改用自托管 Roboto / Roboto Mono woff2 与本地 Mermaid，页面零境外前端请求；GitHub Pages 站维持 Google Fonts 与 unpkg mermaid，外观不变
- 补齐第三方许可文件：Roboto / Roboto Mono（SIL OFL 1.1）、Mermaid（MIT）
- 修复首次 Actions 报错 `Input required and not supplied: server`：新增 `Check FTP secrets` 自检步骤，Secrets 缺失时跳过上传并输出中文 warning 与 Job Summary；`DEPLOY.md` 补常见报错排查章节
- **上线验收全项通过**：首页 HTTP 200、约 0.10s（GitHub Pages 同期 0.90~7.06s）；字体 / mermaid / 23 个 LN Session 分片 / 二维码图均可访问；GitHub 站 Google Fonts 原样保留
- 仓库文档同步：`README.md` v6.1、`DEPLOY.md` 上线验收结果、`docs/index.md` 项目动态、`TODO.md`
- 新增微信贴图物料 `wechat-draft/2026-11-07-cn-mirror-launch/`：9 张 3:4 图 + `note.md` + `copy.txt`，围绕国内镜像站上线，含实测速度对比、双站架构图、两站差异表与 7 项验收清单；第 9 张二维码指向国内站首页，沿用既有品牌红视觉与库名口径

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
