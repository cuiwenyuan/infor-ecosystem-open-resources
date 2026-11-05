# 公众号文章草稿 — LN Session 速查页（2026-11-04）

> **发布状态**：草稿待确认 → 确认后发布到公众号草稿箱
> **配图**：`qrcode-card.png`（二维码卡片）、`qrcode-plain.png`（纯码备用）

---

## 候选标题（三选一，默认 A）

- **A.《查 Session 还在翻官方文档？12,125 条 Infor LN Session 中英速查表，扫码即用》**（✅ 已确认）
- B.《Infor LN 顾问收藏级工具：12,125 条 Session 速查页上线，支持模糊搜索与模块筛选》
- C.《一文搞定 Infor LN Session 查询：23 个包、208 个模块组、中英双语、即搜即达》

**摘要（公众号列表页显示，54 字内）**：
LN Session 数以万计，官方文档查找路径深。我们整理了 12,125 条 Session 中英速查表，支持模糊搜索，扫码即用。

---

## 正文

做 Infor LN 的顾问和开发者，几乎每天都在跟 Session Code 打交道：

配个参数要想「那个维护物料主数据的 session 是 `tiitm0101m000` 还是 `tiitm0107m000`？」；客户现场报错了，要快速定位功能入口；写 4GL 定制，要查标准 session 的编号和用途。

**痛点在于**：LN 的 Session 数以万计，官方文档虽然权威，但查找路径深、全英文界面、在客户现场网络受限时更是抓瞎。国内资料零散，没有一个能"输入关键字马上找到 Session"的地方。

**今天，infor-ecosystem-open-resources 上线了一个专门解决这个问题的页面 —— 「Infor LN Session 速查」。**

### 📊 这个页面收录了什么？

我们基于 Infor 官方文档中心各版本（10.6 / 10.7 / 10.8 / 2024.x Cloud / 2025.x Cloud）的联机帮助与官方 Sitemap，采集整理了 **12,125 条 Session**，覆盖 **23 个包、208 个模块组**：

| 包 | 说明 | 条数 |
|----|------|-----|
| td | 分销（销售/采购/越库/EDI） | 392 |
| tc | 通用数据（物料/伙伴/术语） | 242 |
| ti | 制造（车间/工艺路线/BOM/项目） | 219 |
| wh | 仓储（入库/出库/库存核对） | 116 |
| tp | 项目 | 68 |
| tf | 财务（总帐/应收/应付/现金） | 62 |
| **tt** | **工具（会话管理/表设计器/用户管理）** | **48** |
| cp/ts/dm/fm/ci/bp/qm | 成本/服务/文档/财务模块等 | 152 |

其中 `tt` 工具包收录了开发者最常用的功能：`ttaad2500m000`（维护会话）、`ttaad4100m000`（导出数据字典）、`ttadv1100m000`（维护表）等。

### 🔍 怎么用？

三个核心功能，全部**本页完成，无需跳转**：

**1. 模糊搜索** —— 输入 Session Code 的一部分（如 `tdsls4100`）、中文名（如 `销售订单`）、英文名（如 `purchase`），表格即时过滤。

**2. 包/模块联动筛选** —— 下拉选择包和模块（如 `tf / gld 总帐`），只看该模块的 Session。

**3. 官方文档直达** —— 每一行都有「官方↗」链接，一键打开该 Session 在 docs.infor.com 的完整字段说明，工具栏可切换 10.7 / 10.6 / 10.8 / 2024.x Cloud / 2025.x Cloud 五个官方文档版本。

数据按包分片懒加载，首屏轻快，搜哪个包加载哪个包，手机上也不卡。

### 📱 扫码直达

微信扫描下方二维码，或长按识别，一键打开速查页：

【二维码卡片图 qrcode-card.png】

也可以直接复制链接到微信打开：
`https://cuiwenyuan.github.io/infor-ecosystem-open-resources/resources/ln-sessions/`

### 📚 顺带逛逛：站内还有这些

「**infor-ecosystem-open-resources**」持续收录 Infor 生态的开放资源，近期上线的实用页面：

- **Infor 常见问题 FAQ** —— What is Infor？LN 和 Baan 什么关系？
- **Infor 定价与 TCO 指南** —— 订阅与实施费用区间（第三方口径）
- **Infor 登录指南** —— Ming.le 租户 URL / SSO / 密码重置
- **Infor 顾问职业路径** —— 技能阶梯、认证与中外薪酬行情
- **LN MPS/MRP 规划指南** —— 计划主数据、订单策略与实施避坑
- **长尾关键词清单** —— 1739 条 Infor 相关搜索词

### 🧭 关于 infor-ecosystem-open-resources

这是一个**非官方的 Infor 生态开放资源导航库**，定位很简单：把分散在全网、与 Infor 相关的第三方资源**系统化地收拢到一起**——论坛社区、顾问与实施公司、博客教程、工具插件、培训认证，以及本次的 LN Session 速查、错误码排查、开发手册等实用页面。

整个库基于 MkDocs 构建、托管在 GitHub Pages，全部内容开源，欢迎共建：

`https://github.com/cuiwenyuan/infor-ecosystem-open-resources`

### 最后

这个 Session 速查页会持续扩充（目前已覆盖 10.6 / 10.7 / 10.8 / 2024.x Cloud / 2025.x Cloud 五个官方文档版本）。如果你在用页面时发现某个常用 Session 没被收录，欢迎在 GitHub 仓库提 Issue 告诉我们。

觉得有用的话，**转发给你身边做 Infor LN 的同事和朋友**吧。

---

*infor-ecosystem-open-resources：Infor 生态开放资源导航 · 由崔文远（Troy Cui）维护*
*本文数据更新 2026-11-05，页面地址：https://cuiwenyuan.github.io/infor-ecosystem-open-resources/resources/ln-sessions/*

---

## 发布参数（已确认项）

- **标题**：候选 A（✅ 已确认）
- **作者**：崔文远 Troy Cui
- **摘要**：见上（✅ 已确认）
- **封面图**：`cover-2.35.png`（900×383，2.35:1，✅ 待确认后使用）
- **原文链接**：https://cuiwenyuan.github.io/infor-ecosystem-open-resources/resources/ln-sessions/
