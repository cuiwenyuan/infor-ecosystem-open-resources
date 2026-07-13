---
title: "Infor LN 授权与 Product ID 速查 - Infor 生态开放资源导航站"
description: "Infor LN 的 License Product ID（授权代码）速查表，整理在 Solution License Manager (SLM) 中注册的授权级别、授权类型、编号规律与对应关系，支持搜索与筛选。"
---

# Infor LN 授权与 Product ID 速查

> 在 Infor LN 中，**Product ID 指的是授权 / 许可代码**——即在 **Infor Solution License Manager (SLM)** 中注册的**数字编号**，用于标识一个被授予许可的产品、组件或功能。它定义了用户的**授权级别**：该组件以何种许可类型（并发用户 / 命名用户 / 服务器等）被授权使用。
>
> 例如：要在 LN Studio 中做开发，必须在 SLM 中注册 **Product ID 10146（LN Development）** 的开发授权。
>
> 本页整理 LN 开发与运维中常见的 Product ID 及其授权对应关系，并支持**搜索与分类筛选**，方便快速定位所需的授权代码。

!!! info "使用说明"
    下方「Product ID 速查表」支持：① 在搜索框输入任意关键字（Product ID、产品名、描述、分类均可）实时过滤；② 按「分类」下拉框筛选。表格可横向滚动。

!!! warning "准确性与来源提示"
    Infor **不公开完整**的 Product ID 清单；完整清单随 LN / Enterprise Server 版本与所购组件不同而变化，且需通过 Infor Support Portal 的 SLM 界面查看（见第三节）。下表汇总自 **Infor 官方文档与发布说明中公开可查** 的 Product ID（LN Studio 前提条件、Enterprise Server 技术说明、SLM 维护许可说明等），主要用于开发与运维参考。具体贵司环境的授权请以 SLM 实际许可证文件为准。

---

## 一、什么是 Product ID / 授权级别

- **Product ID**：SLM 中标识一个授权产品的数字代码（如 `10146`、`7056`、`10365`）。
- **授权级别**：每个 Product ID 对应一个产品 / 组件，并按某种 **License Type（授权类型）** 被授权；SLM 依据许可证文件中的数量限制校验每次请求。
- **SLM（Solution License Manager）**：Infor 统一的中央许可证管理器，可为多种 Infor 产品提供许可，无需为每个产品单独安装许可证管理器。

---

## 二、授权类型（License Type）

SLM 支持的授权类型决定了"按什么维度计数 / 锁定"：

| 授权类型 | 说明 |
|----------|------|
| **Concurrent User（并发用户）** | 一组并发用户可使用的授权池 |
| **Named User（命名用户）** | 一组特定命名用户可使用的授权池 |
| **Server（服务器）** | 节点锁定，限定特定服务器 / 桌面计算机池 |
| **Instance（实例）** | 实例锁定，限定特定命名实例池（SLM 2.5 起通过服务器许可登记） |
| **Desktop（桌面）** | 节点锁定，将一组应用程序绑定到特定桌面计算机池 |

> 一个 Product ID 适用哪些授权类型，由 Infor 定价策略（SLSA）决定，具体以许可证文件为准。

---

## 三、如何查询完整的 Product ID 清单

官方不提供一次性公开列表。查看路径（来自 Infor 文档）：

1. 登录 **Infor Support Portal**（Infor Xtreme）。
2. 依次进入：**Resources → Request a Software Key → License Key Forms → Infor BAAN / SLM**。
3. 在页面底部选择 **Infor License Manager (SLM)**，点击 **Information**。
4. 在底部选择 **Infor ERP LN**，点击 **Information** → 显示各产品的 **License Type 与 Product ID** 对照表。

> 参考：Infor LN 文档「SLM product IDs」与「License LN」章节均指向上述操作。

---

## 四、Product ID 速查表（搜索 / 筛选）

