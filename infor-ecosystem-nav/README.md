# Infor 产品生态系统导航站

[![GitHub stars](https://img.shields.io/github/stars/yourusername/infor-ecosystem-nav.svg?style=social&label=Star)](https://github.com/yourusername/infor-ecosystem-nav/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/infor-ecosystem-nav.svg?style=social&label=Fork)](https://github.com/yourusername/infor-ecosystem-nav/network/members)
[![GitHub license](https://img.shields.io/github/license/yourusername/infor-ecosystem-nav.svg)](LICENSE)
[![Website](https://img.shields.io/website?url=https://yourusername.github.io/infor-ecosystem-nav/)](https://yourusername.github.io/infor-ecosystem-nav/)

**Infor 产品生态系统导航站** - 一个开源的、中英文双语的 Infor 产品信息和导航网站。

## 🌟 在线访问

访问我们的网站：https://yourusername.github.io/infor-ecosystem-nav/

## 📋 项目简介

本项目旨在为 Infor 客户、实施合作伙伴、开发者和内部员工提供：

- ✅ **一站式导航** - 快速找到需要的 Infor 产品和解决方案
- ✅ **完整信息** - 产品详细介绍、功能列表、技术规格、资源链接
- ✅ **多语言支持** - 中英文双语，覆盖更广泛的用户群体
- ✅ **开源协作** - 欢迎社区贡献，共同维护和完善

## 🚀 快速开始

### 前置要求

- Python 3.8+ 
- pip（Python 包管理器）

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/yourusername/infor-ecosystem-nav.git
cd infor-ecosystem-nav
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

或者手动安装：

```bash
pip install mkdocs mkdocs-material pymdown-extensions mkdocs-video
```

3. **本地运行**

```bash
mkdocs serve
```

然后访问 http://127.0.0.1:8000/ 查看网站。

### 构建静态网站

```bash
mkdocs build
```

生成的静态文件在 `site/` 目录下。

## 📁 项目结构

```
infor-ecosystem-nav/
├── mkdocs.yml              # MkDocs 配置文件
├── requirements.txt        # Python 依赖
├── docs/                   # 文档内容（Markdown）
│   ├── index.md           # 首页
│   ├── about.md          # 关于页面
│   ├── products/          # 产品分类页面
│   │   ├── by-function/
│   │   ├── by-product-line/
│   │   ├── by-industry/
│   │   └── by-platform/
│   ├── products/details/  # 产品详情页面
│   ├── ecosystem/         # 生态系统页面
│   └── assets/           # 静态资源（图片、CSS、JS）
├── LICENSE                # MIT 许可证
├── CONTRIBUTING.md       # 贡献指南
└── README.md             # 本文件
```

## 🎯 功能特性

### 已实现的功能

- ✅ 产品分类浏览（按业务功能、产品线、行业、技术平台）
- ✅ 产品详情展示（基本信息、功能列表、技术规格、资源链接）
- ✅ 搜索功能（MkDocs 内置搜索）
- ✅ 响应式设计（Material 主题）
- ✅ 暗黑模式切换
- ✅ 生态系统关系图（Mermaid 图表）

### 计划功能

- ⏳ 高级过滤（按标签、产品线、行业过滤）
- ⏳ 产品对比功能
- ⏳ 收藏功能
- ⏳ 多语言完整支持（当前主要是中文，英文待完善）
- ⏳ Algolia DocSearch 集成
- ⏳ 评论和评分系统

## 🤝 贡献指南

我们欢迎任何形式的贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南。

### 快速贡献步骤

1. Fork 本仓库
2. 创建分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

### 贡献内容

- 添加缺失的产品信息
- 更新过时的产品描述
- 修复错误的链接
- 添加新产品和功能
- 改进网站设计和用户体验
- 翻译中英文内容

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) - 查看 LICENSE 文件了解详情。

MIT 许可证允许：
- ✅ 商业使用
- ✅ 修改
- ✅ 分发
- ✅ 专利使用
- ✅ 私人使用

## 📧 联系方式

### 项目维护者

- **GitHub**: [yourusername](https://github.com/yourusername)
- **Email**: your-email@example.com

### 问题反馈

- **GitHub Issues**: [提交问题或建议](https://github.com/yourusername/infor-ecosystem-nav/issues)
- **GitHub Discussions**: [参与讨论](https://github.com/yourusername/infor-ecosystem-nav/discussions)

## 🙏 致谢

### 数据来源

- [Infor 官方网站](https://www.infor.com)
- [Infor 产品文档](https://docs.infor.com)
- [Infor 客户门户](https://www.infor.com/support)
- [ERP Research](https://www.erpresearch.com)

### 技术栈

- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages](https://pages.github.com/)
- [GitHub Actions](https://github.com/features/actions)

### 灵感来源

- [Salesforce Products Guide](https://www.salesforceben.com/salesforce-products/)
- [Awesome Navigation](https://github.com/eryajf/awesome-navigation)
- [发现导航](https://github.com/xjh22222228/nav)

## 📊 统计数据

[![GitHub stars](https://img.shields.io/github/stars/yourusername/infor-ecosystem-nav.svg)](https://github.com/yourusername/infor-ecosystem-nav/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/infor-ecosystem-nav.svg)](https://github.com/yourusername/infor-ecosystem-nav/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/yourusername/infor-ecosystem-nav.svg)](https://github.com/yourusername/infor-ecosystem-nav/watchers)

[![GitHub issues](https://img.shields.io/github/issues/yourusername/infor-ecosystem-nav.svg)](https://github.com/yourusername/infor-ecosystem-nav/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/infor-ecosystem-nav.svg)](https://github.com/yourusername/infor-ecosystem-nav/pulls)
[![GitHub license](https://img.shields.io/github/license/yourusername/infor-ecosystem-nav.svg)](LICENSE)

---

**⭐ 如果这个项目对您有帮助，请给我们一个 Star！**
