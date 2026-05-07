# 贡献指南

感谢您对 **Infor 产品生态系统导航站** 项目的关注！我们欢迎任何形式的贡献。

## 🤔 如何贡献

### 报告 Bug

如果您发现 Bug，请创建 [GitHub Issue](https://github.com/yourusername/infor-ecosystem-nav/issues/new?template=bug-report.md) 并使用 Bug 报告模板。

请在报告中包含：
- 问题的简短描述
- 复现步骤
- 预期行为 vs 实际行为
- 截图（如适用）
- 您的环境（浏览器、设备、操作系统）

### 功能建议

如果您有功能建议，请创建 [GitHub Issue](https://github.com/yourusername/infor-ecosystem-nav/issues/new?template=feature-request.md) 并使用功能请求模板。

请包含：
- 功能的简短描述
- 为什么需要这个功能
- 可能的实现方案（可选）

### 提交 Pull Request

1. **Fork 本仓库**
   ```bash
   # 点击 GitHub 上的 "Fork" 按钮
   ```

2. **创建分支**
   ```bash
   git clone https://github.com/YOUR-USERNAME/infor-ecosystem-nav.git
   cd infor-ecosystem-nav
   git checkout -b feature/amazing-feature
   ```

3. **进行更改**
   - 添加或更新产品信息
   - 修复错误或问题
   - 改进网站设计和用户体验
   - 添加新功能

4. **提交更改**
   ```bash
   git add .
   git commit -m "Add: 添加 Infor XXX 产品详情"
   git push origin feature/amazing-feature
   ```

5. **提交 Pull Request**
   - 访问您的 Fork 页面
   - 点击 "Compare & pull request"
   - 填写 PR 描述模板
   - 提交 PR

## 📝 贡献内容

### 产品信息

- **添加缺失的产品**：创建新的产品详情页面
- **更新产品信息**：更新过时的描述、功能、链接
- **修复错误**：更正错误的产品信息或链接

### 网站改进

- **设计改进**：改进 CSS 样式、响应式设计
- **功能添加**：搜索、过滤、对比、收藏等功能
- **性能优化**：网站加载速度、SEO 优化

### 文档改进

- **翻译**：中英文翻译和改进
- **文档完善**：改进 README、贡献指南等文档
- **示例添加**：添加更多示例和使用案例

## 📋 代码规范

### Markdown 规范

- 使用 Markdown 格式编写内容
- 使用清晰的标题层级（H1, H2, H3...）
- 使用表格、列表、代码块等格式化内容
- 确保所有链接有效

### 产品详情页面模板

```markdown
# 产品名称

![产品 Logo](../../assets/images/product-name.png)

## 产品概述

[产品简要描述]

- **产品类型**: [ERP 系统/ SCM/ HCM/ ...]
- **产品线**: [CloudSuite Industrial/ Infor LN/ Infor M3/ ...]
- **目标客户**: [目标客户描述]
- **核心行业**: [适用行业]

## 核心功能

### 功能分类
- ✅ 功能 1
- ✅ 功能 2

## 技术规格

| 项目 | 说明 |
|------|------|
| **部署方式** | [云部署/ 本地部署] |
| **云平台** | [Infor OS/ ...] |

## 适用场景

### ✅ 适合的企业
- [适用场景 1]
- [适用场景 2]

### ❌ 不适合的企业
- [不适用场景 1]
- [不适用场景 2]

## 相关产品

| 产品 | 关系 |
|------|------|
| [产品 A](product-a.md) | [关系描述] |

## 资源链接

- 📘 [官方文档](https://...)
- 🔧 [API 文档](https://...)
- 📊 [案例研究](https://...)
- 📹 [产品演示视频](https://...)

## 集成能力

[集成能力描述]

## 学习路径

[学习路径描述]

---

**💡 需要帮助？** 访问 [Infor 客户门户](https://www.infor.com/support) 获取支持。
```

### CSS 规范

- 使用 `extra.css` 添加自定义样式
- 遵循 Material for MkDocs 主题规范
- 使用 CSS 变量（如 `var(--md-primary-fg-color)`）
- 确保暗黑模式兼容性

## ✅ 检查清单

提交 PR 前，请确保：

- [ ] 代码可以正常构建（`mkdocs build` 无错误）
- [ ] 所有链接有效（无 404 错误）
- [ ] Markdown 格式正确
- [ ] 添加了必要的截图（如适用）
- [ ] 更新了相关文档
- [ ] 遵循了代码规范
- [ ] 测试了本地构建结果

## 🚀 本地测试

在提交 PR 前，请在本地测试您的更改：

```bash
# 安装依赖
pip install -r requirements.txt

# 本地运行（热重载）
mkdocs serve

# 构建静态网站
mkdocs build
```

然后访问 http://127.0.0.1:8000/ 查看更改效果。

## 📧 联系方式

如果您有任何问题，请：

- 创建 [GitHub Issue](https://github.com/yourusername/infor-ecosystem-nav/issues)
- 加入 [GitHub Discussions](https://github.com/yourusername/infor-ecosystem-nav/discussions)
- 发送邮件到：your-email@example.com

## 📄 许可证

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

**再次感谢您的贡献！** 🙏
