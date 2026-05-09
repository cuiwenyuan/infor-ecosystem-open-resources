# Infor 生态开放资源导航站

[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-blue)](https://cuiwenyuan.github.io/infor-ecosystem-open-resources/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Infor Ecosystem](https://img.shields.io/badge/Infor-Ecosystem-purple.svg)](https://www.infor.com)

**在线访问**：[https://cuiwenyuan.github.io/infor-ecosystem-open-resources/](https://cuiwenyuan.github.io/infor-ecosystem-open-resources/)

---

## 🎯 项目定位

### 核心定位
**Infor 生态开放资源导航站** - 专注于收集和整理 Infor 生态中的优质第三方资源。

### 双重定位
1. **主要焦点**：第三方资源导航
   - 论坛与社区
   - 顾问与实施公司
   - 博客与教程
   - 工具与插件
   - 培训与认证

2. **次要内容**：官方产品介绍（保留但非重点）
   - 作为第三方资源的补充
   - 帮助用户了解产品基础信息

### 这不是...
- ❌ 不是 Infor 官方文档站
- ❌ 不是 Infor 产品介绍站
- ✅ 而是 Infor 生态中第三方资源的聚合导航站

---

## 📖 项目介绍

本项目是一个 **Infor 生态开放资源导航网站**，旨在为 Infor 用户、实施顾问、开发者和学习者提供高质量的第三方资源链接导航。

### 🎯 目标用户

- Infor 客户（现有和潜在）
- Infor 实施顾问和开发者
- Infor 技术爱好者
- 正在寻找实施合作伙伴的企业

### 💎 核心价值

- **资源聚合**：收集整理 Infor 生态中的优质第三方资源
- **分类清晰**：按资源类型、产品、地区等多维度分类
- **社区驱动**：开源项目，欢迎社区贡献
- **中英双语**：服务全球 Infor 用户群体

---

## 🗂️ 资源分类

本网站主要收录以下类型的第三方资源：

### 1. 论坛与社区 💬
- Infor User Community 讨论板块
- LinkedIn Infor 用户群组
- Reddit 相关板块（r/Infor, r/ERP 等）
- 地区性用户组论坛

### 2. 顾问与实施公司 🏢
- 按地区分类（北美、欧洲、亚太、中国等）
- 按产品专长分类（LN、M3、CloudSuite Industrial 等）
- 公司简介、联系方式、官网链接

### 3. 博客与教程 📝
- 技术博客（个人/团队）
- 视频教程（YouTube、Bilibili 等）
- 在线文档资源
- 微信公众号/知乎专栏（中国）

### 4. 工具与插件 🔧
- 开发工具下载
- 第三方插件市场
- 实用工具（ION 工具、LN 工具等）
- GitHub 开源项目

### 5. 培训与认证 🎓
- 官方培训资源
- 第三方培训机构
- 认证考试指南
- 学习路径推荐

---

## 🚀 快速开始

### 在线访问

访问我们的在线网站：**[https://cuiwenyuan.github.io/infor-ecosystem-open-resources/](https://cuiwenyuan.github.io/infor-ecosystem-open-resources/)**

### 本地运行

1. **克隆仓库**
   ```bash
   git clone https://github.com/cuiwenyuan/infor-ecosystem-open-resources.git
   cd infor-ecosystem-open-resources
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **启动本地服务器**
   ```bash
   mkdocs serve
   ```

4. **访问本地站点**
   打开浏览器访问 `http://127.0.0.1:8000`

### 构建静态文件

```bash
mkdocs build
```

生成的静态文件位于 `site/` 目录。

---

## 📂 网站结构

```
infor-ecosystem-open-resources/
├── docs/                           # 文档源文件
│   ├── index.md                    # 首页
│   ├── about.md                    # 关于本项目
│   ├── contact.md                  # 联系我们
│   ├── sponsorship.md              # 广告合作与赞助方案
│   ├── contributing.md             # 贡献指南
│   ├── submission-guide.md         # 资源提交规范
│   │
│   ├── resources/                  # 🌟 第三方资源（主要焦点）
│   │   ├── forums.md               # 论坛与社区（24 资源）
│   │   ├── consultants.md          # 顾问与实施公司（42 家）
│   │   ├── blogs.md                # 博客与教程（66 资源）
│   │   ├── tools.md                # 工具与插件（66+ 工具）
│   │   ├── training.md             # 培训与认证
│   │   └── wechat-communities.md   # 微信公众号与社群
│   │
│   ├── by-region/                  # 🌟 按地区浏览（第三方资源）
│   │   ├── north-america.md        # 北美地区
│   │   ├── europe.md               # 欧洲地区
│   │   ├── asia-pacific.md         # 亚太地区
│   │   └── china.md                # 中国地区
│   │
│   ├── products/                   # 📚 产品介绍（次要内容）
│   │   ├── by-function/            # 按业务功能分类
│   │   ├── by-product-line/        # 按产品线分类
│   │   ├── by-industry/            # 按行业分类
│   │   └── by-platform/            # 按技术平台分类
│   │
│   ├── by-product/                 # 📚 按产品浏览（次要内容）
│   │   ├── ln.md                   # Infor LN 相关资源
│   │   ├── m3.md                   # Infor M3 相关资源
│   │   ├── csi.md                  # CloudSuite Industrial 相关资源
│   │   └── infor-os.md             # Infor OS 相关资源
│   │
│   └── assets/                     # 静态资源
│       └── css/
│           └── extra.css           # 自定义样式（Infor 品牌红主题）
│
├── mkdocs.yml                      # MkDocs 配置文件
├── requirements.txt                # Python 依赖
├── README.md                       # 本文件
├── REQUIREMENTS.md                 # 详细需求文档
├── TODO.md                         # 任务清单
└── .github/                        # GitHub 配置
    ├── ISSUE_TEMPLATE/             # Issue 模板
    │   ├── resource-submission.md
    │   ├── bug-report.md
    │   └── question.md
    ├── PULL_REQUEST_TEMPLATE.md    # PR 模板
    └── workflows/
        └── deploy.yml              # GitHub Actions 自动部署
```

**说明**：
- 🌟 = 主要焦点（第三方资源）
- 📚 = 次要内容（产品介绍）

---

## ✨ 功能特性

**🌟 核心价值：第三方资源导航**

- ✅ **第三方资源聚合**：专注于论坛、顾问公司、博客、工具等第三方资源（200+ 条目）
- ✅ **产品介绍补充**：提供官方产品的基础介绍（作为第三方资源的补充）
- ✅ **响应式设计**：完美适配桌面端、平板和移动端
- ✅ **深色/浅色主题**：自动跟随系统设置，也可手动切换
- ✅ **全文搜索**：基于 MkDocs 的高性能搜索
- ✅ **分类筛选**：按资源类型、产品、地区等多维度筛选
- ✅ **自动部署**：GitHub Actions 自动构建并部署到 GitHub Pages
- ⏳ **中英双语**：支持中英文切换（规划中）
- ⏳ **评论系统**：基于 GitHub Discussions 的评论功能（规划中）

---

## 🤝 如何贡献

我们欢迎任何形式的贡献！

### 贡献方式

1. **提交新资源**
   - 发现优质的 Infor 第三方资源？请通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new?template=resource-submission.md) 提交
   - 或直接创建 Pull Request

2. **修复错误**
   - 发现死链、错误信息？[提交 Bug Report](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new?template=bug-report.md)

3. **完善内容**
   - 补充资源描述、添加 Logo 等

4. **推广项目**
   - 分享给 Infor 社区，在社交媒体上推荐

### 贡献流程

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

详细贡献指南请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📊 项目里程碑

### 当前状态
- **项目阶段**：Phase 2 - 内容完善中
- **技术方案**：MkDocs + Material for MkDocs（已确定）
- **完成度**：96%
- **最后更新**：2026-05-08

### 里程碑进度

| 阶段 | 状态 | 完成时间 |
|------|------|---------|
| Phase 1: MVP（200+ 资源，部署上线） | ✅ 已完成 | 2026-05-07 |
| Phase 2: 内容完善（品牌主题、赞助方案、社群页面） | 🔄 进行中（96%） | 2026-05-12 |
| Phase 3: 功能增强（评论、评分、Google Analytics） | 📝 待开始 | 2026-07-01 |
| Phase 4: 生态扩展（多语言、API） | 💡 规划中 | 2026-09-01 |

查看详细进度：[TODO.md](TODO.md)

---

## 🔧 技术栈

- **静态站点生成器**：[MkDocs](https://www.mkdocs.org/)
- **主题**：[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **编程语言**：Python 3.13+
- **版本控制**：Git + GitHub
- **部署平台**：GitHub Pages
- **CI/CD**：GitHub Actions

---

## 📜 许可证

- **代码**：[MIT License](LICENSE)
- **内容**：[Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## 🙏 致谢

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) — 优秀的 MkDocs 主题
- [GitHub Pages](https://pages.github.com/) — 免费静态托管
- 所有贡献者的无私奉献 ❤️

---

## 📞 联系我们

- **GitHub Issues**：[提交问题或建议](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues)
- **GitHub Discussions**：[社区讨论](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/discussions)

---

## ⚠️ 免责声明

- 本网站为独立第三方资源导航站，与 Infor Inc. 无官方关联
- 本网站收录的资源链接均为公开可访问的第三方资源
- 本网站不对收录资源的内容、准确性、合法性负责
- Infor 是 Infor Inc. 的注册商标，使用时需遵守商标使用规范

---

**文档版本**：v5.1（Phase 2 里程碑更新）
**最后更新**：2026-05-08  
**维护者**：崔文远 Troy Cui
