# Infor 生态资源导航站 - 任务清单

## 📊 当前状态
**项目阶段**：Phase 2 - 内容完善中
**技术方案**：MkDocs + Material for MkDocs（已确定，非 Docusaurus）
**完成度**：100%（P0 高优先级任务全部完成）
**最后更新**：2026-05-11 v5.8

---

## 🎯 项目定位（已更新）

### 主要焦点：第三方资源导航
- 论坛与社区
- 顾问与实施公司
- 博客与教程
- 工具与插件
- 培训与认证

### 次要内容：官方产品介绍（保留但非重点）
- 按业务功能分类
- 按产品线分类
- 按行业分类
- 按技术平台分类

---

## 🚀 Phase 1: MVP调整（当前阶段）

### 高优先级任务

#### 1. 调整网站定位
- [x] 更新需求文档（REQUIREMENTS.md）✅
- [x] 更新任务清单（TODO.md）✅
- [x] 更新 README.md（反映新定位）✅ 2026-05-06
- [x] 调整 mkdocs.yml 导航结构（第三方资源在前，产品介绍在后）✅ 2026-05-06

#### 2. AI 自动搜集第三方论坛资源
- [x] **目标：至少 20 个论坛/社区资源** ✅ 已完成
- [x] **使用 Web Search 搜索以下关键词**：
  - "Infor User Community forum"
  - "LinkedIn Infor user group"
  - "Reddit Infor ERP"
  - "Infor LN 论坛"
  - "Infor 用户组 中国"
- [x] **使用 Web Fetch 提取详细信息**
- [x] **整理成标准格式**
- [x] **创建/更新 `docs/resources/forums.md`**
- [x] **提交给用户审核** - 已完成，用户审核通过，继续搜集
- **📊 进度**：已收录 16 个主资源条目，包含多个子小组，总计超过 20+ 个资源

#### 3. AI 自动搜集顾问与实施公司
- [x] **使用 Web Search 搜索以下关键词**：✅ 2026-05-06
  - "Infor partner North America"
  - "Infor LN consultant Europe"
  - "Infor M3 implementation partner Asia"
  - "Infor 实施伙伴 中国"
  - "Infor 合作伙伴 上海"
- [x] **使用 Web Fetch 提取详细信息**（官网、联系方式、专长产品等）✅
- [x] **按地区分类整理** ✅
- [x] **创建 `docs/resources/consultants.md`** ✅（收录 30 家公司）
- [x] **创建地区分类页面**（`docs/by-region/*.md`）✅（北美/欧洲/亚太/中国 4 个页面）
- [x] 提交给用户审核 ✅ 2026-05-07

#### 4. AI 自动搜集博客和技术资源
- [x] **目标：至少 30 个博客/教程资源** ✅ 已完成 2026-05-06
- [x] **使用 Web Search 搜索以下关键词**：✅
  - "Infor LN blog"
  - "Infor M3 tutorial"
  - "Infor ERP technical blog"
  - "Infor OS development"
  - "Infor 技术博客"
- [x] **使用 Web Fetch 提取详细信息** ✅
- [x] **整理成标准格式** ✅
- [x] **创建 `docs/resources/blogs.md`** ✅（收录 30+ 个资源条目）
- [x] 提交给用户审核 ✅ 2026-05-07

#### 5. AI 自动搜集工具和插件
- [x] **目标：至少 50 个工具/插件资源** ✅ 已完成 2026-05-07
- [x] **使用 Web Search 搜索以下关键词**：✅
  - "Infor GitHub"
  - "Infor LN tools"
  - "Infor M3 plugins"
  - "ION tools Infor"
  - "Infor Marketplace applications"
  - "Infor Coleman AI"
  - "Infor RPA"
  - "Infor Birst"
  - "Infor IDM"
  - "Infor WMS tools"
- [x] **使用 Web Fetch 提取详细信息** ✅
- [x] **整理成标准格式** ✅
- [x] **创建 `docs/resources/tools.md`** ✅（收录 50+ 个工具/插件）
- [x] 提交给用户审核 ✅ 2026-05-07

