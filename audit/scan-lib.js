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
