---
title: "Infor LN 包代码（Package Code）速查 - Infor 生态开放资源导航站"
description: "Infor LN（源自 Baan）的包代码（Package Code）速查表，涵盖编号规则、分类、描述及与模块、表、会话的对应关系，支持按关键字搜索、按分类与按根包筛选。"
---

# Infor LN 包代码（Package Code）速查

> 在 Infor LN（源自 Baan ERP）中，系统功能按 **Package（包）** 组织，每个包有一个 2~4 字母的 **包代码（Package Code）**——它是 LN **技术架构**中的命名前缀，用于组织表、域、会话与源代码。
>
> 本页整理 LN 常用包代码的**编号规则、分类、描述**及与**模块 / 表 / 会话**的对应关系，并支持**搜索、按分类筛选、按根包筛选**，方便开发与实施时快速定位。

!!! tip "与「授权 Product ID」的区别"
    包代码是**技术命名前缀**（如 `tccom` / `tdpur`），与许可无关；而 [Infor LN 授权与 Product ID](ln-product-ids.md) 页面讲的是 **SLM 中的授权代码**（数字编号，如 `10146`）。两者都被口语称作"Product ID"，请勿混淆。

!!! info "使用说明"
    下方「主速查表」支持三种过滤方式，可叠加使用：① 在搜索框输入任意关键字（包代码、描述、分类、根包均可）实时过滤；② 按「分类」下拉框筛选；③ 按「根包」下拉框筛选（如只看 `td` 分销下的所有子包）。表格可横向滚动。

!!! warning "准确性提示"
    LN 的包代码随版本（10.x）与本地化有所差异。本表聚焦最常用、可跨版本稳定的核心包；贵司实际启用的组件与包代码，请以系统中的 **已实施的软件组件 (`tccom0100s000`)** 与实际 VRC 为准。其中 `qm`（质量）、`ts`（服务）、`fm`（货运）、`tdedi`（EDI）等子包命名在不同 LN 版本间可能略有差异。

---

## 一、编号规则

### 1.1 包代码（Package Code）
- **构成**：`t` + 2~3 个字母，如 `tc`（公共）、`td`（分销）、`ti`（库存）、`wh`（仓储）、`tf`（财务）、`tp`（生产）、`cp`（企业计划）；另有独立根包 `cisli`（统一开票）、`qm`（质量）、`ts`（服务）、`fm`（货运）。
- **子包（Sub-package）**：在根包后追加功能缩写，如 `tdpur`（采购 = td + pur）、`tdsls`（销售 = td + sls）、`tfacp`（应付 = tf + acp）、`tfgld`（总账 = tf + gld）。

### 1.2 表 / 域代码（Table / Domain）
- **表代码** = 子包前缀 + 实体，如 `tccom100`（公司）、`tccom114`（业务伙伴地址）、`tdpur400`（采购订单）、`tdsls400`（销售订单）。
- **域（Domain）代码**常以包缩写开头，如 `tccmp`（公司）、`tcorno`（订单号）、`tcmcs`（MCS 通用域）、`tcwoc`（部门）。

### 1.3 会话代码（Session）
- **格式**：`<子包><4位数字><m|s><3位序号>`，例如：

| 会话代码 | 含义 |
|----------|------|
| `tdsls1100m000` | 销售报价（维护） |
| `tdsls4100m000` | 销售订单与订单行 |
| `tdsls4201m000` | 审批销售订单 |
| `tdsls4246m000` | 释放到仓储 |
| `whinh4131m000` | 装运（Shipments） |
| `whinh4275m000` | 确认装运 |
| `tfacr2110s000` | 应收匹配 / 关 AR |
| `tfcmg2500m000` | 收款 / 银行事务 |
| `cisli2200m000` | 编制发票 |
| `cisli2400m000` | 打印并过账发票 |
| `tisfc0101m100` | 生产订单 |
| `tisfc0105m000` | 生产订单分配 |
| `qmptc2220m000` | 生成库存检验 |
| `qmptc1101m000` | 检验订单行 |
| `tsmdm1100m100` | 服务部门 |

> 其中 `m` 通常表示多行维护类会话，`s` 表示单行 / 选择类会话。

### 1.4 子系统代码（已实施的软件组件）
LN 通过 **已实施的软件组件 (`tccom0100s000`)** 标识已安装子系统，采用 2 字母代码（详见第三节）。

---

## 二、主速查表（搜索 / 分类 / 根包筛选）

<div class="pid-toolbar">
  <input type="text" id="pid-search" class="pid-input" placeholder="🔍 搜索包代码 / 描述 / 分类 / 根包…" aria-label="搜索包代码">
  <select id="pid-category" class="pid-select" aria-label="按分类筛选"><option value="">全部分类</option></select>
  <select id="pid-root" class="pid-select" aria-label="按根包筛选"><option value="">全部根包</option></select>
  <span class="pid-count" id="pid-count"></span>