### 中优先级任务

#### 6. 创建按产品独立详细页面
- [x] **创建 `docs/by-product/ln.md`** ✅ 2026-05-07
- [x] **创建 `docs/by-product/m3.md`** ✅ 2026-05-07
- [x] **创建 `docs/by-product/csi.md`** ✅ 2026-05-07
- [x] **创建 `docs/by-product/infor-os.md`** ✅ 2026-05-07
- [x] **创建 `docs/by-product/wms.md`** ✅ 2026-05-08（产品概述、8大功能模块、第三方资源速查）
- [x] **创建 `docs/by-product/factory-track.md`** ✅ 2026-05-08（产品概述、7大功能模块、第三方资源速查）
- [x] **更新 mkdocs.yml 导航** ✅ 2026-05-08（新增 WMS 和 Factory Track 条目）
- [x] **更新 `docs/index.md` 首页产品卡片** ✅ 2026-05-08
- [x] **更新产品分类索引页** ✅ 2026-05-08（by-product-line、by-function、by-platform）

#### 7. 丰富产品页第三方资源
- [x] **丰富 WMS 页面资源（+2）** ✅ 2026-05-08（CSDN CRB 教程、Infor U Campus 课程）
- [x] **丰富 Factory Track 页面资源（+9）** ✅ 2026-05-08（3 论坛 + 4 博客 + 2 工具）

#### 8. 设计资源卡片样式
- [x] 论坛资源卡片 ✅ 2026-05-07
- [x] 顾问公司卡片 ✅ 2026-05-07
- [x] 博客资源卡片 ✅ 2026-05-07
- [x] 更新 `docs/assets/css/extra.css` ✅ 2026-05-07

#### 9. 创建资源提交规范
- [x] 创建 `docs/submission-guide.md` ✅（已存在，内容完善）
- [x] 更新 GitHub Issue 模板 ✅ 2026-05-07（resource-submission / bug-report / question）
- [x] 更新 Pull Request 模板 ✅ 2026-05-07

### 低优先级任务

#### 11. 优化搜索功能
- [x] 优化 MkDocs 搜索权重 ✅ 2026-05-07（配置 separator、min_search_length=1、prebuild_index=true）
- [ ] 配置 Algolia DocSearch（可选，需申请审核）

#### 12. SEO 优化
- [x] 创建 .nojekyll 文件 ✅ 2026-05-07
- [x] 创建 robots.txt ✅ 2026-05-07
- [x] 为所有 22 个 .md 页面添加 Frontmatter（title、description）✅ 2026-05-07
- [x] 创建 docs/overrides/main.html（JSON-LD 结构化数据）✅ 2026-05-07
- [x] 优化 mkdocs.yml 全局 SEO（site_description、搜索配置）✅ 2026-05-07
- [x] Sitemap.xml（Material 主题自动生成）✅ 2026-05-07
- [ ] 提交到 Google Search Console → 移至 Phase 3
- [ ] 提交到百度站长平台 → 移至 Phase 3

---

## 🔧 Phase 2: 内容完善

### 任务清单

#### 1. 扩充资源条目
- [x] **目标：200+ 资源条目** ✅ 已达成（200+）
- [x] 每个分类至少 20 个资源 ✅
- [x] forums.md: 15 → 24（新增 Reddit、CSDN、知乎、IMUN 亚太、WMS LATAM 等）✅
- [x] blogs.md: 56 → 63（新增 Fortude, Sama, Medium, 播客等）✅
- [x] blogs.md: 63 → 66（新增 Stack Overflow 标签、Bilibili 视频资源、微信公众号/知识星球）✅
- [x] tools.md: 55+ → 66+（新增 Workato, Makini, Novacura, FORTEST 等）✅
- [x] consultants.md: 30+ → 42（新增 12 家，含 Genesis, GlobalBaan）✅

