# InforIndex 项目长期记忆

## 项目概要
- **项目名称**：Infor 生态第三方资源导航站
- **项目路径**：`C:\Users\Administrator\Documents\InforIndex`
- **技术栈**：MkDocs + Material for MkDocs（Python 3.13+）
- **部署目标**：GitHub Pages
- **定位**：收录 Infor 生态第三方资源（论坛/顾问/博客/工具/培训），非官方文档站

## 项目结构
```
InforIndex/
├── mkdocs.yml                    # MkDocs 配置（nav 结构定义）
├── TODO.md                       # 任务清单（当前完成度 80%）
├── docs/
│   ├── index.md                  # 首页（含统计卡片）
│   ├── about.md                  # 关于本项目
│   ├── submission-guide.md       # 资源提交规范
│   ├── contributing.md           # 贡献指南
│   ├── contact.md                # 联系我们
│   ├── resources/
│   │   ├── forums.md             # 论坛与社区（20+ 资源）
│   │   ├── consultants.md        # 顾问与实施公司（30+ 家）
│   │   ├── blogs.md              # 博客与教程（30+ 资源）
│   │   ├── tools.md              # 工具与插件（50+ 工具）
│   │   └── training.md           # 培训与认证（20+ 资源）
│   ├── by-product/
│   │   ├── ln.md                 # Infor LN 详情
│   │   ├── m3.md                 # Infor M3 详情
│   │   ├── csi.md                # CloudSuite Industrial 详情
│   │   └── infor-os.md           # Infor OS 详情
│   ├── products/
│   │   ├── by-function/index.md  # 按业务功能分类
│   │   ├── by-product-line/index.md  # 按产品线分类
│   │   ├── by-industry/index.md  # 按行业分类
│   │   └── by-platform/index.md  # 按技术平台分类
│   ├── by-region/
│   │   ├── north-america.md
│   │   ├── europe.md
│   │   ├── asia-pacific.md
│   │   └── china.md
│   └── assets/css/extra.css      # 自定义样式
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── resource-submission.md
    │   ├── bug-report.md
    │   └── question.md
    └── PULL_REQUEST_TEMPLATE.md
```

## 关键约定
- **资源搜集**：使用 Web Search + Web Fetch 组合搜集真实资源，不使用占位符
- **交叉引用**：每个产品/平台链接到 4 类资源（论坛/顾问/博客/工具），使用相对路径
- **内容格式**：标准 Markdown，每种资源类型有统一模板格式
- **CSS 样式**：extra.css 使用 `.resource-card` 基础类，`.resource-tag--xxx` 标签变体
- **导航结构**：第三方资源在前（导航第一组），产品介绍在后

## 关键约定
- **资源搜集**：使用 Web Search + Web Fetch 组合搜集真实资源，不使用占位符
- **交叉引用**：每个产品/平台链接到 4 类资源（论坛/顾问/博客/工具），使用相对路径
- **内容格式**：标准 Markdown，每种资源类型有统一模板格式
- **CSS 样式**：extra.css 使用 `.resource-card` 基础类，`.resource-tag--xxx` 标签变体
- **导航结构**：第三方资源在前（导航第一组），产品介绍在后
- **GitHub 信息**：用户名 `cuiwenyuan`，仓库名 `infor-ecosystem-open-resources`，在线地址 `https://cuiwenyuan.github.io/infor-ecosystem-open-resources/`

## 注意事项
- mkdocs.yml 中**不使用** `sitemap` 外部插件（Material 主题内置了 sitemap，外部插件会导致构建失败）
- GitHub Actions 工作流已创建：`.github/workflows/deploy.yml`（push main 分支自动触发）
- contact.md 中的邮箱占位符 `your-email@example.com` 还未替换（可选）
- Google Analytics ID (`G-XXXXXXXXXX`) 还未替换（可选）

## Phase 1 剩余任务
- 用户执行 git push 完成首次部署（见 DEPLOY.md）
- 持续完善和补充资源条目
