---
title: "关于本项目 - Infor 生态第三方资源导航站"
description: "了解 Infor 生态第三方资源导航站的项目定位、核心理念和发展规划。"
---

# 关于本项目

## 项目简介

**Infor 生态第三方资源导航站** 是一个开源项目，旨在为 Infor 用户、实施顾问、开发者和学习者提供高质量的第三方资源链接导航。

### 项目定位

本网站是 **Infor 生态第三方资源导航站**，主要收录：

- ✅ **第三方论坛与社区** - Infor User Community、LinkedIn 群组、Reddit 板块等
- ✅ **顾问与实施公司** - 全球各地的 Infor 实施合作伙伴
- ✅ **博客与教程** - 技术博客、视频教程、学习资源
- ✅ **工具与插件** - 开发工具、第三方插件、实用工具
- ✅ **培训与认证** - 官方/第三方培训资源、认证指南

**不是**：
- ❌ Infor 官方文档站
- ❌ Infor 产品介绍站
- ❌ Infor Inc. 官方网站

---

## 项目范围

### ✅ 包含内容

- 第三方论坛、社区、讨论群组
- 合法的 Infor 实施顾问公司和合作伙伴
- 技术博客、教程、视频资源
- Infor 相关的开发工具、插件、实用工具
- 培训资源、认证指南
- GitHub 上的 Infor 相关开源项目

### ❌ 不包含内容

- Infor 官方产品文档（请访问 [Infor Documentation](https://docs.infor.com)）
- Infor 官方培训课程（请访问 [Infor Learning Center](https://www.infor.com/company/education)）
- 非法网站或资源
- 纯广告/营销内容（无实质技术内容）
- 与 Infor 生态无关的资源

---

## 技术架构

### 技术栈

- **静态站点生成器**：[MkDocs](https://www.mkdocs.org/)
- **主题**：[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **编程语言**：Python 3.13+
- **版本控制**：Git + GitHub
- **部署平台**：GitHub Pages
- **CI/CD**：GitHub Actions（可选）

### 项目结构

```
infor-ecosystem-open-resources/
├── docs/                           # 文档源文件
│   ├── index.md                    # 首页
│   ├── about.md                    # 本页面
│   ├── submission-guide.md         # 资源提交规范
│   ├── contributing.md             # 贡献指南
│   ├── resources/                  # 资源页面
│   │   ├── forums.md               # 论坛与社区
│   │   ├── consultants.md          # 顾问与实施公司
│   │   ├── blogs.md                # 博客与教程
│   │   ├── tools.md                # 工具与插件
│   │   └── training.md             # 培训与认证
│   ├── by-product/                 # 按产品分类
│   ├── by-region/                  # 按地区分类
│   └── assets/                     # 静态资源
├── mkdocs.yml                      # MkDocs 配置文件
├── requirements.txt                 # Python 依赖
├── README.md                       # 项目说明
├── REQUIREMENTS.md                 # 详细需求文档
├── TODO.md                         # 任务清单
├── CONTRIBUTING.md                 # 贡献指南（详细版）
├── LICENSE                         # MIT 许可证
└── .github/                        # GitHub 配置
```

---

## 贡献指南

本网站是开源项目，欢迎社区贡献！

### 如何贡献

1. **提交新资源** - 发现优质资源？[提交 Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new)
2. **修复错误** - 发现死链或错误？[提交 PR](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/pulls)
3. **完善内容** - 补充资源描述、添加 Logo 等
4. **翻译** - 帮助翻译成其他语言

### 贡献流程

详细贡献流程请阅读：[CONTRIBUTING.md](contributing.md)

简版流程：
1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 创建 Pull Request
5. 等待审核

---

## 许可证

### 代码许可证

本项目代码使用 [MIT License](LICENSE) 开源。

### 内容许可证

本网站内容使用 [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可证。

**含义**：
- **BY**（署名）：必须注明出处
- **SA**（相同方式共享）：衍生作品必须使用相同许可证

### 商标声明

- **Infor** 是 Infor Inc. 的注册商标
- 本网站与 Infor Inc. 无官方关联
- 使用 Infor 商标需遵守 [Infor 商标使用规范](https://www.infor.com/company/legal/trademarks)

---

## 联系方式

### 问题反馈

- **GitHub Issues**：[提交问题或建议](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues)
- **GitHub Discussions**：[社区讨论](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/discussions)

### 邮件联系

- **电子邮件**：troy.cui@qq.com（可选）

---

## 致谢

### 技术致谢

- [MkDocs](https://www.mkdocs.org/) - 优秀的静态站点生成器
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - 精美的主题
- [GitHub Pages](https://pages.github.com/) - 免费的静态网站托管

### 社区致谢

感谢所有贡献者的无私奉献！❤️

贡献者名单将在网站首页和 GitHub README 中展示。

---

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细更新记录。

### 最近更新

- **2026-05-07**：完成资源卡片样式设计、GitHub 模板、产品介绍页面优化（130+ 资源）
- **2026-05-06**：完成顾问公司、博客资源搜集，创建地区分类页面（100+ 资源）
- **2026-05-05**：项目启动，调整定位为第三方资源导航，完成论坛资源搜集（20+ 资源）

---

**最后更新**：2026-05-05  
**维护者**：Infor 生态社区  
**项目地址**：[GitHub](https://github.com/cuiwenyuan/infor-ecosystem-open-resources)