<div class="pid-toolbar">
  <input type="text" id="pid-search" class="pid-input" placeholder="🔍 搜索 Product ID / 产品名 / 描述 / 分类…" aria-label="搜索 Product ID">
  <select id="pid-category" class="pid-select" aria-label="按分类筛选"><option value="">全部分类</option></select>
  <span class="pid-count" id="pid-count"></span>
</div>

<table id="pid-table" class="pid-table">
<thead><tr><th>Product ID</th><th>产品 / 组件</th><th>分类</th><th>授权类型</th><th>描述 / 授权范围</th><th>备注</th></tr></thead>
<tbody>
<tr><td><code>10056</code></td><td>Infor LN</td><td>核心应用</td><td>按合同</td><td>LN ERP 基础产品许可（主产品之一）</td><td>—</td></tr>
<tr><td><code>7114</code></td><td>Infor LN (2)</td><td>核心应用</td><td>按合同</td><td>LN 附加产品许可</td><td>—</td></tr>
<tr><td><code>7115</code></td><td>Infor LN (3)</td><td>核心应用</td><td>按合同</td><td>LN 附加产品许可</td><td>—</td></tr>
<tr><td><code>7116</code></td><td>Infor LN (4)</td><td>核心应用</td><td>按合同</td><td>LN 附加产品许可</td><td>—</td></tr>
<tr><td><code>10896</code></td><td>Infor LN Service</td><td>核心应用</td><td>按合同</td><td>LN Service 产品许可</td><td>—</td></tr>
<tr><td><code>7117</code></td><td>Infor LN Service (2)</td><td>核心应用</td><td>按合同</td><td>LN Service 附加许可</td><td>—</td></tr>
<tr><td><code>10146</code></td><td>LN Development（LN Studio 开发许可）</td><td>开发</td><td>开发授权</td><td>创建 / 修改 表、域、UI 脚本、函数、库；修改并生成 Business Interface 实现</td><td>运行 LN Studio 必须具备；用户常见示例"开发权限 Product ID = 10146"</td></tr>
<tr><td><code>7105</code></td><td>Business Studio</td><td>开发</td><td>开发授权</td><td>建模 / 生成业务对象（BID / BII 等）；导入 BOR / BI</td><td>可由 10146 替代</td></tr>
<tr><td><code>7033</code></td><td>Infor Business Data Entity Modeler</td><td>业务对象</td><td>开发授权</td><td>在 BOR 中建模业务对象（ttadv7500m000）</td><td>亦可由 7105 或 10146 替代</td></tr>
<tr><td><code>7034</code></td><td>Infor Business Data Entity Implementation Generator</td><td>业务对象</td><td>开发授权</td><td>由 BOR 生成 BOL 运行时</td><td>亦可由 7105 或 10146 替代</td></tr>
<tr><td><code>7035</code></td><td>Infor Business Data Entity Repository</td><td>业务对象</td><td>运行授权</td><td>运行时从 BOR 检索元数据（BOL-based BOI）</td><td>仅 BOR 类业务对象相关</td></tr>
<tr><td><code>7013</code></td><td>Adapter for LN（Open Architecture Adapter 2.6 for LN）</td><td>集成/适配器</td><td>运行授权</td><td>运行时调用 BDE / BOD 业务对象（旧版）</td><td>旧版；如已持有则无需新许可</td></tr>
<tr><td><code>7056</code></td><td>Adapter for LN（Open Architecture Adapter 2.7 / Integration 6.2 / ION LN Adapter）/ Infor LN Connector for Web Services</td><td>集成/适配器</td><td>Server license</td><td>运行时调用业务对象；Web Services 连接器</td><td>新版适配器，替代 7013</td></tr>
<tr><td><code>7046</code></td><td>Connector for JDBC</td><td>集成/适配器</td><td>运行授权</td><td>使用主页（Homepages）所需</td><td>—</td></tr>
<tr><td><code>10996</code></td><td>Enterprise Server</td><td>企业服务器</td><td>运行授权</td><td>运行 Enterprise Server 所需</td><td>—</td></tr>
<tr><td><code>10365</code></td><td>Infor365 Maintenance Contract（维护合同）</td><td>维护</td><td>Concurrent User（qty 1）</td><td>维护许可；校验所装补丁是否在合同期内</td><td>必须保留该条目即使到期；end-date = 维护合同到期日</td></tr>
</tbody>
</table>

