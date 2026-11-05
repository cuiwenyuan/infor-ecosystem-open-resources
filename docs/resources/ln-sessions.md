---
title: Infor LN Session 速查（Session Code 汇总）
description: Infor LN 全版本 Session Code 速查表（10.6 / 10.7 / 10.8 / 2024.x Cloud / 2025.x Cloud）- 12,125 条，按 TD 分销 / TF 财务 / TI 制造 / TC 通用 / WH 仓储等包-模块分组，中英双语描述，页内搜索定位，多版本官方文档直达链接。
---

# Infor LN Session 速查

!!! info "数据说明"
    - **数据来源**：Infor 官方文档中心 docs.infor.com 各版本 Session 在线帮助页与官方 Sitemap，共 **12,125 条**（中文描述 10,626 条），采集于 **2026-11-04**。
    - **覆盖范围**：合并 **10.8 / 2024.x Cloud / 2025.x Cloud** 官方 Sitemap 全量 Session 页 + **10.7 zh-cn** 联机帮助全量采集，覆盖 20+ 包 / 100+ 模块组：TF 财务、TC 通用、TI 制造、TD 分销、WH 仓储、TS 企业服务、TP 项目、CP 物料计划、FM 货运管理、LP 各国本地化、BP 人力管理、EC 电子数据交换、PD 产品开发、QM 质量、CI 开票、DM 文档、TT 系统工具等。
    - **多版本链接**：每条 Session 按官方数据严格标注可用版本 —— **10.7**（zh-cn，主口径）、**10.6**（zh-cn，10.7 验证集）、**10.8**（zh-cn）、**2024.x Cloud**（zh-cn）、**2025.x Cloud**（en-us）。用工具栏「文档版本」切换「官方」列的链接目标；该 Session 在所选版本无文档页时显示「—」。10.5 官方文档库不完整，请从 [10.5 文档库入口](https://docs.infor.com/ln/10.5/zh-cn/lnolh/default.html) 检索。
    - **用法**：输入 Session Code（如 `tdsls4100m000`）或中英文关键字（如 `销售订单`、`purchase`）即时过滤；点击「官方」列打开该 Session 在所选版本的完整字段说明。

<style>
/* LN Session 速查表 - 紧凑样式（仅作用于本页） */
.lns-wrap .kw-table { font-size: 12px; }
.lns-wrap .kw-table th { white-space: nowrap; padding: 6px 10px; font-size: 12px; }
.lns-wrap .kw-table td { padding: 3px 10px; vertical-align: top; line-height: 1.45; }
.lns-wrap td.lns-code { white-space: nowrap; }
.lns-wrap td.lns-code code { font-size: 12px; padding: 1px 4px; background: rgba(0,0,0,.04); }
.lns-wrap td.lns-link { white-space: nowrap; }
.lns-wrap .kw-input, .lns-wrap .kw-select { font-size: 12px; }
.lns-wrap td.lns-en { color: #888; }
</style>

<div class="kw-wrap lns-wrap">
  <div class="kw-toolbar">
    <input type="search" id="ss-search" class="kw-input" placeholder="🔍 搜索 Session Code / 中文 / 英文（如 tdsls4100m000、销售订单、purchase）" aria-label="搜索 Session">
    <select id="ss-pkg" class="kw-select" aria-label="按包筛选"></select>
    <select id="ss-mod" class="kw-select" aria-label="按模块筛选"></select>
    <select id="ss-ver" class="kw-select" aria-label="文档版本">
      <option value="107" selected>10.7 zh-cn</option>
      <option value="2024">2024.x Cloud zh-cn</option>
      <option value="2025">2025.x Cloud en-us</option>
      <option value="108">10.8 zh-cn</option>
      <option value="106">10.6 zh-cn</option>
    </select>
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
  var INDEX = [{"pkg": "td", "n": 1342, "label": "分销管理 (td - Distribution)", "mods": ["bod", "cms", "gen", "ipu", "isa", "pcg", "pct", "pur", "sls", "smi", "sta"]}, {"pkg": "tf", "n": 1766, "label": "财务管理 (tf - Financials)", "mods": ["acp", "acr", "bgc", "bia", "cat", "cmg", "fam", "fbs", "fst", "gld", "tax"]}, {"pkg": "ti", "n": 1299, "label": "制造管理 (ti - Manufacturing)", "mods": ["apl", "asc", "asl", "bod", "bom", "cpr", "cst", "edm", "grt", "ipd", "mfc", "pcf", "pcs", "rou", "rpt", "sch", "sfc", "sub", "trp"]}, {"pkg": "tc", "n": 1654, "label": "通用基础 (tc - Common)", "mods": ["bcm", "bgc", "bod", "ccp", "clb", "cls", "com", "cri", "emm", "fin", "gen", "gtc", "ibd", "itr", "itu", "lct", "mcs", "mpr", "peg", "ppl", "rac", "sec", "spt", "stl", "tax", "trm", "ttm", "uef"]}, {"pkg": "wh", "n": 937, "label": "仓储管理 (wh - Warehousing)", "mods": ["bod", "ina", "inh", "inp", "inr", "ltc", "spt", "wmd"]}, {"pkg": "as", "n": 1, "label": "自动化服务器 (as - Automation Server)", "mods": ["int"]}, {"pkg": "bc", "n": 100, "label": "迁移工具 (bc - Migration Tools)", "mods": ["cnv", "gct", "mcp", "mec", "mtc", "mtd", "mtf", "mtg", "mti", "run", "ttc", "ttf", "tti"]}, {"pkg": "bo", "n": 4, "label": "业务对象文档 (bo - Business Object Documents)", "mods": ["bod"]}, {"pkg": "bp", "n": 123, "label": "人力管理 (bp - Benefits/People)", "mods": ["bod", "mdm", "tmm", "xtm"]}, {"pkg": "br", "n": 60, "label": "仓库移动应用 (br - Warehouse Mobility)", "mods": ["cnd", "inh", "kan", "mcs", "pac", "sfc", "tmm"]}, {"pkg": "ci", "n": 149, "label": "开票管理 (ci - Invoicing)", "mods": ["rrc", "sli"]}, {"pkg": "cp", "n": 268, "label": "物料计划 (cp - Item Planning)", "mods": ["bod", "com", "dsp", "pat", "rao", "rmp", "rpd", "rrp", "vmi", "wlc"]}, {"pkg": "dm", "n": 120, "label": "文档管理 (dm - Document Management)", "mods": ["chm", "com", "doc", "fmg", "qry", "sys"]}, {"pkg": "ec", "n": 341, "label": "电子商务 (ec - Electronic Commerce)", "mods": ["edi"]}, {"pkg": "fm", "n": 235, "label": "货运管理 (fm - Freight Management)", "mods": ["fmd", "foc", "frc", "fri", "lbd", "rpg", "spt"]}, {"pkg": "lp", "n": 330, "label": "本地化法定报表 (lp - Localization)", "mods": ["ago", "arg", "chl", "cze", "esp", "gbr", "gen", "hun", "idn", "ind", "isr", "ita", "kor", "mex", "mys", "nor", "phl", "prt", "rou", "sau", "svk", "tha", "tur"]}, {"pkg": "pd", "n": 516, "label": "产品开发 (pd - Product Development)", "mods": ["adm", "bpn", "cad", "com", "cps", "erp", "exp", "imp", "pdm", "rqm", "snp", "wfl"]}, {"pkg": "pl", "n": 128, "label": "企业计划增强 (pl - Enterprise Planning Plus)", "mods": ["aps", "exp"]}, {"pkg": "qm", "n": 294, "label": "质量管理 (qm - Quality Management)", "mods": ["bod", "cpl", "ncm", "pqm", "ptc", "rca"]}, {"pkg": "tg", "n": 339, "label": "企业建模器 (tg - Enterprise Modeler)", "mods": ["brg", "erm", "wzr"]}, {"pkg": "tp", "n": 999, "label": "项目分包 (tp - Project (Baan))", "mods": ["bod", "ctm", "est", "pdm", "pin", "ppc", "pss", "ptc", "spt"]}, {"pkg": "ts", "n": 1072, "label": "企业服务 (ts - Enterprise Server / BSMS)", "mods": ["acm", "bod", "bsc", "cfg", "clm", "cmm", "ctm", "epp", "mdm", "msc", "sbm", "soc", "spc", "spt", "tdm", "wcs"]}, {"pkg": "tt", "n": 48, "label": "系统工具 (tt - Tools)", "mods": ["aad", "adv", "ams", "dsk", "gfd", "mig", "mtm", "spt"]}];
  var TPL = {
    '106':  'https://docs.infor.com/ln/10.6/zh-cn/lnolh/help/{pkg}/{mod}/{code}.html',
    '107':  'https://docs.infor.com/ln/10.7/zh-cn/lnolh/help/{pkg}/{mod}/{code}.html',
    '108':  'https://docs.infor.com/ln/10.8/zh-cn/lnolh/{pkg}olh/help/{pkg}/{mod}/{code}.html',
    '2024': 'https://docs.infor.com/ln/2024.x/zh-cn/lnolh/{pkg}olh/help/{pkg}/{mod}/{code}.html',
    '2025': 'https://docs.infor.com/ln/2025.x/en-us/lnolh/{pkg}olh/help/{pkg}/{mod}/{code}.html'
  };
  var cache = {}, loading = {};
  function base() {
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
  var verEl = document.getElementById('ss-ver');
  var countEl = document.getElementById('ss-count');
  var LIMIT = 500, allRows = [];

  var opt = document.createElement('option');
  opt.value = ''; opt.textContent = '全部包（' + 12125 + '）';
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
    var p = pkgEl.value, m = modEl.value, ver = verEl.value;
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
    var linked = 0;
    shown.forEach(function(r) {
      if ((',' + (r.av || '') + ',').indexOf(',' + ver + ',') >= 0) linked++;
    });
    countEl.textContent = '匹配 ' + rows.length + ' 条' + (rows.length > LIMIT ? '（显示前 ' + LIMIT + '）' : '');
    var html = [];
    shown.forEach(function(r) {
      var has = (',' + (r.av || '') + ',').indexOf(',' + ver + ',') >= 0;
      var zh = r.zh || r.en || '';
      var en = r.en || '';
      var zhCell = r.zh ? esc(zh) : ('<span class="lns-en">' + esc(en) + ' (EN)</span>');
      var linkCell = has
        ? '<a href="' + esc(TPL[ver].replace('{pkg}', r.pkg).replace('{mod}', r.mod).replace('{code}', r.code)) + '" target="_blank" rel="noopener">官方↗</a>'
        : '<span title="该版本官方库未收录此 Session">—</span>';
      html.push('<tr><td class="lns-code"><code>' + esc(r.code) + '</code></td>'
        + '<td>' + zhCell + '</td>'
        + '<td>' + esc(en) + '</td>'
        + '<td>' + esc(r.pkg + '/' + r.mod) + '</td>'
        + '<td class="lns-link">' + linkCell + '</td></tr>');
    });
    body.innerHTML = html.join('') || '<tr><td colspan="5">未找到匹配的 Session</td></tr>';
  }

  var t = null;
  searchEl.addEventListener('input', function() {
    clearTimeout(t); t = setTimeout(render, 180);
  });
  pkgEl.addEventListener('change', function() { refreshMods(); render(); });
  modEl.addEventListener('change', render);
  verEl.addEventListener('change', render);

  loadAll(function(rows) { allRows = rows; render(); });
  render();
})();
</script>

---

**最后更新**：2026-11-04
**维护者**：崔文远 Troy Cui
