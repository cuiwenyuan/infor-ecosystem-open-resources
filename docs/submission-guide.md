---
title: "资源提交规范 - Infor 生态第三方资源导航站"
description: "Infor 生态资源提交规范与流程，了解如何向本导航站推荐优质第三方资源。"
---

# 资源提交规范

欢迎向 **Infor 生态第三方资源导航站** 提交优质的 Infor 生态资源！本页面详细说明资源提交的标准和流程。

---

## 📋 可提交的资源类型

### ✅ 欢迎提交

- **论坛与社区**：Infor User Community 讨论板块、LinkedIn 群组、Reddit 板块等
- **顾问与实施公司**：合法的 Infor 实施合作伙伴（需提供真实信息）
- **博客与教程**：技术博客、视频教程、学习资源
- **工具与插件**：Infor 相关的开发工具、第三方插件、实用工具
- **培训与认证**：官方/第三方培训资源、认证指南
- **GitHub 仓库**：Infor 相关的开源项目、工具、示例代码
- **文档资源**：技术文档、白皮书、案例研究（公开可访问）

### ❌ 不接受提交

- 纯广告/营销内容（无实质技术内容）
- 非法网站或内容
- 包含恶意软件或病毒的网站
- 侵犯版权的资源
- 与 Infor 生态无关的资源

---

## 📝 提交格式规范

### 1. 论坛/社区资源模板

```markdown
## 资源名称

**类型**：论坛 / 社区 / 社交媒体群组

**适用产品**：Infor LN / M3 / CloudSuite Industrial / 通用

**地区**：全球 / 北美 / 欧洲 / 中国 / 其他

**语言**：英文 / 中文 / 多语言

**简介**：
简短描述（2-3句话）

**链接**：
- 官网：[链接](https://...)

**特色**：
- 特色点1
- 特色点2

**最后更新**：YYYY-MM-DD
```

### 2. 顾问公司模板

```markdown
## 公司名称

![公司Logo](../../assets/images/consultants/company-logo.png)  <!-- 可选 -->

**公司官网**：[链接](https://...)

**成立时间**：YYYY年

**总部地点**：城市，国家

**服务地区**：北美 / 欧洲 / 亚太 / 全球

**Infor 产品专长**：
- Infor LN ⭐⭐⭐⭐⭐
- Infor M3 ⭐⭐⭐⭐
- CloudSuite Industrial ⭐⭐⭐

**服务类型**：
- 实施咨询
- 定制开发
- 培训服务
- 技术支持

**联系方式**：
- 邮箱：contact@company.com
- 电话：+1-xxx-xxx-xxxx

**简介**：
公司详细介绍...

**客户案例**（可选）：
- 案例1
- 案例2

**最后更新**：YYYY-MM-DD
```

### 3. 博客/教程资源模板

```markdown
## 资源名称

**类型**：技术博客 / 视频教程 / 文档资源

**适用产品**：Infor LN / M3 / 通用

**作者/机构**：作者姓名或机构名称

**更新频率**：每周 / 每月 / 不定期

**语言**：英文 / 中文

**简介**：
简短描述（2-3句话）

**链接**：
- 官网：[链接](https://...)
- RSS（如有）：[链接](https://...)

**特色内容**：
- 特色内容1
- 特色内容2

**最后更新**：YYYY-MM-DD
```

### 4. 工具/插件资源模板

```markdown
## 工具名称

**类型**：开发工具 / 第三方插件 / 实用工具

**适用产品**：Infor LN / M3 / Infor OS / 通用

**平台**：Windows / Linux / Web / 跨平台

**许可证**：开源 / 免费 / 商业

**简介**：
简短描述（2-3句话）

**链接**：
- 官网：[链接](https://...)
- GitHub（如适用）：[链接](https://...)
- 下载链接（如适用）：[链接](https://...)

**主要功能**：
- 功能1
- 功能2

**最后更新**：YYYY-MM-DD
```

---

## 🚀 提交流程

### 方式一：通过 GitHub Issue 提交（推荐给非技术人员）

1. **访问 Issue 页面**
   - 点击[这里](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new?template=feature-request.md)创建新 Issue
   - 选择 "Feature Request" 模板

2. **填写信息**
   - **标题**：`[资源提交] 资源名称`
   - **内容**：使用上述模板格式，填写完整信息
   - **标签**：添加 `resource-submission` 标签

3. **等待审核**
   - 维护者会在 1-3 个工作日内审核
   - 审核通过后，维护者会将资源添加到网站

### 方式二：直接创建 Pull Request（推荐给技术人员）

1. **Fork 仓库**
   ```bash
   git fork https://github.com/cuiwenyuan/infor-ecosystem-open-resources.git
   ```

2. **创建分支**
   ```bash
   git checkout -b add-resource-资源名称
   ```

3. **编辑对应页面**
   - 论坛资源：编辑 `docs/resources/forums.md`
   - 顾问公司：编辑 `docs/resources/consultants.md`
   - 博客资源：编辑 `docs/resources/blogs.md`
   - 工具资源：编辑 `docs/resources/tools.md`
   - 或创建新文件（如按产品分类）

4. **提交更改**
   ```bash
   git add .
   git commit -m "Add resource: 资源名称"
   git push origin add-resource-资源名称
   ```

5. **创建 Pull Request**
   - 访问你的 Fork 页面
   - 点击 "New Pull Request"
   - 填写 PR 模板，说明添加的资源

6. **等待审核**
   - 维护者会审核你的 PR
   - 可能会要求修改
   - 审核通过后，会合并到主分支

---

## ✅ 审核标准

### 通用标准

- ✅ 资源必须可公开访问（无需登录即可查看基本信息）
- ✅ 资源必须与 Infor 生态相关
- ✅ 信息必须真实、准确、完整
- ✅ 链接必须有效（无 404 错误）
- ✅ 无恶意内容或病毒

### 顾问公司额外审核标准

- ✅ 必须有真实的官网
- ✅ 必须有有效的联系方式
- ✅ 必须有一定的 Infor 实施经验（需在简介中说明）
- ✅ 无欺诈或虚假宣传历史

---

## 🔄 资源更新流程

### 如果资源信息过期

1. 通过 GitHub Issue 提交更新请求
2. 或直接创建 Pull Request 编辑对应页面
3. 注明"信息更新"及原因

### 如果资源链接失效

1. 通过 GitHub Issue 报告死链
2. 维护者会验证并移除或更新链接

---

## 📞 寻求帮助

如果在提交过程中遇到问题，请：

1. **查看 [CONTRIBUTING.md](contributing.md)** - 详细贡献指南
2. **创建 GitHub Issue** - 选择 "Question" 模板
3. **加入 GitHub Discussions** - 社区讨论

---

## 🙏 致谢

感谢所有贡献资源的社区成员！你们的贡献让本网站更有价值。

贡献者名单将在网站首页和 GitHub README 中展示。

---

**最后更新**：2026-05-05  
**维护者**：Infor 生态社区