</div>

<table id="pid-table" class="pid-table">
<thead><tr><th>包代码</th><th>根包</th><th>分类</th><th>描述</th><th>对应模块 / 典型表·会话</th></tr></thead>
<tbody>
<tr><td><code>tc</code></td><td>tc</td><td>公共</td><td>公共 / 工具根包（公共函数、术语、定制、迁移等）</td><td>tctrm（术语）、tccus（定制）、tcmig（迁移）</td></tr>
<tr><td><code>tccom</code></td><td>tc</td><td>公共</td><td>公司、业务伙伴、地址主数据</td><td>tccom100（公司主数据）、tccom114（业务伙伴地址）</td></tr>
<tr><td><code>tcmcs</code></td><td>tc</td><td>公共</td><td>多公司系统 / 通用主数据（参数、计量单位）</td><td>tcmcs010（系统参数）、tcmcs0565m000（部门）</td></tr>
<tr><td><code>tctrm</code></td><td>tc</td><td>公共</td><td>术语（界面标签 / 多语言文本）</td><td>—</td></tr>
<tr><td><code>tccus</code></td><td>tc</td><td>公共</td><td>定制（用户字段 / 表格扩展）</td><td>—</td></tr>
<tr><td><code>tcmig</code></td><td>tc</td><td>公共</td><td>数据迁移（Migration）</td><td>—</td></tr>
<tr><td><code>td</code></td><td>td</td><td>分销</td><td>分销 / 订单管理根包（Order Management）</td><td>—</td></tr>
<tr><td><code>tdpur</code></td><td>td</td><td>分销</td><td>采购（Purchase）</td><td>tdpor400 / tdpur400（采购订单）、tdpur401、tdpur4100m000</td></tr>
<tr><td><code>tdsls</code></td><td>td</td><td>分销</td><td>销售（Sales）</td><td>tdsls1100m000（报价）、tdsls4100m000（订单）、tdsls4201m000（审批）、tdsls4246m000（释放仓储）</td></tr>
<tr><td><code>tdreq</code></td><td>td</td><td>分销</td><td>采购申请（Requisitioning）</td><td>—</td></tr>
<tr><td><code>tdedi</code></td><td>td</td><td>集成</td><td>电子数据交换（EDI，版本相关）</td><td>采购 / 销售 / 库存 / 开票商务文件转换</td></tr>
<tr><td><code>cisli</code></td><td>cisli</td><td>开票</td><td>统一开票（Centralized Invoicing）</td><td>cisli2200m000（编制发票）、cisli2400m000（打印并过账）</td></tr>
<tr><td><code>ti</code></td><td>ti</td><td>库存</td><td>库存根包（Inventory）</td><td>—</td></tr>
<tr><td><code>tiitm</code></td><td>ti</td><td>库存</td><td>物料主数据（Item）</td><td>tiitm001（物料）</td></tr>
<tr><td><code>ticom</code></td><td>ti</td><td>库存</td><td>物料通用数据</td><td>—</td></tr>
<tr><td><code>timfc</code></td><td>ti</td><td>库存</td><td>物料财务数据</td><td>—</td></tr>
<tr><td><code>tibom</code></td><td>ti</td><td>库存</td><td>物料清单 BOM</td><td>tibom1110m000（BOM 维护）</td></tr>
<tr><td><code>tiedm</code></td><td>ti</td><td>库存</td><td>工程物料清单（Engineering BOM）</td><td>tiedm1110m000</td></tr>
<tr><td><code>tirou</code></td><td>ti</td><td>库存</td><td>工艺流程（Routing）</td><td>tirou1101m000、tirou1102m000</td></tr>
<tr><td><code>ticst</code></td><td>ti</td><td>库存</td><td>物料成本（Item Costing，版本相关）</td><td>—</td></tr>
<tr><td><code>ticpr</code></td><td>ti</td><td>项目</td><td>项目控制（PCS / Project Control；亦见 tipcs）</td><td>包代码因版本而异，以实际为准</td></tr>
<tr><td><code>wh</code></td><td>wh</td><td>仓储</td><td>仓储根包（Warehousing）</td><td>—</td></tr>
<tr><td><code>whwmd</code></td><td>wh</td><td>仓储</td><td>仓储主数据（Warehouse Master Data）</td><td>whwmd2300m000（仓库全方位视图）、whwmd6290m000（检查更正库存）</td></tr>
<tr><td><code>whinh</code></td><td>wh</td><td>仓储</td><td>入库 / 出库处理（Inbound / Outbound）</td><td>whinh2120m000（出库订单行）、whinh2222m000（释放出库）、whinh4131m000（装运）、whinh4275m000（确认装运）、whinh2300m000（仓库经理仪表板）</td></tr>
<tr><td><code>whinp</code></td><td>wh</td><td>仓储</td><td>入库（Inbound）</td><td>—</td></tr>
<tr><td><code>whout</code></td><td>wh</td><td>仓储</td><td>出库（Outbound）</td><td>—</td></tr>
<tr><td><code>whltc</code></td><td>wh</td><td>仓储</td><td>批次控制（Lot Control）</td><td>—</td></tr>
<tr><td><code>tf</code></td><td>tf</td><td>财务</td><td>财务根包（Finance）</td><td>—</td></tr>
<tr><td><code>tfgl</code></td><td>tf</td><td>财务</td><td>总账（General Ledger）</td><td>tfgld（总账）</td></tr>
<tr><td><code>tfacp</code></td><td>tf</td><td>财务</td><td>应付账款（Accounts Payable）</td><td>tfacp2560m000（应付全方位视图）、tfacp2540m000</td></tr>
<tr><td><code>tfacr</code></td><td>tf</td><td>财务</td><td>应收账款（Accounts Receivable）</td><td>tfacr2110s000（匹配 / 关 AR）、tfacr2560m000（应收全方位视图）、tfacr2510m000</td></tr>
<tr><td><code>tfcmg</code></td><td>tf</td><td>财务</td><td>现金管理（Cash Management）</td><td>tfcmg2500m000（收款 / 银行事务）</td></tr>
<tr><td><code>tffam</code></td><td>tf</td><td>财务</td><td>固定资产（Fixed Assets）</td><td>—</td></tr>
<tr><td><code>tp</code></td><td>tp</td><td>生产</td><td>生产根包（Production）</td><td>—</td></tr>
<tr><td><code>tisfc</code></td><td>tp</td><td>生产</td><td>车间控制（Shop Floor Control）</td><td>tisfc0101m100（生产订单）、tisfc0105m000（生产订单分配）</td></tr>
<tr><td><code>tiapl</code></td><td>tp</td><td>生产</td><td>装配（Assembly）</td><td>tiapl1510m000、tiapl2510m000（通用装配 BOM）、tiapl2520m000</td></tr>
<tr><td><code>tppss</code></td><td>tp</td><td>生产</td><td>生产计划（Production Planning / PPS）</td><td>—</td></tr>
<tr><td><code>cp</code></td><td>cp</td><td>计划</td><td>企业计划（Enterprise Planning）根包</td><td>—</td></tr>
<tr><td><code>cprrp</code></td><td>cp</td><td>计划</td><td>需求计划（Requirements Planning / MRP）</td><td>cprrp0740m000（浏览订单挂钩）</td></tr>
<tr><td><code>cpplan</code></td><td>cp</td><td>计划</td><td>主生产计划（MPS）</td><td>—</td></tr>
<tr><td><code>qm</code></td><td>qm</td><td>质量</td><td>质量管理根包（Quality Management）</td><td>qmptc（质量主数据 / 检验）、qmncm（不合格品管理）</td></tr>
<tr><td><code>qmptc</code></td><td>qm</td><td>质量</td><td>质量主数据 / 检验（参数、特性、检测、算法、抽样、检验订单）</td><td>qmptc0100m000（QM 参数）、qmptc0106m000（检测）、qmptc2220m000（生成库存检验）、qmptc2120m000（库存检验）、qmptc1101m000（检验订单行）、qmptc1115m000（检验订单测试数据）、qmptc1202m000（处理检验订单）</td></tr>
<tr><td><code>qmncm</code></td><td>qm</td><td>质量</td><td>不合格品管理（Non-Conformance Management）</td><td>qmncm1100m000（不合格报告）</td></tr>
<tr><td><code>ts</code></td><td>ts</td><td>服务</td><td>服务管理根包（Service Management）</td><td>tsmdm（服务主数据）、tssoc（服务订单）、tsmsc（维护销售订单）、tstdm（售后服务）</td></tr>
<tr><td><code>tsmdm</code></td><td>ts</td><td>服务</td><td>服务主数据（参数、服务部门、服务物料）</td><td>tsmdm0100m000（通用服务参数）、tsmdm1100m100（服务部门）、tsmdm2100m000（服务物料）、tsmdm0130m000（服务类型）</td></tr>
<tr><td><code>tssoc</code></td><td>ts</td><td>服务</td><td>服务订单控制（Service Order Control）</td><td>tssoc0100m000（服务订单管理参数）、tssoc2100m100（服务订单）、tssoc2110m100（服务订单活动）、tssoc2121m000（服务订单材料成本）</td></tr>
<tr><td><code>tsmsc</code></td><td>ts</td><td>服务</td><td>维护销售订单（Maintenance Sales Order）</td><td>tsmsc1110m000（维护销售订单行）</td></tr>
<tr><td><code>tstdm</code></td><td>ts</td><td>服务</td><td>售后服务（After Sales Service）</td><td>tstdm5101m000（售后服务行）</td></tr>
<tr><td><code>fm</code></td><td>fm</td><td>货运</td><td>货运管理根包（Freight Management：运输计划、货运费率、货运订单）</td><td>货运订单（Freight Orders）、货运费率 / 距离表（Freight Tariffs）</td></tr>
</tbody>
</table>