<script>
(function () {
  function initPidFilter() {
    var search = document.getElementById('pid-search');
    var cat = document.getElementById('pid-category');
    var table = document.getElementById('pid-table');
    var count = document.getElementById('pid-count');
    if (!search || !cat || !table) return;
    var tbody = table.tBodies[0];
    if (!tbody) return;
    var rows = Array.prototype.slice.call(tbody.rows);
    var cats = {};
    rows.forEach(function (r) {
      var cell = r.cells[2];
      if (!cell) return;
      var c = cell.textContent.trim();
      if (c) cats[c] = true;
    });
    Object.keys(cats).sort(function (a, b) {
      return a.localeCompare(b, 'zh');
    }).forEach(function (c) {
      var o = document.createElement('option');
      o.value = c;
      o.textContent = c;
      cat.appendChild(o);
    });
    function applyFilter() {
      var q = search.value.trim().toLowerCase();
      var c = cat.value;
      var shown = 0;
      rows.forEach(function (r) {
        var text = r.textContent.toLowerCase();
        var matchQ = !q || text.indexOf(q) !== -1;
        var matchC = !c || (r.cells[2] && r.cells[2].textContent.trim() === c);
        var ok = matchQ && matchC;
        r.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      if (count) count.textContent = '共 ' + shown + ' / ' + rows.length + ' 条';
    }
    search.addEventListener('input', applyFilter);
    cat.addEventListener('change', applyFilter);
    applyFilter();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPidFilter);
  } else {
    initPidFilter();
  }
})();
</script>

---

## 五、编号规律观察（非官方，仅供参考）

根据公开文档中出现的 Product ID，可观察到大致区间（**并非严格分层，且随版本变化**）：

| 区间 / 编号 | 类别 |
|------------|------|
| `10056` / `7114`~`7117` / `10896` | 主产品与 LN Service 许可 |
| `10146` / `7105` | 开发类（LN Development / Business Studio） |
| `7033` / `7034` / `7035` | 业务对象类（BOD / BDE Modeler / Generator / Repository） |
| `7013`（旧） / `7056`（新） / `7046` | 适配器 / 集成类（含 JDBC 连接器） |
| `10996` | 企业服务器（Enterprise Server） |
| `10365` | 维护合同（Infor365 Maintenance Contract） |

> 结论：编号仅作识别用途，授权含义以 SLM 中该 Product ID 关联的 License Type 与数量为准。

---

## 六、常见混淆澄清

为避免术语混淆，Infor LN 中有 **三种都叫"Product"** 的概念，请注意区分：

| 概念 | 含义 | 是否本页主题 |
|------|------|--------------|
| **License Product ID**（本文） | SLM 中的**授权代码**（如 `10146`），定义授权级别 | ✅ 是 |
| **包代码（Package Code）**（如 `tccom` / `tdpur`） | LN 技术架构中的**包 / 表 / 会话前缀** | ❌ 否，参见 [Infor LN 包代码速查](ln-package-codes.md) |
| **Product Type（tdipu001 的 A/M/E/P）** | ERP **物料主数据**的"产品类型"字段（实际 / 制造 / 估算 / 计划） | ❌ 否，与授权无关 |

---

## 七、相关资源

- [Infor LN Studio 前提条件（官方，含 10146 / 7013 / 7056）](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnstudiodg/iex1504268054460.html)
- [SLM 授权与校验（官方）](https://docs.infor.com/ln/10.8/en-us/lnesolh/refesag_op/ttomslm_license_management_and_validation.html)
- [Infor LN 产品总览](ln.md)
- [Infor LN 包代码速查](ln-package-codes.md) — 技术架构包 / 表 / 会话前缀
- [LN Public Interfaces 速查（包代码对应 PI 函数）](../resources/ln-pi-reference.md)

---

**最后更新**：2026-07-13
