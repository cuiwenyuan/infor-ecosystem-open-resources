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

---

## 附录：国内镜像站部署（2026-11-07 新增）

GitHub Pages 在国内访问偏慢、偶发不可达，因此增加一份**国内镜像站**，与 GitHub Pages 保持同一份内容、同一次推送自动更新。

- **镜像域名**：`https://infor-ecosystem-open-resources.cuiwenyuan.cn/`（根路径部署）
- **主机**：阿里云 ECS + 宝塔面板，`cuiwenyuan.cn` 已备案、国内节点
- **接入方式**：普通 FTP（**主机不支持 FTPS**），端口 21，部署到 FTP 根目录

### 架构：一次 push，两个站点

`.github/workflows/deploy.yml` 里有两个**并行、互不依赖**的 job，任一失败不影响另一个：

| job | 目标 | 构建配置 | 命令 |
|---|---|---|---|
| `deploy` | GitHub Pages | `mkdocs.yml`（原样，零改动） | `mkdocs gh-deploy --force` |
| `deploy-cn` | 国内镜像站 | `mkdocs.cn.yml`（INHERIT 主配置） | `mkdocs build -f mkdocs.cn.yml --strict -d site-cn` → FTP 增量同步 |

触发方式沿用现有 `push main` + `workflow_dispatch`（可在 Actions 页手动重跑）。

**为什么要两次构建**：GitHub Pages 地址带 `/infor-ecosystem-open-resources/` 子路径，国内站是根路径 `/`；`site_url` 会写进 canonical、`sitemap.xml` 和 JSON-LD，必须各自生成，否则搜索引擎会把国内站判成 GitHub Pages 的重复内容。

**两站差异**（内容完全相同，仅前端资源与元数据不同）：

| 项 | GitHub Pages 站 | 国内镜像站 |
|---|---|---|
| 构建配置 | `mkdocs.yml` | `mkdocs.cn.yml` |
| `site_url` | `cuiwenyuan.github.io/infor-ecosystem-open-resources/` | `infor-ecosystem-open-resources.cuiwenyuan.cn/` |
| 字体 | **维持 Google Fonts**（Roboto / Roboto Mono） | **自托管 woff2**（`fonts-selfhost.css` + `assets/fonts/`），视觉一致 |
| Mermaid | `unpkg.com/mermaid@10` | 本地 `assets/javascripts/mermaid.min.js` |
| 境外前端请求 | 有 | **零**（实际页面已验证） |

主 `mkdocs.yml` 一个字都不改，因此 GitHub Pages 站的字体与行为完全不变。

### 需要你在主机 / GitHub 后台完成的操作

> ⚠️ 密码不要发给我，也不要写进任何项目文件，只填到 GitHub Secrets。

**1. DNS 解析**

在域名解析处添加一条记录，把 `infor-ecosystem-open-resources` 指向主机公网 IP：

| 类型 | 主机记录 | 记录值 |
|---|---|---|
| A | `infor-ecosystem-open-resources` | 阿里云 ECS 公网 IP |

**2. 宝塔面板添加站点**

- 「网站」→ 添加站点，域名填 `infor-ecosystem-open-resources.cuiwenyuan.cn`，先建好站点根目录（如 `/www/wwwroot/infor-ecosystem-open-resources.cuiwenyuan.cn/`）
- 申请免费 SSL 证书（Let's Encrypt），并开启「强制 HTTPS」
- 「设置 → 默认文档」确认 `index.html` 在列表内 —— 这是 `/resources/ln-sessions/` 这类目录能正常打开的关键

**3. 创建独立 FTP 账号（重要）**

- 「FTP」→ 创建账号，**根目录直接指向上面这个子域名的站点根目录**
- 不要用主账号、也不要把根目录设为 `/www/wwwroot/`：`FTP-Deploy-Action` 会按 state 文件删除服务器上的旧文件，共用根目录有误删其他站点的风险
- 记下 FTP 服务器地址（IP 或域名）、用户名、密码

**4. 放行 FTP 端口（最常见的失败原因）**

FTP 使用被动模式（PASV），需要同时放行控制端口和数据端口：

| 位置 | 需要放行 |
|---|---|
| 阿里云 ECS 安全组（入方向） | TCP `21` + 被动端口段 |
| 宝塔「安全」→ 系统防火墙 | 同上 |

被动端口段以宝塔「FTP 管理 → 配置」里的 `PassivePortRange` 为准，Pure-FTPd 常见默认是 `39000-40000`。

若出现「能登录但 LIST / 上传超时」，多半是 ECS 在 NAT 后返回了私网 IP，需在 Pure-FTPd 配置里设置 `ForcePassiveIP` 为 ECS 公网 IP。

**5. 确认没有 IP 限制**

宝塔若开启「FTP 登录 IP 限制 / 境外 IP 拦截」需关闭 —— GitHub Actions 的出口 IP 不固定。（本项目已确认未开启。）

**6. 添加 GitHub Secrets**

仓库 → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`，添加 3 个：

| Secret 名称 | 值 |
|---|---|
| `FTP_SERVER` | FTP 服务器地址（IP 或域名，不带 `ftp://`、不带端口） |
| `FTP_USERNAME` | 第 3 步创建的独立账号用户名 |
| `FTP_PASSWORD` | 该账号密码 |