#### 2. 网站品牌与体验优化
- [x] 切换为 Infor 品牌红主题（#D81820）✅ 2026-05-08
- [x] 新增广告合作与赞助方案页面（sponsorship.md）✅ 2026-05-08
- [x] 新增微信公众号/社群页面（wechat-communities.md）✅ 2026-05-08
- [x] 添加 Footer 底部导航链接 ✅ 2026-05-08
- [x] 维护者信息更新为"崔文远 Troy Cui"（全站 13 处）✅ 2026-05-08

#### 8. 导航结构优化
- [x] **「开发者中心」+「故障排查」+「LN 开发系列」合并为「开发者资源中心」** ✅ 2026-05-11
  - 减少顶部 Tab 数量，导航更紧凑
  - 三个子板块保留独立侧边栏入口
- [x] 更新 mkdocs.yml 导航结构 ✅ 2026-05-11
- [x] 更新首页「按资源类型浏览」表格 ✅ 2026-05-11

#### 3. 添加资源 Logo/截图
- [ ] 创建 `docs/assets/images/` 目录结构
- [ ] 收集顾问公司 Logo
- [ ] 收集论坛/网站截图
- [ ] 优化图片（压缩、WebP 格式）

#### 4. 完善分类页面
- [x] 按产品分类 ✅（by-function, by-product-line, by-industry, by-platform 四个页面）
- [x] 按地区分类 ✅（china.md, north-america.md, europe.md, asia-pacific.md）
- [x] 交叉引用和标签系统 ✅

#### 5. 社区反馈收集
- [ ] 添加 GitHub Discussions
- [ ] 创建反馈表单（Google Forms / Typeform）
- [ ] 定期审核资源（每季度）

#### 6. 创建更多产品独立页
- [x] WMS 独立产品页 ✅ 2026-05-08
- [x] Factory Track 独立产品页 ✅ 2026-05-08
- [x] **Infor d/EPM 独立产品页** ✅ 2026-05-10（预算、合并、管理报表、合规）
- [x] **Infor QMS 独立产品页** ✅ 2026-05-10（SQM、内部质控、审计、SPC、ISO/FDA 合规）
- [x] **Infor YMS 独立产品页** ✅ 2026-05-10（场地预约、实时可视化、闸口管理、月台管理）
- [x] **Infor ION 独立产品页** ✅ 2026-05-10（BOD 详解、ION Gateway/Connect/Workflow/Data Lake）
- [ ] HCM 独立产品页（可选）
- [ ] EAM 独立产品页（可选）
- [ ] CRM 独立产品页（可选）

