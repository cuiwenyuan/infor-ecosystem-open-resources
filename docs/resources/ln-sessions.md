---
title: Infor LN Session 速查（Session Code 汇总）
description: Infor LN 10.7 全量 Session Code 速查表 - 按 TD 分销 / TF 财务 / TI 制造 / TC 通用 / WH 仓储等包-模块分组，中英双语描述，支持页内搜索定位，附官方文档直达链接。
---

# Infor LN Session 速查

!!! info "数据说明"
    - **数据来源**：Infor 官方文档中心 docs.infor.com 的 LN **10.7** 版 Session 在线帮助页（zh-cn / en-us），页面标题即「描述 (Session Code)」，共 **1299 条**，采集于 **2026-11-04**。
    - **覆盖范围**：优先采集 **TD 分销 / TF 财务 / TI 制造 / TC 通用 / WH 仓储** 五大核心包（BFS 链接扩散自动发现，同时覆盖 cp / ec / tt 等其他包中被引用的 Session）。
    - **版本口径**：LN 10.7 官方中文为公开文档中覆盖最全的可用版本（2025.x / 2026.11 新版文档平台已改为内容 ID 结构，不再按 Session Code 组织，故未采用）。Session Code 在 10.x 各版本间高度稳定，可用于 10.3 ~ 10.7 与 CloudSuite Industrial Enterprise (LN) 10.x。
    - **用法**：输入 Session Code（如 `tdsls4100m000`）或中英文关键字（如 `销售订单`、`purchase`）即时过滤；点击「官方」列可在 docs.infor.com 打开该 Session 的完整字段说明。

<style>
/* LN Session 速查表 - 紧凑样式（仅作用于本页） */
.lns-wrap .kw-table { font-size: 12px; }
.lns-wrap .kw-table th { white-space: nowrap; padding: 6px 10px; font-size: 12px; }
.lns-wrap .kw-table td { padding: 3px 10px; vertical-align: top; line-height: 1.45; }
.lns-wrap td.lns-code { white-space: nowrap; }
.lns-wrap td.lns-code code { font-size: 12px; padding: 1px 4px; background: rgba(0,0,0,.04); }
.lns-wrap td.lns-link { white-space: nowrap; }
.lns-wrap .kw-input, .lns-wrap .kw-select { font-size: 12px; }
</style>

<div class="kw-wrap lns-wrap">
  <div class="kw-toolbar">
    <input type="search" id="ss-search" class="kw-input" placeholder="🔍 搜索 Session Code / 中文 / 英文（如 tdsls4100m000、销售订单、purchase）" aria-label="搜索 Session">
    <select id="ss-pkg" class="kw-select" aria-label="按包筛选"></select>
    <select id="ss-mod" class="kw-select" aria-label="按模块筛选"></select>
    <span id="ss-count" class="kw-count"></span>
  </div>
  <div class="kw-scroll">
    <table class="kw-table">
      <thead>
        <tr><th style="width:160px">Session Code</th><th>中文描述</th><th>英文描述</th><th style="width:100px">包/模块</th><th style="width:56px">官方</th></tr>
      </thead>
      <tbody id="ss-body"></tbody>
    </table>
  </div>
</div>

