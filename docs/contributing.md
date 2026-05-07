# 贡献指南

感谢你对 **Infor 生态第三方资源导航站** 的关注！本页面详细说明如何为项目做出贡献。

---

## 🎯 如何贡献

### 1. 提交新资源（最简单）

**适合人群**：所有用户，无需技术背景

**流程**：
1. 访问 [GitHub Issues](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new?template=feature-request.md)
2. 选择 "Feature Request" 模板
3. 填写资源信息（参考 [submission-guide.md](submission-guide.md) 的格式）
4. 提交 Issue
5. 等待维护者审核（1-3 个工作日）

### 2. 修复错误（简单）

**适合人群**：所有用户，无需技术背景

**流程**：
1. 发现死链、错误信息等
2. 访问 [GitHub Issues](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new?template=bug-report.md)
3. 选择 "Bug Report" 模板
4. 描述问题
5. 提交 Issue

### 3. 直接编辑文件（需要基本 Git 知识）

**适合人群**：有 Git 使用经验的用户

**流程**：
1. Fork 本仓库
2. 创建分支：`git checkout -b fix-typo`
3. 编辑文件（如 `docs/resources/forums.md`）
4. 提交更改：`git commit -m "Fix typo in forums.md"`
5. 推送分支：`git push origin fix-typo`
6. 创建 Pull Request

### 4. 添加新页面或大幅修改（需要技术背景）

**适合人群**：有 Markdown、Git、MkDocs 经验的用户

**流程**：
1. 阅读本指南的完整版本
2. 在本地测试：`mkdocs serve`
3. 提交 Pull Request
4. 等待代码审查

---

## 📝 代码规范

### Markdown 规范

- 使用 ATX 风格标题（`# H1`, `## H2`）
- 列表项之间不加空行
- 代码块使用围栏式（```）
- 链接格式：`[文本](URL)`
- 图片格式：`![alt](path)`

### 文件命名规范

- 使用小写字母和连字符：`forums.md`, `consultants.md`
- 避免空格和特殊字符
- 目录名也使用小写+连字符：`by-product/`, `by-region/`

### 提交信息规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**类型（type）**：
- `feat`: 新功能（如添加新资源）
- `fix`: 修复错误（如修正链接）
- `docs`: 文档更新
- `style`: 格式调整（不影响功能）
- `refactor`: 重构
- `test`: 测试相关

**示例**：
```
feat(resources): 添加 LinkedIn Infor 用户群组

添加了 LinkedIn 上的 Infor 用户交流群组资源

Closes #12
```

---

## ✅ 提交前检查清单

### 如果你提交新资源

- [ ] 资源链接可访问（无 404）
- [ ] 信息完整（参考 [submission-guide.md](submission-guide.md)）
- [ ] 格式正确（使用对应的模板）
- [ ] 无重复资源（已搜索确认）

### 如果你修复错误

- [ ] 明确指出错误位置（文件名 + 行号）
- [ ] 提供正确的信息
- [ ] 已测试修复后的效果（如有条件）

### 如果你添加新页面

- [ ] 已在 `mkdocs.yml` 的 `nav` 中添加导航
- [ ] 已测试本地构建（`mkdocs serve`）
- [ ] 无断链
- [ ] 图片已优化（压缩、合适尺寸）

---

## 🧪 本地测试

### 环境准备

1. 安装 Python 3.13+
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

### 测试流程

1. **启动本地服务器**
   ```bash
   mkdocs serve
   ```
   访问 `http://127.0.0.1:8000`

2. **检查以下内容**
   - 导航链接是否正常
   - 页面渲染是否正确
   - 图片是否加载
   - 搜索功能是否正常

3. **构建静态文件**（可选）
   ```bash
   mkdocs build
   ```
   检查 `site/` 目录输出

---

## 📋 Pull Request 规范

### PR 标题格式

```
<type>: <简短描述>
```

**示例**：
- `feat: 添加 10 个 Infor LN 相关论坛资源`
- `fix: 修复顾问公司联系方式错误`
- `docs: 更新贡献指南`

### PR 描述模板

```markdown
## 变更类型
- [ ] 新资源添加
- [ ] 错误修复
- [ ] 文档更新
- [ ] 新功能

## 变更描述
（详细描述你的变更）

## 测试步骤
1. 运行 `mkdocs serve`
2. 访问 [页面链接]
3. 确认 XXX

## 截图（可选）
（如果涉及样式变更，提供截图）

## 检查清单
- [ ] 已测试本地构建
- [ ] 无断链
- [ ] 遵循代码规范
- [ ] 更新了相关文档
```

---

## 🚀 审核流程

### 审核时间

- **Issue**：1-3 个工作日
- **Pull Request**：3-7 个工作日

### 审核标准

- ✅ 内容真实、准确
- ✅ 格式符合规范
- ✅ 无重复内容
- ✅ 无恶意链接
- ✅ 通过本地测试

### 审核结果

- **直接合并**：内容完美，无需修改
- **请求修改**：需根据审核意见修改
- **拒绝**：不符合项目范围或规范

---

## 💬 社区行为准则

### 我们的承诺

- 欢迎新手贡献者
- 尊重不同观点
- 接受建设性批评
- 关注项目最佳利益

### 禁止行为

- 使用性暗示语言或图像
- 人身攻击或侮辱
- 公开或私下骚扰
- 发布他人私密信息

### 举报

如遇到不当行为，请联系：[your-email@example.com](mailto:your-email@example.com)

---

## ❓ 寻求帮助

- **查看 [submission-guide.md](submission-guide.md)** - 资源提交格式
- **查看 [TODO.md](TODO.md)** - 当前任务清单
- **创建 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues)** - 选择 "Question" 模板
- **加入 [GitHub Discussions](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/discussions)** - 社区讨论

---

## 🙏 致谢

感谢所有贡献者的无私奉献！❤️

贡献者名单将在网站首页和 GitHub README 中展示。

---

**最后更新**：2026-05-05  
**维护者**：Infor 生态社区