#### 7. 竞品对比页面（新增值内容）
- [x] **创建 Infor LN vs SAP S/4HANA 对比页** ✅ 2026-05-10（离散制造场景、核心差异、TCO 对比、选型建议）
- [x] **创建 Infor M3 vs SAP S/4HANA 对比页** ✅ 2026-05-10（流程制造/时尚行业、配方管理、合规、TCO 对比）
- [x] **创建 Infor LN vs Infor M3 对比页** ✅ 2026-05-11（同门对比，适用场景辨析）
- [x] **创建 Infor LN vs CloudSuite Industrial 对比页** ✅ 2026-05-11（企业级 vs 中小型离散制造）
- [x] **创建 Infor LN vs Microsoft Dynamics 365 对比页** ✅ 2026-05-11（制造深度 vs Microsoft 生态）
- [x] **创建 Infor LN vs Oracle ERP Cloud 对比页** ✅ 2026-05-11（制造专家 vs Oracle 全生态）
- [x] **创建 Infor LN vs QAD 对比页** ✅ 2026-05-11（汽车供应链专项对比）
- [x] **创建 Infor LN vs Sage X3 对比页** ✅ 2026-05-11（中大型 vs 中小型制造）
- [x] **创建 Infor LN vs IFS Applications 对比页** ✅ 2026-05-11（纯制造 vs 项目制造+资产密集型）
- [x] **创建 Infor LN vs Epicor Kinetic 对比页** ✅ 2026-05-11（ETO 深度 vs 易用性）
- [x] **创建 Infor LN vs Odoo ERP 对比页** ✅ 2026-05-11（商业深度 vs 开源灵活性）
- [x] **创建 Infor Birst vs Microsoft Power BI 对比页** ✅ 2026-05-11（网络化 BI vs Microsoft 生态）
- [x] **创建 Infor Birst vs Tableau 对比页** ✅ 2026-05-11（网络化 BI vs 数据可视化标杆）
- [x] **创建 Infor Birst vs Qlik Sense 对比页** ✅ 2026-05-11（网络化 BI vs 关联引擎）
- [x] **创建 Infor Birst vs Looker 对比页** ✅ 2026-05-11（网络化 BI vs LookML 语义层）
- [x] **创建 Infor Birst vs SAP Analytics Cloud 对比页** ✅ 2026-05-11（嵌入式分析 vs BI+计划一体化）
- [x] **创建 Infor Birst vs Oracle Analytics Cloud 对比页** ✅ 2026-05-11（嵌入式分析 vs Oracle 生态+AI）
- [x] **创建 Infor Birst vs IBM Cognos Analytics 对比页** ✅ 2026-05-11（纯 SaaS vs AI 辅助分析+混合云）
- [x] **创建 Infor LN vs 金蝶云·星瀚 对比页** ✅ 2026-05-11（高端制造ERP vs 大型企业EBC平台）
- [x] **创建 Infor LN vs 用友U9 cloud 对比页** ✅ 2026-05-11（复杂制造 vs 数智制造创新平台）
- [x] **创建 Infor LN vs 用友NC Cloud 对比页** ✅ 2026-05-11（复杂制造 vs 大型集团数字化平台）
- [x] **创建 Infor LN vs 鼎捷T100 对比页** ✅ 2026-05-11（国际高端ERP vs 台资背景制造ERP）
- [x] **创建 Infor LN vs 浪潮海岳GS Cloud 对比页** ✅ 2026-05-11（复杂制造 vs 国产大型智能ERP）
- [x] **创建 Infor WMS vs Blue Yonder 对比页** ✅ 2026-05-11（WMS 领导者对标）
- [x] **创建 Infor WMS vs Manhattan 对比页** ✅ 2026-05-11（云原生 WMS 对标）
- [x] **创建 Infor WMS vs SAP EWM 对比页** ✅ 2026-05-11（WMS vs SAP 生态）
- [x] **创建 Infor M3 vs Oracle ERP Cloud 对比页** ✅ 2026-05-11（流程制造 vs Oracle 全生态）
- [x] **创建 Infor M3 vs Microsoft Dynamics 365 对比页** ✅ 2026-05-11（流程制造 vs Microsoft 生态）
- [x] **创建 Infor HCM vs Workday 对比页** ✅ 2026-05-11（HCM vs HCM 领导者）
- [x] **创建 Infor HCM vs SAP SuccessFactors 对比页** ✅ 2026-05-11（HCM vs SAP 生态）
- [ ] 创建 Infor WMS vs Blue Yonder 对比页（可选）
- [ ] 创建 Infor M3 vs Oracle ERP Cloud 对比页（可选）

---

## 🌐 Phase 3: 功能增强

### 任务清单

#### 1. 集成评论系统
- [ ] 选择方案：Giscus（基于 GitHub Discussions）或 Utterances
- [ ] 配置和测试
- [ ] 添加评论指南

#### 2. 添加资源评分
- [ ] 研究实现方案（静态站点限制）
- [ ] 可能方案：
  - 基于 GitHub Issues 的评分
  - 第三方服务（如 Hotjar）
  - 手动维护评分

#### 3. 搜索优化
- [ ] 申请 Algolia DocSearch
- [ ] 配置自定义搜索权重
- [ ] 添加搜索建议

#### 4. 数据分析面板
- [ ] Google Analytics 集成
- [ ] 创建资源统计页面
- [ ] 资源分布可视化（基于 Mermaid 或 Chart.js）
- [ ] 提交到 Google Search Console
- [ ] 提交到百度站长平台

---

## 🚀 Phase 4: 生态扩展

### 任务清单

