# 关于本项目

## 项目简介

**Infor 产品生态系统导航站** 是一个开源项目，旨在为 Infor 客户、实施合作伙伴、开发者和内部员工提供完整、准确、易用的 Infor 产品信息和导航。

### 为什么创建这个项目？

Infor 拥有复杂的产品组合（多条产品线、多个模块、多种部署方式），用户经常需要花费大量时间查找和比较产品信息。我们希望通过本项目：

- ✅ 提供**一站式导航**，快速找到需要的产品和解决方案
- ✅ 提供**完整信息**，包括产品详细介绍、功能列表、技术规格、资源链接
- ✅ 支持**多语言**（中英文），覆盖更广泛的用户群体
- ✅ 建立**开源协作**平台，欢迎社区贡献，共同维护和完善

## 项目范围

### 包含的内容

- ✅ Infor 7 大核心模块（财务、制造、供应链、HCM、EAM、CRM、Infor OS）
- ✅ 3 条主要产品线（CloudSuite Industrial、Infor LN、Infor M3）
- ✅ 行业解决方案（汽车、工业制造、食品饮料、医疗等）
- ✅ 技术平台（Infor OS、Coleman AI、Birst、ION、Ming.le）
- ✅ 产品关系图、集成矩阵、学习路径

### 不包含的内容

- ❌ Infor 产品的 pricing 信息（敏感信息）
- ❌ 客户专有信息或内部资料
- ❌ 第三方产品的详细比较（仅与 Infor 产品对比）

## 技术架构

### 技术栈

- **静态网站生成器**: MkDocs（Python）
- **主题**: Material for MkDocs
- **搜索**: MkDocs 内置搜索 + 可选 Algolia DocSearch
- **部署**: GitHub Pages
- **CI/CD**: GitHub Actions

### 项目结构

```
infor-ecosystem-nav/
├── mkdocs.yml              # MkDocs 配置文件
├── docs/                   # 文档内容（Markdown）
│   ├── index.md           # 首页
│   ├── products/          # 产品分类页面
│   │   ├── by-function/
│   │   ├── by-product-line/
│   │   ├── by-industry/
│   │   └── by-platform/
│   ├── products/details/  # 产品详情页面
│   ├── ecosystem/         # 生态系统页面
│   └── about.md          # 关于页面
├── docs/assets/           # 静态资源（图片、CSS、JS）
├── LICENSE                # 开源许可证
└── README.md             # 项目说明文件
```

## 如何贡献

我们欢迎任何形式的贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南。

### 快速贡献步骤

1. **Fork 本仓库**
2. **创建分支** (`git checkout -b feature/AmazingFeature`)
3. **提交更改** (`git commit -m 'Add some AmazingFeature'`)
4. **推送到分支** (`git push origin feature/AmazingFeature`)
5. **提交 Pull Request**

### 贡献内容

- 添加缺失的产品信息
- 更新过时的产品描述
- 修复错误的链接
- 添加新产品和功能
- 改进网站设计和用户体验
- 翻译中英文内容

## 许可证

本项目采用 [MIT 许可证](LICENSE) - 查看 LICENSE 文件了解详情。

MIT 许可证允许：
- ✅ 商业使用
- ✅ 修改
- ✅ 分发
- ✅ 专利使用
- ✅ 私人使用

## 联系方式

### 项目维护者

- **GitHub**: [yourusername](https://github.com/yourusername)
- **Email**: your-email@example.com

### 问题反馈

- **GitHub Issues**: [提交问题或建议](https://github.com/yourusername/infor-ecosystem-nav/issues)
- **讨论区**: [参与讨论](https://github.com/yourusername/infor-ecosystem-nav/discussions)

## 致谢

### 数据来源

- Infor 官方网站 (https://www.infor.com)
- Infor 产品文档 (https://docs.infor.com)
- Infor 客户门户 (https://www.infor.com/support)
- ERP Research (https://www.erpresearch.com)

### 技术栈

- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages](https://pages.github.com/)
- [GitHub Actions](https://github.com/features/actions)

### 灵感来源

- [Salesforce Products Guide](https://www.salesforceben.com/salesforce-products/)
- [Awesome Navigation](https://github.com/eryajf/awesome-navigation)
- [发现导航](https://github.com/xjh22222228/nav)

## 统计数据

[![GitHub stars](https://img.shields.io/github/stars/yourusername/infor-ecosystem-nav.svg?style=social&label=Star)](https://github.com/yourusername/infor-ecosystem-nav/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/infor-ecosystem-nav.svg?style=social&label=Fork)](https://github.com/yourusername/infor-ecosystem-nav/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/yourusername/infor-ecosystem-nav.svg?style=social&label=Watch)](https://github.com/yourusername/infor-ecosystem-nav/watchers)

[![GitHub issues](https://img.shields.io/github/issues/yourusername/infor-ecosystem-nav.svg)](https://github.com/yourusername/infor-ecosystem-nav/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/infor-ecosystem-nav.svg)](https://github.com/yourusername/infor-ecosystem-nav/pulls)
[![GitHub license](https://img.shields.io/github/license/yourusername/infor-ecosystem-nav.svg)](LICENSE)

---

**⭐ 如果这个项目对您有帮助，请给我们一个 Star！**