<script>
(function () {
  function initPidFilter() {
    var search = document.getElementById('pid-search');
    var cat = document.getElementById('pid-category');
    var root = document.getElementById('pid-root');
    var table = document.getElementById('pid-table');
    var count = document.getElementById('pid-count');
    if (!search || !cat || !root || !table) return;
    var tbody = table.tBodies[0];
    if (!tbody) return;
    var rows = Array.prototype.slice.call(tbody.rows);
    var cats = {}, roots = {};
    rows.forEach(function (r) {
      var cCell = r.cells[2], rCell = r.cells[1];
      if (cCell) { var c = cCell.textContent.trim(); if (c) cats[c] = true; }
      if (rCell) { var rr = rCell.textContent.trim(); if (rr) roots[rr] = true; }
    });
    function fill(sel, obj) {
      Object.keys(obj).sort(function (a, b) { return a.localeCompare(b, 'zh'); }).forEach(function (k) {
        var o = document.createElement('option');
        o.value = k; o.textContent = k; sel.appendChild(o);
      });
    }
    fill(cat, cats);
    fill(root, roots);
    function applyFilter() {
      var q = search.value.trim().toLowerCase();
      var c = cat.value, rr = root.value;
      var shown = 0;
      rows.forEach(function (row) {
        var text = row.textContent.toLowerCase();
        var matchQ = !q || text.indexOf(q) !== -1;
        var matchC = !c || (row.cells[2] && row.cells[2].textContent.trim() === c);
        var matchR = !rr || (row.cells[1] && row.cells[1].textContent.trim() === rr);
        var ok = matchQ && matchC && matchR;
        row.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      if (count) count.textContent = '共 ' + shown + ' / ' + rows.length + ' 条';
    }
    search.addEventListener('input', applyFilter);
    cat.addEventListener('change', applyFilter);
    root.addEventListener('change', applyFilter);
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

## 三、子系统代码对照（已实施的软件组件）

通过 **已实施的软件组件 (`tccom0100s000`)** 标识公司已安装的子系统，采用 2 字母代码。以下为文档中明确列举的子系统：

| 子系统代码 | 名称 | 说明 |
|-----------|------|------|
| **BP** | 人员管理（Personnel Management） | 人员 / 人力资源相关功能 |
| **TF** | 财务管理（Finance） | 记录财务事务，生成集成事务处理 |
| **CP** | 企业计划（Enterprise Planning） | 企业级计划 / MRP / APS |
| **TD** | 订单管理（Order Management） | 分销相关：销售、采购、仓储订单 |

> 说明：LN 还包含更多子系统（如库存 TI、仓储 WH、生产 TP 等），具体以贵司 `tccom0100s000` 实际配置为准。

---

## 四、包代码 vs 其他"Product"概念

LN 中有三种都涉及"Product"或"编号"的概念，请注意区分：

| 概念 | 含义 | 是否本页主题 |
|------|------|--------------|
| **包代码（Package Code）**（本文，如 `tccom` / `tdpur`） | LN 技术架构中的**包 / 表 / 会话前缀** | ✅ 是 |
| **License Product ID**（如 `10146`） | SLM 中的**授权代码**，定义授权级别 | ❌ 否，参见 [Infor LN 授权与 Product ID](ln-product-ids.md) |
| **Product Type（tdipu001 的 A/M/E/P）** | ERP **物料主数据**的"产品类型"字段（实际 / 制造 / 估算 / 计划） | ❌ 否，与技术架构无关 |

---

## 五、相关资源

- [Infor LN 产品总览](ln.md) — LN 概述、版本历史、技术架构
- [Infor LN 授权与 Product ID](ln-product-ids.md) — SLM 授权代码速查
- [LN Public Interfaces 速查](../resources/ln-pi-reference.md) — 包代码对应的 PI 函数与调用模板
- [LN 4GL 语言基础](../resources/ln-4gl-tips.md) — 4GL 开发入门

---

**最后更新**：2026-07-13
