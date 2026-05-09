# 部署到 GitHub Pages - 完整操作说明

**仓库信息**：
- GitHub 用户名：`cuiwenyuan`
- 仓库名：`infor-ecosystem-open-resources`
- 在线访问地址：`https://cuiwenyuan.github.io/infor-ecosystem-open-resources/`

---

## 第一步：在 GitHub 上创建仓库

1. 打开浏览器，访问 [https://github.com/new](https://github.com/new)
2. 填写以下信息：
   - **Repository name**：`infor-ecosystem-open-resources`
   - **Description**：`Infor 生态开放资源导航站 - 论坛、顾问公司、博客、工具等资源链接导航`
   - **Visibility**：选 `Public`（Public 仓库 GitHub Pages 免费）
3. **滚动到页面底部**，找到 `Initialize this repository with:` 区域：
   - ❌ **不要勾选** `Add a README file`
   - ❌ **不要选择** `.gitignore template`
   - ❌ **不要选择** `Choose a license`
   > 以上三个选项全部留空即可。新版 GitHub 页面布局可能有调整，这三个选项通常在 Repository name 和 Description 下方、Create repository 按钮上方。如果找不到，尝试往下滚动。
4. 点击绿色 **Create repository** 按钮
5. 创建成功后会跳转到仓库页面，顶部显示 `Quick setup — if you've done this kind of thing before`，说明仓库是空的，可以继续下一步。

**⚠️ 如果不小心勾选了 README / .gitignore / License**：
- 不用删除仓库，在第二步的 `git push` 之前多执行一步：
  ```bash
  git pull origin main --allow-unrelated-histories
  ```
- 如果弹出合并编辑器，直接保存退出即可。

---

## 第二步：本地初始化 Git 仓库并推送

在你的电脑上打开 **命令提示符** 或 **Git Bash**，执行以下命令：

```bash
# 进入项目目录
cd C:\Users\Administrator\Documents\InforIndex

# 初始化 Git 仓库（如果还没有）
git init

# 设置默认分支为 main
git branch -M main

# 添加所有文件到暂存区
git add .

# 提交（首次提交）
git commit -m "feat: 初始化 Infor 生态开放资源导航站

- 论坛与社区资源（20+ 条目）
- 顾问与实施公司（30+ 家）
- 博客与教程（30+ 资源）
- 工具与插件（50+ 工具）
- 培训与认证（20+ 资源）
- 按产品/地区/功能/行业分类页面
- MkDocs + Material 主题
- GitHub Actions 自动部署"

# 添加远程仓库
git remote add origin https://github.com/cuiwenyuan/infor-ecosystem-open-resources.git

# 推送到 GitHub
git push -u origin main
```

**如果提示需要登录**：输入你的 GitHub 用户名和密码（或 Personal Access Token）。

---

## 第三步：配置 GitHub Pages

1. 打开仓库页面：[https://github.com/cuiwenyuan/infor-ecosystem-open-resources](https://github.com/cuiwenyuan/infor-ecosystem-open-resources)
2. 点击顶部的 **Settings** 标签
3. 左侧菜单找到 **Pages**（在 Code and automation 分类下）
4. 在 **Source** 部分，选择 **GitHub Actions**（而不是 Deploy from a branch）
5. 点击 **Save**

---

## 第四步：等待自动部署

Push 代码后，GitHub Actions 会自动触发构建和部署流程：

1. 在仓库页面点击 **Actions** 标签查看部署进度
2. 找到 `Deploy MkDocs to GitHub Pages` 工作流
3. 等待 2-5 分钟，绿色 ✅ 表示部署成功

**查看部署状态**：
`https://github.com/cuiwenyuan/infor-ecosystem-open-resources/actions`

---

## 第五步：访问上线网站

部署成功后，访问：
**[https://cuiwenyuan.github.io/infor-ecosystem-open-resources/](https://cuiwenyuan.github.io/infor-ecosystem-open-resources/)**

---

## 常见问题

### Q1：push 时提示 "Permission denied"
**解决**：需要配置 GitHub 个人访问令牌（PAT）：
1. 访问 [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. 点击 **Generate new token (classic)**
3. 勾选 `repo` 权限
4. 复制生成的 token，用它代替密码

### Q2：GitHub Actions 构建失败
**检查步骤**：
1. 点击 Actions → 失败的工作流 → 查看错误日志
2. 常见原因：requirements.txt 中的包版本冲突
3. 尝试解决：删除版本限制，让 pip 自动选择

### Q3：页面显示 404
**解决**：
1. 确认 Settings → Pages → Source 选择的是 **GitHub Actions**
2. 确认 `mkdocs.yml` 中 `site_url` 正确（已配置为 `https://cuiwenyuan.github.io/infor-ecosystem-open-resources/`）

### Q4：本地预览（可选）
如果想在推送前本地预览效果：
```bash
pip install mkdocs-material pymdown-extensions
mkdocs serve
# 打开 http://127.0.0.1:8000
```

---

## 后续更新

每次修改内容后，只需：
```bash
git add .
git commit -m "docs: 更新资源内容"
git push
```

GitHub Actions 会自动重新构建并部署，通常 2-3 分钟后生效。

---

**完成后网站地址**：[https://cuiwenyuan.github.io/infor-ecosystem-open-resources/](https://cuiwenyuan.github.io/infor-ecosystem-open-resources/)
