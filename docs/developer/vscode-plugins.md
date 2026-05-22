---
title: "VS Code 插件 - 开发者资源中心"
description: "收录 Infor/Baan ERP 开发相关的 Visual Studio Code 扩展和插件。"
---

# 💻 VS Code 插件

> 在 VS Code 中提升 Infor ERP 开发效率的必备插件——从语法高亮到构件浏览。

---

## 🧩 插件列表

### Infor LN Constraint Language Support

**发布者**：[perjesid1](https://marketplace.visualstudio.com/publishers/perjesid1)
**平台**：VS Code Marketplace
**安装量**：258 | **评分**：★★★★★ (5.0)

为 VS Code 中的 Infor LN 约束语言（Constraint Language）提供语法高亮和代码片段支持。

**主要功能**：
- ✅ 完整的约束语言语法高亮
- ✅ 基于官方 Infor LN 文档的所有语言元素
- ✅ 包含 BaaN ERP 系统的遗留元素
- ✅ 常用代码片段（Snippets）

**适用场景**：LN 约束/规则的编写和调试

| 信息 | 内容 |
|------|------|
| **支持语言** | Infor LN Constraint Language |
| **安装方式** | VS Code → 扩展 → 搜索 `ln-constraint-language-support` |
| **许可证** | 免费 |
| **Marketplace** | [安装链接](https://marketplace.visualstudio.com/items?itemName=perjesid1.ln-constraint-language-support) |

---

### Infor LN DevTools

**发布者**：[shubham225](https://github.com/shubham225)
**平台**：GitHub（开源，MIT 许可证）
**状态**：⚠️ 尚未发布到 VS Code Marketplace

专为 Infor LN ERP 开发者打造的 VS Code 扩展，支持从远程 LN 环境浏览和导入组件。

**主要功能**：
- ✅ **组件探索**：以 `Type → Package → Module → Component` 层级结构浏览 LN 构件
- ✅ **支持组件类型**：Table（表）、Session（会话）、Script（脚本）、Function（功能）、Domain（域）、Report（报表）
- ✅ **导入工作流**：选中组件后生成 ZIP 并自动解压到工作区
- ✅ **BaanC 语言支持**：语法高亮 + 智能自动完成
- ✅ **函数 IntelliSense**：显示函数签名、参数列表、参数类型

**适用场景**：LN 开发者日常编码、构件浏览与管理

| 信息 | 内容 |
|------|------|
| **支持语言** | BaanC (.bc) |
| **后端需求** | 需要 Infor LN 环境（通过 API 连接） |
| **许可证** | MIT License |
| **GitHub** | [仓库地址](https://github.com/shubham225/infor-ln-devtools) |

---

## 📋 对比一览

| 特性 | LN Constraint Language Support | LN DevTools |
|------|-------------------------------|-------------|
| 语法高亮 | ✅ 约束语言 | ✅ BaanC |
| 代码片段 | ✅ | ⚠️ 部分 |
| 组件浏览 | ❌ | ✅ |
| 构件导入 | ❌ | ✅ |
| IntelliSense | ❌ | ✅ 函数签名 |
| Marketplace 已上架 | ✅ | ❌（仅 GitHub） |
| 安装量 | 258 | 0（未上架） |
| 适用版本 | 所有 LN 版本 | LN 10.7+ |

---

## 🚀 安装指南

### 方式一：从 VS Code Marketplace 安装（推荐）

1. 打开 VS Code
2. 点击左侧活动栏的 **扩展** 图标（或按 `Ctrl+Shift+X`）
3. 在搜索框中输入插件名称
4. 找到后点击 **安装**
5. 安装完成后可能需要重启 VS Code

### 方式二：从 VSIX 文件安装（仅适用于 LN DevTools）

```bash
# 1. 克隆仓库
git clone https://github.com/shubham225/infor-ln-devtools.git

# 2. 安装依赖并打包
cd infor-ln-devtools
npm install
npm run package

# 3. 在 VS Code 中安装 VSIX
# Ctrl+Shift+P → "Extensions: Install from VSIX..." → 选择生成的 .vsix 文件
```

---

## 📝 注意事项

- **LN DevTools** 需要后端 Infor LN 环境的 API 支持，请确保已配置正确的连接信息
- **LN Constraint Language Support** 开箱即用，无需额外配置
- 以上插件均非 Infor 官方出品，使用时请自行评估风险

---

## 🤝 贡献新插件

欢迎推荐更多 VS Code 插件！请确保：

- ✅ 与 Infor/Baan ERP 开发直接相关
- ✅ 在 VS Code Marketplace 或 GitHub 上可公开访问
- ✅ 信息真实准确，链接有效

请通过 [GitHub Issues](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues) 提交建议。

---

## 相关页面

- [开源项目](open-source.md) - 更多 Infor 开源工具
- [LN 4GL 代码库](ln-4gl-snippets.md) - LN 4GL 代码片段
- [工具与插件](../resources/tools.md) - 全品类开发工具

---

**最后更新**：2026-05-23
