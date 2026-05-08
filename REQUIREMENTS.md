# Infor 生态资源导航站 - 需求文档

## 项目概述

### 项目定位
**Infor 生态资源导航网站** - 为Infor客户、实施伙伴、开发者和内部员工提供全面资源导航。

**双重定位**：
1. **主要定位**：第三方资源导航（论坛、顾问公司、博客、工具等）
2. **次要定位**：官方产品介绍（保留但非重点）

### 目标用户
- Infor 客户（现有和潜在）
- Infor 实施顾问
- Infor 开发人员
- Infor 内部员工
- 对 Infor 产品感兴趣的学习者

### 核心价值
- **资源聚合**：收集整理 Infor 生态中的优质资源（官方 + 第三方）
- **分类清晰**：按资源类型、产品、行业、平台等多维度分类
- **自动更新**：AI 自动搜集和整理第三方资源
- **中英双语**：服务全球 Infor 用户群体

---

## 技术规格

### 技术栈（最终确定）

**✅ 确定使用：MkDocs + Material for MkDocs**

- **静态站点生成器**：[MkDocs](https://www.mkdocs.org/)
- **主题**：[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **编程语言**：Python 3.13+
- **版本控制**：Git + GitHub
- **部署平台**：GitHub Pages
- **CI/CD**：GitHub Actions（可选）
- **AI 搜集**：Web Search + Web Fetch

**❌ 已弃用：Docusaurus**

~~Docusaurus 方案因 Node.js 环境问题已弃用，请不要参考 Docusaurus 相关配置。~~

### 依赖包
```
mkdocs>=1.5.0
mkdocs-material>=9.4.0
pymdown-extensions>=10.0.0
mkdocs-sitemap>=1.0.0
```

### 配置要求
- `mkdocs.yml` 主配置文件
- 支持深色/浅色主题切换
- 响应式设计（移动端适配）
- 搜索引擎优化（SEO）
- Site Map 生成

---

## 功能需求

### 核心功能

#### 1. 资源导航（主要焦点）

##### 1.1 第三方论坛与社区
**由 AI 自动搜集整理**
- Infor User Community（官方社区讨论板块）
- LinkedIn Infor 用户群组
- Reddit 相关板块（r/Infor, r/ERP 等）
- 地区性用户组论坛
- 微信公众号/知乎专栏（中国）

##### 1.2 顾问与实施公司
**由 AI 自动搜集整理**
- 按地区分类（北美、欧洲、亚太、中国等）
- 按产品专长分类（LN、M3、CS Industrial 等）
- 公司简介、联系方式、官网链接
- 用户评价（未来）

**目标数量**：每个地区至少 10-20 家公司，总计 40+ 家

##### 1.3 博客与教程
**由 AI 自动搜集整理**
- 技术博客（个人/团队）
- 视频教程（YouTube、Bilibili 等）
- 在线文档资源
- 技术问答（Stack Overflow 标签等）

**目标数量**：至少 30 个

##### 1.4 工具与插件
**由 AI 自动搜集整理**
- 开发工具下载
- 第三方插件市场
- 实用工具（ION 工具、LN 工具等）
- GitHub 开源项目

**目标数量**：至少 50 个

##### 1.5 培训与认证
- 官方培训资源
- 第三方培训机构
- 认证考试指南

#### 2. 产品介绍（保留但非重点）

**导航顺序**：放在第三方资源后面

##### 2.1 按业务功能分类
- ERP 系统（Infor LN, M3, CloudSuite Industrial）
- HCM（人力资源管理）
- EAM（企业资产管理）
- CRM（客户关系管理）
- 专业解决方案（CPQ, Factory Track）

##### 2.2 按产品线分类
- CloudSuite Industrial（SyteLine）
- Infor LN
- Infor M3
- 产品选择决策矩阵

##### 2.3 按行业分类
- 离散制造（汽车、工业设备、电子）
- 流程制造（食品饮料、化工、制药）
- 分销（分销、时尚、3PL）
- 服务（酒店）

##### 2.4 按技术平台分类
- Infor OS 平台
- Coleman AI
- Birst 分析
- ION（智能开放网络）
- Ming.le
- 文档管理

#### 3. 搜索功能
- 全文搜索（基于 MkDocs 自带搜索）
- 按分类筛选
- 按产品筛选
- 按地区筛选

#### 4. 资源提交
- GitHub Issue 模板（新资源推荐）
- Pull Request 流程（添加/更新资源）
- AI 自动搜集 + 人工审核机制

---

## AI 自动搜集规范

### 搜集范围

#### 1. 第三方论坛与社区
- Infor User Community 讨论板块
- LinkedIn Infor 用户群组
- Reddit（r/Infor, r/ERP, r/ManufacturingERP 等）
- 地区性用户组（如 Infor LN User Group - China）
- 技术问答平台（Stack Overflow, Quora）

**目标数量**：至少 20 个

#### 2. 顾问与实施公司
**搜索关键词**：
- "Infor partner" + [地区]
- "Infor LN consultant" + [地区]
- "Infor M3 implementation" + [地区]
- "Infor 实施伙伴" + [中国城市]

**目标数量**：每个地区至少 10-20 家，总计 40+ 家

#### 3. 博客与教程
**搜索关键词**：
- "Infor LN blog"
- "Infor M3 tutorial"
- "Infor ERP 技术博客"
- "Infor OS development"

**目标数量**：至少 30 个

#### 4. 工具与插件
**搜索范围**：
- GitHub（搜索 "Infor", "Infor LN", "Infor M3"）
- Infor App Store
- 第三方插件市场

**目标数量**：至少 50 个

### 搜集流程

1. **AI 使用 Web Search 搜索**
2. **AI 使用 Web Fetch 提取详细信息**
3. **AI 整理成标准格式**
4. **人工审核（用户确认）**
5. **合并到主分支**

### 审核标准

- ✅ 资源必须可公开访问
- ✅ 资源必须与 Infor 生态相关
- ✅ 信息必须真实、准确
- ✅ 链接必须有效
- ❌ 纯广告/营销内容（无实质技术内容）
- ❌ 非法网站或资源

---

## 内容结构

### 站点地图

```
首页 (index.md)
├── 快速开始
├── 资源分类导航
│   ├── 🌟 第三方资源（主要焦点）
│   │   ├── 论坛与社区 (resources/forums.md)
│   │   ├── 顾问与实施公司 (resources/consultants.md)
│   │   ├── 博客与教程 (resources/blogs.md)
│   │   ├── 工具与插件 (resources/tools.md)
│   │   └── 培训与认证 (resources/training.md)
│   └── 📚 产品介绍（保留但非重点）
│       ├── 按业务功能 (products/by-function/index.md)
│       ├── 按产品线 (products/by-product-line/index.md)
│       ├── 按行业 (products/by-industry/index.md)
│       └── 按技术平台 (products/by-platform/index.md)
├── 按产品浏览 (by-product/)
│   ├── Infor LN (by-product/ln.md)
│   ├── Infor M3 (by-product/m3.md)
│   ├── CloudSuite Industrial (by-product/csi.md)
│   └── Infor OS (by-product/infor-os.md)
├── 按地区浏览 (by-region/)
│   ├── 北美 (by-region/north-america.md)
│   ├── 欧洲 (by-region/europe.md)
│   ├── 亚太 (by-region/asia-pacific.md)
│   └── 中国 (by-region/china.md)
└── 关于本项目
    ├── 项目介绍 (about.md)
    ├── 资源提交规范 (submission-guide.md)
    ├── 贡献指南 (contributing.md)
    └── 联系我们 (contact.md)
```

---

## 非功能性需求

### 性能要求
- 页面加载时间 < 2秒
- 支持 100+ 并发访问
- 静态资源 CDN 加速（GitHub Pages 自带）

### 可用性要求
- 移动端适配
- 浏览器兼容（Chrome、Firefox、Safari、Edge 最新版本）
- 无障碍访问（WCAG 2.1 AA 级别）

### 维护性要求
- 清晰的文档结构
- 社区贡献友好
- **AI 自动搜集 + 人工审核**
- 定期内容审核（每季度）

### 安全性要求
- HTTPS 强制启用
- 外部链接安全提示
- 无用户数据存储（静态站点）

---

## 项目里程碑

### Phase 1: MVP（已完成 ✅）
- [x] 项目初始化
- [x] 基础站点搭建（MkDocs）
- [x] 核心页面创建（占位符）
- [x] 确定技术方案：MkDocs（非 Docusaurus）
- [x] **调整定位：第三方资源为主，产品介绍为辅**
- [x] **AI 自动搜集第三方论坛资源**（目标 20+，实际 24）
- [x] **AI 自动搜集顾问公司目录**（目标 40+，实际 42）
- [x] **AI 自动搜集博客和技术资源**（目标 30+，实际 63）
- [x] **AI 自动搜集工具和插件**（目标 50+，实际 66+）
- [x] 保留并优化产品介绍页面
- [x] **资源突破 200+，已部署至 GitHub Pages**

### Phase 2: 内容完善（进行中 🔄）
- [x] 扩充资源条目（目标 200+，实际 200+ ✅）
- [ ] 添加资源 Logo/截图
- [x] 完善按产品分类 ✅（4个分类页面）
- [x] 完善按地区分类 ✅（4个地区页面）
- [ ] 社区反馈收集

### Phase 3: 功能增强
- [ ] 集成评论系统
- [ ] 添加资源评分
- [ ] 搜索优化（Algolia DocSearch）
- [ ] 数据分析面板

### Phase 4: 生态扩展
- [ ] 多语言支持（中英文完整切换）
- [ ] RSS 订阅
- [ ] API 接口（供第三方调用）
- [ ] 移动应用（可选）

---

## 开源协议

- **代码**：MIT License
- **内容**：Creative Commons BY-SA 4.0
- **商标**：Infor 是 Infor Inc. 的注册商标，使用时需遵守商标使用规范

---

## 附录

### 参考资料
- [Infor 官网](https://www.infor.com)
- [Infor Documentation](https://docs.infor.com)
- [Infor Community](https://www.infor.com/company/community)

### 相关项目
- [Awesome Infor LN](https://github.com/...)（示例）
- [Infor 技术资源列表](https://...)（示例）

---

**文档版本**：v5.0（里程碑状态更新，Phase 1 已完成）
**最后更新**：2026-05-07
**维护者**：崔文远 Troy Cui
