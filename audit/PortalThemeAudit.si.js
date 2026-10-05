var PortalThemeAudit = Class.create();
PortalThemeAudit.prototype = { initialize: function() {}, type: "PortalThemeAudit" };
PortalThemeAudit.scanScss = (function(){
// ES5 SCSS scanner used inside ServiceNow background scripts (Rhino).
// Returns hardcoded design values (colours, fonts, radii, shadows) with selector context,
// plus theme $variables referenced.
function scanScss(src) {
  src = (src || '') + '';
  // strip block comments, then line comments (not inside url(...) / strings)
  src = src.replace(/\/\*[\s\S]*?\*\//g, '');
  src = src.replace(/(^|[^:"'(])\/\/[^\n]*/g, '$1');
  var stack = [], buf = '', res = { colors: [], fonts: [], radii: [], shadows: [], vars: {}, localVars: {} };
  var NAMED = /\b(white|black|red|green|blue|gray|grey|silver|orange|yellow|purple|pink|navy|teal|maroon|olive|lime|aqua|fuchsia|darkgr[ae]y|lightgr[ae]y|whitesmoke|gainsboro)\b/i;
  var COLOR = /#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)/g;
  function sel() { return stack.join(' > ').replace(/\s+/g, ' ').substr(0, 160); }
  function decl(d) {
    d = d.replace(/\s+/g, ' ').trim();
    if (!d) return;
    var m = d.match(/^(\$[\w-]+)\s*:\s*(.*)$/);
    var vre = /\$[\w-]+/g, v;
    if (m) { res.localVars[m[1]] = m[2].substr(0, 80); var rhs = m[2]; while ((v = vre.exec(rhs))) res.vars[v[0]] = (res.vars[v[0]] || 0) + 1; return; }
    while ((v = vre.exec(d))) res.vars[v[0]] = (res.vars[v[0]] || 0) + 1;
    var ci = d.indexOf(':'); if (ci < 0) return;
    var prop = d.substr(0, ci).trim().toLowerCase(), val = d.substr(ci + 1).trim();
    if (prop.indexOf('@') === 0) return;
    var c; COLOR.lastIndex = 0;
    var found = [], bare = val.replace(/\$[\w-]+/g, '');
    while ((c = COLOR.exec(bare))) { if (!/^rgba?\(\s*,/.test(c[0])) found.push(c[0]); }
    if (prop !== 'font-family' && prop.indexOf('font') !== 0 && prop !== 'content' && prop !== 'transition') { var n = bare.match(NAMED); if (n) found.push(n[0]); }
    for (var i = 0; i < found.length; i++) res.colors.push(sel() + ' | ' + prop + ': ' + val.substr(0, 90));
    if (prop === 'font-family' && val.indexOf('$') < 0 && !/inherit|initial/.test(val)) res.fonts.push(sel() + ' | ' + val.substr(0, 80));
    if (prop.indexOf('radius') > -1 && val.indexOf('$') < 0 && !/^0(px|rem)?( !important)?$/.test(val) && !/^(inherit|initial|unset)/.test(val)) res.radii.push(sel() + ' | ' + prop + ': ' + val);
    if (prop.indexOf('shadow') > -1 && val.indexOf('$') < 0 && !/^none/.test(val)) res.shadows.push(sel() + ' | ' + prop + ': ' + val.substr(0, 90));
  }
  for (var i = 0; i < src.length; i++) {
    var ch = src.charAt(i);
    if (ch === '{') {
      // interpolation #{...}
      if (src.charAt(i - 1) === '#') { var j = src.indexOf('}', i); buf += src.substring(i, j + 1); i = j; continue; }
      stack.push(buf.replace(/\s+/g, ' ').trim()); buf = '';
    } else if (ch === '}') { decl(buf); buf = ''; stack.pop(); }
    else if (ch === ';') { decl(buf); buf = ''; }
    else buf += ch;
  }
  decl(buf);
  return res;
}
return scanScss; })();
PortalThemeAudit.crawl = (function(){
// Crawl the pages + widgets a portal can actually render.
function crawlPortal(PORTAL, menuId, themeId) {
  var pages = {}, queue = [], routedAway = {}, widgets = {};
  var r = new GlideRecord('sp_page_route_map'); r.addActiveQuery(); r.query();
  var routes = [];
  while (r.next()) { var ps = r.portals + ''; if (ps === '' || ps.indexOf(PORTAL) > -1) { routedAway[r.route_from_page.id + ''] = r.route_to_page.id + ''; routes.push(r.route_to_page.id + ''); } }
  function addPage(id, why) {
    if (!id) return; id = id + '';
    if (routedAway[id]) id = routedAway[id];
    if (pages[id]) return;
    var g = new GlideRecord('sp_page'); g.addQuery('id', id); g.query(); if (!g.next()) return;
    pages[id] = { why: why, sys_id: g.getUniqueValue(), css: (g.css + '').length, pub: g['public'] + '' }; queue.push(id);
  }
  var p = new GlideRecord('sp_portal'); p.get(PORTAL);
  ['homepage', 'kb_knowledge_page', 'sc_catalog_page', 'login_page', 'notfound_page'].forEach(function (f) { if (!p[f].nil()) addPage(p[f].id, 'portal.' + f); });
  routes.forEach(function (id) { addPage(id, 'route'); });
  (function menuWalk(parent) {
    var it = new GlideRecord('sp_rectangle_menu_item');
    if (parent) it.addQuery('sp_rectangle_menu_item', parent); else { it.addQuery('sp_rectangle_menu', menuId); it.addNullQuery('sp_rectangle_menu_item'); }
    it.addActiveQuery(); it.query();
    while (it.next()) { if (!it.sp_page.nil()) addPage(it.sp_page.id, 'menu'); var mm = (it.url + '').match(/[?&]id=([\w\-]+)/); if (mm) addPage(mm[1], 'menu'); menuWalk(it.getUniqueValue()); }
  })(null);
  var idre = /[?&]id=([a-z0-9_\-]+)/gi;
  function scanText(t, via) { if (!t) return; var m; idre.lastIndex = 0; while ((m = idre.exec(t)) !== null) addPage(m[1], 'ref:' + via); }
  function addWidget(w, via) {
    var k = w.getUniqueValue();
    if (!widgets[k]) { widgets[k] = { id: w.id + '', name: w.name + '', via: [] }; scanWidget(w); }
    if (widgets[k].via.length < 3 && widgets[k].via.indexOf(via) < 0) widgets[k].via.push(via);
  }
  function scanWidget(w) {
    var srv = w.script + '', tpl = w.template + '', cli = w.client_script + '';
    scanText(tpl + cli + srv + w.option_schema, w.id + '');
    var m, re = /\$sp\.getWidget\(\s*['"]([^'"]+)['"]/g;
    while ((m = re.exec(srv)) !== null) { var e = new GlideRecord('sp_widget'); if (e.get('id', m[1])) addWidget(e, 'embed:' + w.id); }
    var re2 = /<widget\s+id=["']([^"']+)["']/g;
    while ((m = re2.exec(tpl)) !== null) { var e2 = new GlideRecord('sp_widget'); if (e2.get('id', m[1])) addWidget(e2, 'embed:' + w.id); }
    var re3 = /['"](?:widget_id|widget)['"]\s*:\s*['"]([\w\-]+)['"]/g;
    while ((m = re3.exec(srv + cli)) !== null) { var e3 = new GlideRecord('sp_widget'); if (e3.get('id', m[1])) addWidget(e3, 'embed:' + w.id); }
  }
  var th = new GlideRecord('sp_theme'); th.get(themeId);
  [th.header + '', th.footer + ''].forEach(function (s) { var w = new GlideRecord('sp_widget'); if (s && w.get(s)) addWidget(w, 'theme'); });
  var guard = 0;
  while (queue.length && guard++ < 300) {
    var pid = queue.shift();
    var inst = new GlideRecord('sp_instance'); inst.addQuery('sp_column.sp_row.sp_container.sp_page.id', pid); inst.addActiveQuery(); inst.query();
    while (inst.next()) { var w = inst.sp_widget.getRefRecord(); if (w.isValidRecord()) addWidget(w, 'page:' + pid); scanText(inst.widget_parameters + '' + inst.url, pid); }
  }
  return { pages: pages, widgets: widgets };
}
return crawlPortal; })();