<script>
(function(){
  var INDEX = [{"pkg": "td", "n": 392, "label": "分销管理 (td - Distribution)", "mods": ["cms", "ipu", "isa", "pcg", "pct", "pur", "sls", "smi"]}, {"pkg": "tf", "n": 62, "label": "财务管理 (tf - Financials)", "mods": ["acp", "acr", "bgc", "cmg", "gld"]}, {"pkg": "ti", "n": 219, "label": "制造管理 (ti - Manufacturing)", "mods": ["apl", "asc", "asl", "bom", "cpr", "cst", "edm", "ipd", "mfc", "pcf", "pcs", "rou", "rpt", "sfc", "sub", "trp"]}, {"pkg": "tc", "n": 242, "label": "通用基础 (tc - Common)", "mods": ["bgc", "bod", "ccp", "com", "emm", "fin", "gtc", "ibd", "itr", "lct", "mcs", "mpr", "peg", "ppl", "sec", "stl", "tax", "trm", "uef"]}, {"pkg": "wh", "n": 116, "label": "仓储管理 (wh - Warehousing)", "mods": ["ina", "inh", "inp", "inr", "ltc", "wmd"]}, {"pkg": "bp", "n": 7, "label": "人力管理 (bp - Benefits/People)", "mods": ["mdm", "tmm"]}, {"pkg": "ci", "n": 11, "label": "开票管理 (ci - Invoicing)", "mods": ["sli"]}, {"pkg": "cp", "n": 44, "label": "物料计划 (cp - Item Planning)", "mods": ["com", "dsp", "pat", "rao", "rmp", "rpd", "rrp", "vmi"]}, {"pkg": "dm", "n": 21, "label": "文档管理 (dm - Document Management)", "mods": ["com", "sys"]}, {"pkg": "fm", "n": 20, "label": "食品行业管理 (fm - Food Management)", "mods": ["fmd", "foc", "frc", "lbd"]}, {"pkg": "qm", "n": 5, "label": "质量管理 (qm - Quality Management)", "mods": ["ncm", "ptc"]}, {"pkg": "tp", "n": 68, "label": "项目分包 (tp - Project (Baan))", "mods": ["ctm", "est", "pdm", "pin", "ppc", "pss", "ptc"]}, {"pkg": "ts", "n": 44, "label": "企业服务 (ts - Enterprise Server / BSMS)", "mods": ["bsc", "cfg", "clm", "ctm", "epp", "mdm", "msc", "soc", "spc", "wcs"]}, {"pkg": "tt", "n": 48, "label": "系统工具 (tt - Tools)", "mods": ["aad", "adv", "ams", "dsk", "gfd", "mig", "mtm", "spt"]}];
  var cache = {};   // pkg -> rows
  var loading = {};
  function base() {
    // 构建 URL: 页面在 /resources/ln-sessions/, JSON 在 /assets/ln-sessions/
    var p = window.location.pathname;
    p = p.replace(/\/index\.html?$/, '/');
    if (!/\/$/.test(p)) p += '/';
    p = p.replace(/[^/]+\/$/, '');
    return p + '../assets/ln-sessions/';
  }
  function loadPkg(pkg, cb) {
    if (cache[pkg]) return cb(cache[pkg]);
    if (loading[pkg]) { loading[pkg].push(cb); return; }
    loading[pkg] = [cb];
    fetch(base() + pkg + '.json').then(function(r){return r.json();}).then(function(rows){
      cache[pkg] = rows;
      (loading[pkg]||[]).forEach(function(f){f(rows);});
      delete loading[pkg];
    }).catch(function(){
      (loading[pkg]||[]).forEach(function(f){f([]);});
      delete loading[pkg];
    });
  }
  function loadAll(cbs) {
    var pkgs = INDEX.map(function(x){return x.pkg;});
    var done = 0, all = [];
    pkgs.forEach(function(p){ loadPkg(p, function(rows){ all = all.concat(rows); if (++done === pkgs.length) cbs(all); }); });
  }
  function esc(s) {
    return String(s || '').replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; });
  }
  var body = document.getElementById('ss-body');
  var searchEl = document.getElementById('ss-search');
  var pkgEl = document.getElementById('ss-pkg');
  var modEl = document.getElementById('ss-mod');
  var countEl = document.getElementById('ss-count');
  var LIMIT = 500, allRows = [];

  // 包下拉
  var opt = document.createElement('option');
  opt.value = ''; opt.textContent = '全部包（' + 1299 + '）';
  pkgEl.appendChild(opt);
  INDEX.forEach(function(x) {
    var o = document.createElement('option');
    o.value = x.pkg; o.textContent = x.label + '（' + x.n + '）';
    pkgEl.appendChild(o);
  });
  function refreshMods() {
    var p = pkgEl.value;
    modEl.innerHTML = '';
    var first = document.createElement('option');
    first.value = ''; first.textContent = '全部模块';
    modEl.appendChild(first);
    INDEX.forEach(function(x) {
      if (p && x.pkg !== p) return;
      x.mods.forEach(function(mo) {
        var o = document.createElement('option');
        o.value = x.pkg + '/' + mo;
        o.textContent = mo.toUpperCase() + '（' + x.pkg + '）';
        modEl.appendChild(o);
      });
    });
  }
  refreshMods();

  function render() {
    var q = (searchEl.value || '').trim().toLowerCase();
    var p = pkgEl.value, m = modEl.value;
    var rows = allRows.filter(function(r) {
      if (p && r.pkg !== p) return false;
      if (m && (r.pkg + '/' + r.mod) !== m) return false;
      if (q) {
        var hit = r.code.toLowerCase().indexOf(q) >= 0
               || (r.zh || '').toLowerCase().indexOf(q) >= 0
               || (r.en || '').toLowerCase().indexOf(q) >= 0;
        if (!hit) return false;
      }
      return true;
    });
    rows.sort(function(a, b) { return a.code < b.code ? -1 : 1; });
    var shown = rows.slice(0, LIMIT);
    countEl.textContent = '匹配 ' + rows.length + ' 条' + (rows.length > LIMIT ? '（显示前 ' + LIMIT + '）' : '');
    var html = [];
    shown.forEach(function(r) {
      html.push('<tr><td class="lns-code"><code>' + esc(r.code) + '</code></td>'
        + '<td>' + esc(r.zh) + '</td>'
        + '<td>' + esc(r.en) + '</td>'
        + '<td>' + esc(r.pkg + '/' + r.mod) + '</td>'
        + '<td class="lns-link"><a href="' + esc(r.url) + '" target="_blank" rel="noopener">官方↗</a></td></tr>');
    });
    body.innerHTML = html.join('') || '<tr><td colspan="5">未找到匹配的 Session</td></tr>';
  }

  var t = null;
  searchEl.addEventListener('input', function() {
    clearTimeout(t); t = setTimeout(render, 180);
  });
  pkgEl.addEventListener('change', function() { refreshMods(); render(); });
  modEl.addEventListener('change', render);

  loadAll(function(rows) { allRows = rows; render(); });
  render();
})();
</script>

---

**最后更新**：2026-11-04
**维护者**：崔文远 Troy Cui