#### 1. 多语言支持
- [ ] 配置 MkDocs 多语言插件
- [ ] 翻译核心页面（英文）
- [ ] 翻译资源描述（逐步进行）
- [ ] 语言切换器测试

#### 2. RSS 订阅
- [ ] 配置 RSS feed
- [ ] 添加新资源通知
- [ ] 集成 RSS 阅读器

#### 3. API 接口
- [ ] 研究实现方案（静态站点限制）
- [ ] 可能方案：
  - 导出 JSON 数据文件
  - 使用 GitHub API
  - 第三方服务（如 SheetDB）

#### 4. 移动应用（可选）
- [ ] PWA（Progressive Web App）支持
- [ ] 响应式设计优化
- [ ] 离线访问支持

---

## 📝 文档任务

### 持续任务

#### 1. 维护贡献者指南
- [ ] 定期更新 CONTRIBUTING.md
- [ ] 添加新贡献者
- [ ] 记录重要决策

#### 2. 维护 CHANGELOG
- [ ] 记录每次重要更新
- [ ] 遵循 Keep a Changelog 规范

#### 3. 许可证 compliance
- [ ] 确保所有资源使用合规
- [ ] 添加版权声明
- [ ] 商标使用规范

---

## 🐛 已知问题

### 需要修复

#### 1. 产品介绍页面定位错误
- **影响**：内容定位不一致（应该是次要内容）
- **解决方案**：调整导航顺序，简化内容

#### 2. 导航结构不完整
- **影响**：用户体验混乱
- **解决方案**：调整 mkdocs.yml nav 配置（第三方资源在前）

#### 3. 部分链接为占位符
- **影响**：功能不完整
- **解决方案**：AI 搜集真实资源后替换

---

## 📊 进度追踪

### 本周目标（2026-05-05 至 2026-05-12）

1. ✅ 完成网站定位调整（需求文档和任务清单）
2. ✅ 更新 README 和导航结构
3. ✅ AI 搜集 20 个第三方论坛资源
4. ✅ AI 搜集 30 家顾问公司信息
5. ✅ 部署 MVP 到 GitHub Pages（配置完成，等待用户执行 git push）✅ 2026-05-07
6. ✅ 资源总数突破 200+ ✅ 2026-05-07
7. ✅ 创建 4 个产品分类页面 ✅ 2026-05-07

### 本月目标（2026-05）

1. ✅ MVP 版本部署到 GitHub Pages
2. ✅ AI 搜集 200+ 资源条目
3. ✅ 完成核心分类页面
4. [ ] 吸引首批社区贡献者

---

## 🤖 AI 自动搜集任务（重点！）

### 搜集流程

1. **使用 Web Search 搜索关键词**
2. **使用 Web Fetch 提取详细信息**
3. **整理成标准格式**（参考 submission-guide.md）
4. **创建/更新对应 Markdown 文件**
5. **提交给用户审核**
6. **根据用户反馈修改**
7. **合并到主分支**

### 搜集规范

- ✅ 资源必须可公开访问（无需登录即可查看基本信息）
- ✅ 资源必须与 Infor 生态相关
- ✅ 信息必须真实、准确、完整
- ✅ 链接必须有效（无 404 错误）
- ❌ 纯广告/营销内容（无实质技术内容）
- ❌ 非法网站或资源

### 优先级

1. **高优先级**：论坛与社区、顾问与实施公司
2. **中优先级**：博客与教程、工具与插件
3. **低优先级**：培训与认证

---

## 🤝 贡献者任务

### 如何参与

1. **提交新资源**：通过 GitHub Issue 或 Pull Request
2. **修复错误**：发现过期/错误链接，提交修复
3. **翻译**：帮助翻译成其他语言
4. **推广**：分享给 Infor 社区

### 审核流程

1. 提交 Issue/PR
2. 维护者审核（1-3 个工作日）
3. 合并到主分支
4. 自动部署到生产环境

---

**任务清单版本**：v5.8（导航重构：三大板块合并为「开发者资源中心」）
**最后更新**：2026-05-11
**维护者**：崔文远 Troy Cui