端口 `21`、`protocol: ftp`、`server-dir: ./` 已明文写在 workflow 里，无需配置。

### ⚠️ 明文 FTP 的安全提醒

主机不支持 FTPS，因此账号密码与文件内容在传输中是**明文**的。已采取的缓解措施：

- 使用**仅授权该子域名目录**的独立最小权限账号
- 密码只存于 GitHub Secrets，不落盘、不进仓库、不经过对话
- 建议定期更换该 FTP 密码；不要与其他服务复用

若将来主机支持 FTPS，只需把 workflow 中 `protocol: ftp` 改为 `ftps`（显式 FTPS，端口仍 21）或 `ftps-legacy`（隐式，端口 990）。

### 首次部署与验收

推送代码后（或 Actions 页手动 `Run workflow`），首次为全量上传约 **30MB / 267 个文件**，几分钟完成；之后依靠服务器上的 `.ftp-deploy-sync-state.json` 只传变化文件。

逐项验收：

- [ ] `https://infor-ecosystem-open-resources.cuiwenyuan.cn/` 首页打开，样式正常（Roboto 自托管生效、无字体闪烁）
- [ ] 「LN Session 速查」页可搜索，且 `assets/ln-sessions/tf.json` 等 23 个分片 JSON 能加载
- [ ] 二维码图 `assets/wechat/2026-11-04-ln-session/qrcode-card.png` 可访问
- [ ] `sitemap.xml` 中 `<loc>` 全部为 `.cn` 域名，**不含 github.io**
- [ ] 页面源码中无 `fonts.googleapis.com` / `fonts.gstatic.com` / `unpkg.com`
- [ ] `<link rel="canonical">` 指向 `.cn` 域名
- [ ] GitHub Pages 站复查：Google Fonts 与原有外观无变化

可选：把国内站的 `sitemap.xml` 提交到百度搜索资源平台。

### 本地验证命令

```bash
cd C:\Users\Administrator\Documents\InforIndex

# GitHub Pages 站（默认配置）
py -m mkdocs build --strict

# 国内镜像站（独立配置，输出到 site-cn/，已被 .gitignore 排除）
py -m mkdocs build -f mkdocs.cn.yml --strict -d site-cn
```

### 第三方资源许可

| 资源 | 版本 / 来源 | 许可证 | 许可证文件 |
|---|---|---|---|
| Roboto | `@fontsource/roboto@5`（latin woff2） | SIL OFL 1.1 | `docs/assets/fonts/LICENSE-ROBOTO.txt` |
| Roboto Mono | `@fontsource/roboto-mono@5`（latin woff2） | SIL OFL 1.1 | `docs/assets/fonts/LICENSE-ROBOTO-MONO.txt` |
| Mermaid | `mermaid@10` dist | MIT | `docs/assets/javascripts/LICENSE-MERMAID.txt` |

### 常见报错排查

#### `Error: Input required and not supplied: server`

**原因**：`FTP_SERVER`（或其余两个 Secret）在这次 workflow 运行时解析为空字符串。`FTP-Deploy-Action` 把 `server` 声明为必填入参，拿到空值就抛这个错。**属于 Secrets 配置未完成，不是 workflow 或代码问题。**

按上文「6. 添加 GitHub Secrets」补齐 3 个后，到 Actions 页 `Run workflow` 重跑即可。核对要点：

| 检查项 | 正确做法 |
|---|---|
| 名称 | 必须**完全一致且区分大小写**：`FTP_SERVER` / `FTP_USERNAME` / `FTP_PASSWORD` |
| 位置 | 仓库 `Settings → Secrets and variables → Actions → Repository secrets`；**不要建在 Environments secrets**（除非 job 显式声明 `environment:`） |
| 仓库 | 确认是当前这个仓库，不是其他仓库或组织级 Secret |
| `FTP_SERVER` 值 | 只填主机，如 `123.45.67.89` 或 `ftp.cuiwenyuan.cn`；**不带** `ftp://`、路径、端口，值前后不要有空格 |
| 生效时机 | Secret 新建后**已完成的运行不会自动回填**，需重新触发一次 workflow |

> 自 2026-11-07 起 workflow 增加了 `Check FTP secrets` 步骤：Secrets 缺失时 `deploy-cn` 会**跳过上传**，在 Annotations 显示 warning、在 Job Summary 输出中文排查清单，job 保持绿色，GitHub Pages 站部署完全不受影响；3 个 Secret 齐全后自动恢复上传。若希望缺失时**直接让 job 失败**，删掉 FTP 部署步骤上的 `if: steps.ftp-check.outputs.skip == 'false'` 即可。

#### `425 Can't open data connection` / 能登录但 LIST、上传超时

FTP 被动模式的数据端口未放行：在阿里云安全组与宝塔防火墙同时放行 TCP `21` + 被动端口段（Pure-FTPd 常见 `39000-40000`）；ECS 在 NAT 后还需在 Pure-FTPd 配置 `ForcePassiveIP` 为公网 IP。详见上文「放行 FTP 端口」。
