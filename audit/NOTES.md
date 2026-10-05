# Audit notes (working file)

## Instance facts (kev)
- Business Portal: sp_portal `f264dbaccbfd52108d3f6a6fc041e4b5`, url `/business_portal`, menu `2adee5ca144eca10f87712d022bf8391` (Portal B2B menu), portal css_variables: `$portal-rem-base-font-size: 100%;`
- Base theme: Customer Experience Coral Theme `60bed96c93131210aa38860754891827` (scope Portal Next Experience Theme), header `portal-coral-header` (45306dec...), footer `portal-next-experience-footer` (5cf9e323...)
- Matching UXF theme: sys_ux_theme `fad87d2ca304121029a4d1aed31e610f` (used for Next Experience web components)
- noris Theme `d71405382beacf54a5feffb86e91bf75` — user's palette prototype, not attached to any portal
- Canary theme (scratch): `2b74c97c2bb3cf10a5feffb86e91bfeb` "zz Theme Lab - Canary"
- Update sets: framework `3da381f82bb3cf10a5feffb86e91bfb4`, scratch `06a381342b7f0350ff68f76a6e91bff0`
- Scratch SI `PortalThemeAudit` (f3b381f82bb3cf10a5feffb86e91bfbc): scanScss(), crawl(portal, menu, theme)

## How the CSS is built
- Core: `/styles/scss/sp-bootstrap-rem.scss?portal_id=..&theme_id=..` — honours ANY theme_id (even as guest). Bootstrap 3 + SP core.
- Theme CSS includes (sp_css): compiled with theme vars, inlined as <style> in page HTML.
- Widget CSS: compiled with the *portal's* theme; returned in /api/now/sp/page JSON. No theme_id override.
- `GlideSCSSCompiler` exists server-side but compile() returns null / compileTheme is access-restricted.

## Theme include hardcodes (static scan)
- portal-next-experience-kb-rem-px-theme: #ddd, #ccc, #0f3f39 (attachment modal drop zone)
- portal-next-experience-rem-px-theme: `lightgray` attachment picker header border; radius 3px
- portal-next-experience-catalogs-theme: font "Lato" !important on .sc-item-description; radius 6px
- portal-coral-common-theme: radius 6px select2 highlight
- portal-coral-knowledge-theme-upgrade: LOCAL REDECLARE `$border-primary: #737F84` + `$link-focus-color: #091F46`; radii .6rem / 4.8px on search bars

## Legacy bugs in Coral css_variables
- `$now-sp-nass-*` lines: `;` inside trailing `//` comment -> declarations run together
- `$navbar-inverse-bg` and `$navbar-inverse-link-hover-color` declared twice, both `!default` -> FIRST wins (2nd block is dead)
- `$sp-nav-subnav: $sp-navbar-divider-color;` referenced before definition

## Core compile canary results (sp-bootstrap-rem)
Colour vars used by core (direct/derived): text-primary(89) text-tertiary(28) text-white(38) text-secondary(4) background-primary/secondary/tertiary, border-primary/secondary/tertiary/tertiary-actionable, brand-primary(51+11 derived) brand-primary-darker/lighter/lightest, brand-danger/info/success/warning, btn-*-bg, code-color, gray-base/darker/dark/gray/light/lighter, input-border-focus(38), label-default-bg, label-primary-bg, link-color, link-hover-color, navbar-default-link-hover-color, navbar-inverse-bg(1st), navbar-inverse-border, navbar-inverse-link-*, popover-border-color, select-primary, sp-loading-color, state-*-bg, state-danger-text
NOT used by core (check includes/widgets): select-primary-lighter/darker, brand-primary-darkest, brand-*-darker, sp-navbar-divider-color, table-hover, brand-moderate, brand-low, color-*, preview-outline*, tox-secondary-hover-bg, fav-star-*, line-separator-color, label-success-background, alert-info-message-*, form-label-bg-color, secondary-button-*, now-sp-nass-*, filter-group-*
Core hardcoded (visible-relevant): .form-control[disabled] bg #dce0e2; .timeline borders #dee5e7; mark #ff0; fieldset #c0c0c0; .sp-ai-tag/.alert-suggestion; sn-mention #c3dff2; .sp-facet-lists .heading #3a3f51 (mobile); drop-zone icon #b6b6b6; otto-onboarding-modal hardcoded Coral teal (#0080a3 family); hopscotch tours #7a828a etc.

## Core non-colour usage (numeric canary)
- Used by core: border-radius-base(63) -large(14) -small(9), btn-font-weight, font-family-sans-serif (body/tooltip/popover), headings-font-family/-weight/-line-height, font-size-base(13), line-height-base(18)/-small, padding-base-vertical, sp-navbar-height (.navbar min-height, .navbar-brand), sp-page-padding-* (body .padding*), sp-space--xs/sm/md/lg/xl (form controls, buttons, tables), now-sp-font-family-sans-serif -> --now-font-family
- NOT used by core: container-min-height, flex-paperclip-margin-left (ticket include), font-weight-small, form-textbox-button-height (include), sp-logo-* (header widget), sp-space--3xs/xxs/xxl/3xl (widgets)

## SCSS -> --now-* bridge (core emits on :root)
Core emits ~150 custom props from theme vars: --now-button--primary/secondary/tertiary--*, --now-text-link--*, --now-tabs--*, --now-pill--*, --now-dropdown-list--*, --now-color_text--primary, --now-color_focus-ring, --now-color_background--primary, --now-assist-selfservice_* (Now Assist), --sp-agent-chat-bg/--sp-agent-hover-color.
Broken/static:
- --now-color_alert--moderate-3, --now-color--neutral-10, --now-color_background--secondary-actionable, --now-color_text--primary-actionable: STATIC (from $now-sp-nass-* which are malformed)
- --now-label-value-inline--color: literal "$now-sp-label-value-inline--color" (platform bug); --now-color_text--tertiary: literal "$now-sp-color-text-tertiary"; --now-button-iconic--bare_tertiary--* literal
- --now-global-border-radius--md / --now-button--border-radius / --now-container--border-radius: static .25rem (ignore $border-radius-base)
- --now-assist-selfservice_bot_bubble_bg_color, _modal_header_bg_color, _hover_bg_multichoice_color, _disabled_input_bg_color, _tooltip_bg_color: static
- --sp-agent-focus-color static 115,115,174

## Instance-wide reference counts
See chat log; summary: vars with 0 refs in any widget/sp_css/page AND not used by core => dead:
$border-tertiary-actionable(only via btn-default-border), $select-primary-lighter, $brand-*-darker (except danger-darker: 2 non-BP), $sp-nav-subnav, $sp-navbar-inverse-bg, $container-min-height, $sp-body-bg, $table-hover, $brand-moderate, $error, $panel-primary, $color-accent-light(est), $color-blue-*, $color-green-dark, $progress-bar, $preview-outline*, $font-size-2xl, $font-size-h1-3x, $now-sp-tabs--*, $sp-agent-chat-bg (core uses? -> --sp-agent-chat-bg comes from brand-primary), $rp-default-bg, $label-success-background, $btn-border-radius-* (Bootstrap 3.3 doesn't have them -> dead!)
Undeclared-in-theme but used by BP widgets: $sp-homepage-bg $brand-primary-dark $panel-border-color $login-btn-bg $login-btn-border $login-mask-btn-bg $input-border-radius $sp-page-bg $sp-avatar-text-color $banner-secondary-btn-bgcolor $primary-icon $sp-nav-tabs-active-tab $sp-sc-accordion-hover $sp-now-tabs-color-* $sp-search-results-highlight-color $sp-faceted-search-interactive-color $selection-primary(-darker) $data-table-selected $sp-list-cell-color-selected $panel-*-heading-bg/-text $tropical-rain $gull-grey $navbar-invese-bg(typo!) $sp-logo-max-width ...

## SCSS compiler = Vaadin Sass (com.vaadin.sass) — capability map (tested in lab 2026-10-05)
OK: variables, !default, nesting/&, @mixin/@include, @function/@return, @if/@else (incl. null, ==, >), @each over a plain list,
    mix(), darken(), lighten(), transparentize(), scale-color(), rgba($hex, a), red()/green()/blue(), hue()/saturation()/lightness(),
    ceil(), math, calc() with #{} interpolation, var(--x, fallback) passthrough, !important with vars, null property values (dropped)
NOT OK: maps (map-get outputs literally), `@each $k, $v in $map` (PARSE ERROR)
On parse error: the WHOLE stylesheet is silently dropped from the page (logged in syslog as com.vaadin.sass ParseException, level 2).
Theme CSS is cached (SPThemeCSSCache): touch the sp_theme (setForceUpdate) after editing an sp_css to see changes.
An error in theme css_variables would break EVERY include + widget (vars are prepended to each compile).

## px -> rem conversion (portal level!)
Every px in theme includes/widgets is post-converted to rem. Divisor = sys_property
`glide.service_portal.resize_text.<url_suffix>.base_font` (default 10!). Business Portal has 16. Also `...<suffix>.enable_rem_conversion=true` (auto-created by BR "Create Or Update Rem Conversion Sys Prop").
=> NEW CLIENT PORTAL GOTCHA: must create `glide.service_portal.resize_text.<suffix>.base_font = 16` or all sizes render 60% too big.
Conversion happens on values (ceil(16px*1.25) -> 1.25rem fine).
`glide.sp.polaris.theme.allowed.portals` only controls which portals may pick the Polaris theme (ref qual) — not needed.

## Lab setup (scratch)
- Lab theme `c1b5c93c2b7f0350ff68f76a6e91bf70` "zz Theme Lab" (Coral copy + zz-theme-lab-scratch 19b5c93c... + zz-t-* feature tests)
- Lab portal `5db5c93c2b7f0350ff68f76a6e91bff6` /theme_lab ; 7 route maps mirrored ; property glide.service_portal.resize_text.theme_lab.base_font=16
- Theme variant "Coral Dark" exists (sp_theme_variant 162dd26d4f513210f4ca7421b1ce0bba) with empty css_variables — not used by BP.

## Instance options with colours (bypass theme)
- Portal Banner instance 7f85b4ae43ca82108d3f8dc226b8f2b6 on portal_b2b_home: heading_color/description_color #10171A (inline ng-style), background_image = db_image business_portal_homepage_banner.svg (gradient image)
- kb_home container: background_image 94e60d4cffd826108647ffffffffff68 (banner-container)
- Form instance 9dbfcec347730200ba13a5554ee490eb css: `.panel-heading{background-color:$primary; color:#ffffff}`
- Footer social icon colour from footer config (social_icons_color)

## PROGRESS (2026-10-05 ~12:55)
Deliverables (local = source of truth, instance in sync by byte length):
- theme/css_variables.template.scss (36670) -> staged on instance as sys_property zz.portal_brand_tokens.stage2
- theme/css_variables.noris.scss (37731) -> APPLIED to noris Theme d71405382beacf54a5feffb86e91bf75 (backup: sys_property zz.portal_brand_tokens.noris_backup_20261005, 22359 chars)
- theme/portal-brand-tokens-overrides.scss (43728) -> sp_css 39fcc9782b37cf10a5feffb86e91bf83 + sp_css_include 010dc9782b37cf10a5feffb86e91bfa4 (created via REST -> Framework update set; later edits via bg script -> Default set: MOVE sys_update_xml at end)
- override include attached (order 1000) to: lab theme, noris theme
Lab portal currently points at noris theme (switch back to lab theme c1b5... for candy tests). Lab theme has CANDY palette in section 1.
Regression (template vs Coral): only intended/sub-perceptual diffs.
Candy audit: public pages (home, login, registration, 404) = 0 offenders.
Hidden platform defaults found & mapped: login-mask-btn #fcfcfc, sp-faceted-search-interactive #1f8476, sp-now-tabs-* #1f8476/#0f4337, data-table-selected #909090, search highlight #ffa, sc-field-error-text #FFFFFF, sp-homepage-bg #fff.
Undefined (dead OOTB rules, left dead): $panel-border-color, $brand-primary-dark, $tropical-rain, $gull-grey, $mesp-*, $selection-primary*, $default, $border-width-xs, $navbar-invese-bg (typo).
Static bundle css_includes_$sp.css: select2, datepicker, slider, skeletons -> overrides C11.
Async placeholders: inline style background #e2e5e7 -> override with !important.
OOTB bug: portal-banner widget CSS `$sp-space--xxs: 2px; !default;` (semicolon before !default -> forced).
TODO: authenticated pages audit (need login), template theme record, docs + screenshots, cleanup scratch + move update xml.

## PROGRESS (2026-10-05 ~13:17) - authenticated sweep done (impersonating Alex Linde, customer_admin)
Candy-clean pages: home(guest+auth), login, registration, 404, kb_home (banner img->hero), kb_search, kb_article (only authored inline spans), sc_home, portal_taxonomy, portal_cases, csm_profile, portal_contacts, install base, sp_search, approvals, my_requests, faqs, sc_cart, csm_get_help form (+open select2), standard_ticket (TinyMCE minor: swatches/disabled glyphs), product_catalog (after UX sync).
Crawler gaps found & fixed: nested rows (sp_row inside sp_column) and ticket_configuration/ticket_tab_configuration widgets.
Edge cases (not themeable by CSS): portal_case_cards state pills (instance option state_highlight_colour JSON, inline JS), KB article inline styles (content), TinyMCE editable iframe, logos/images, select2.png sprite, illustration line art.
NEW deliverables: sys_script_include PortalBrandTokensUx b61595742b734350ff68f76a6e91bf7a (REST, Framework set), sys_ui_action "Sync Next Experience theme" 462559742b734350ff68f76a6e91bf60 (REST + bg update ui16_compatible).
UX sync run: lab -> sys_ux_theme 18351d742b734350ff68f76a6e91bf84 ; noris -> 6e655df82bb7cf10a5feffb86e91bfaf (colors d6655df8..., typo 22655df8...)
Local files: template 37342, noris 38403, overrides 50109, PortalBrandTokensUx.js 18712.

## PROGRESS (2026-10-05 ~13:40) - docs phase
- Token demo screenshots 10-21 in docs/screenshots (lab theme restored to stage2 = template, 37342).
- Regression template vs Coral rerun: 5514/5514 decls, 28 real diffs, all intended (NASS fix, label-default, pager pill, lbf, derived disabled header) + 1-step rgb rounding.
- SI PortalBrandTokensUx: added cloneTheme(src, name) (fields + css/js m2m + ZZ_YY attachments). Local 20902, md5 52735c03... = instance. Tested on template: 15/15 includes; test clone deleted.
- NEW UI action "Clone theme with includes" f23ad9f82bf7cf10a5feffb86e91bfb4 (REST -> Framework set). Local copy theme/ui-actions.js.
- No sp_theme has logo attachments; BP logo comes from sp_portal.logo.
- Fonts: OOTB Lato = base64 woff2 in sp_css portal-next-experience-lato-fonts (736 KB).

## PROGRESS (2026-10-05 ~13:55) - docs done, update sets sorted
- Docs: docs/README.md (guide), docs/token-reference.md (139 tokens, generated), docs/variable-inventory.md (421 rows, generated), docs/brand-tokens.html (offline copy of the artifact page).
- Artifact (private): https://claude.ai/artifact/SGnrCrcTX6FRiehMqqXJxB  (source: scratchpad site/brand-tokens.html; generators in scratchpad: inventory.py, wiring.py, tokenref.py, pagedata.py, page.template.html)
- Update sets: moved 18 framework entries Default -> Framework; 152 lab/scratch entries Default -> scratch set. Removed stale older Framework entries for sp_css 39fc.. and UI action 4625.. (newer ones moved in).
- Deleted unused auto-created duplicate sp_css_include b1fcc978 (+ its 2 update xml).
- LEFT IN DEFAULT: 13 noris entries (sp_theme d714.., m2m include 8eff.., generated UX theme/styles + 8 m2m_theme_style) - user to decide (their set "noris Theme - Business Portal branding (noris.de)" c058cb66 already has older sp_theme_d714 entries); plus not-mine entries (mb_dashboard_stats x8, sn_kmf prop) and reverted polaris property.
- Browser pane ServiceNow session still impersonating alex.linde (sys_unimpersonate.do blocked for customer user; only Logout offered) - user to end.

## 2026-10-05 ~14:00 - moved + decisions
- Project moved from C:\kevin\js\happyplatform\portal-theming to C:\kevin\js\portal-branding-framework (same layout + README.md + tools/docs/).
- Docs generators consolidated into tools/docs/build_docs.py (+ token-content.json, page.template.html); output verified identical to the previous build.
- User decisions: noris theme/records are test-only (leave noris entries in Default, no action); KEEP the lab (portal /theme_lab, lab theme, canary, scratch set records).

## 2026-10-05 ~14:25 - Aareal Bank showcase example
- Brand from aareal-bank.com: navy #002A5F, sky #79BFE8 (CTA, navy bold text, 4px), cream #F6F5EE, sand #EDEBDD, footer shard blues #012C84 #023293 #033CAA #1B52A5; fonts ITC Lubalin Graph (slab headings) + Helvetica Neue; square cards.
- Files: examples/aareal/ (css_variables.aareal.scss md5 BC37CBA6..., aareal-fonts.scss md5 FD987063..., fonts/arvo-400/700.woff2 OFL, aareal-logo-white.svg md5 66195ed4...). User approved downloading Arvo + logo.
- Instance: sp_theme a32169b42b7bcf10a5feffb86e91bf12 (cloned from template), sp_css aareal-fonts 1b5161302b374350ff68f76a6e91bf01 + auto include 5f5161302b374350ff68f76a6e91bf02 (m2m order 95), UX theme c761e1302b374350ff68f76a6e91bfe4. Update set "Portal Brand Tokens - Aareal Bank example" 6ff06d7c2bf34350ff68f76a6e91bf6d (30 entries).
- Instance fetched fonts/logo itself (RESTMessageV2 + saveResponseBodyAsAttachment; global scope: GlideSysAttachment.getBytes + GlideStringUtil.base64Encode - getContentBase64 is undefined in global). saveResponseBodyAsAttachment to ZZ_YYsp_portal fails -> write to sp_portal then change table_name.
- Lab portal NOW SHOWS AAREAL: theme a32169b4..., logo attachment 167169f42b7bcf10a5feffb86e91bf25 (ZZ_YYsp_portal), quick_start_config footer: logo_img_name "/167169f4...iix", org_info Aareal address, copyright "(theme demo)". Originals: theme c1b5c93c..., logo 7818298c..., footer logo business_portal_coral_servicenow_footer_logo.png, org_info ["2225 Lawson Lane,","Santa Clara, CA 95054"], copyright " © ServiceNow. All rights reserved."
- Footer logo/address come from sp_portal.quick_start_config (JSON footer), not portal logo/theme.
- Framework fixes (overrides 51914, md5 028F75B0...): header .sp-loading-indicator -> $ui-header-text; KB .banner-container heading/summary -> $ui-hero-text when hero-bg+text set (nested @if compiles fine); otto modal btn hover -> darken($ui-button-primary-bg,10%).
- Limit found: generated UX theme covers colours + fonts only; macroponent radii/shadows stay Coral.
- Screenshots now at 1152x1068 viewport (pane too narrow for 1200): 30-36 Aareal, 40/42/43/44 stock Coral (lab portal temporarily on Coral). Old 01-06 deleted.

## 2026-10-05 ~15:40 - noris network example rebuilt from scratch + framework v1.1
- User: "delete the current noris example and start from scratch" from noris's real branding. Old examples/noris/css_variables.noris.scss replaced (git history keeps it; user's original css_variables still in property zz.portal_brand_tokens.noris_backup_20261005).
- Sources: noris.de site CSS (vars --noris-primary #244e5c, --noris-secondary #118291, --noris-highlight #9e1946 / hover #7a1336, --noris-light #f4f7f8, petrol-light #f0f7f8, petrol-hover #e0eff1, radius 12px, CTA pills r=50px, promo gradient 135deg #244e5c->#118291, h1-h3 Open Sans 700 uppercase ls 1px), Logo-Nutzungsrichtlinie PDF (download area: black/white SVG logos, min 100px digital, WCAG AA contrast, petrol covers with angled cuts, hexagon line motif), product sheets (petrol tabs, hexagon icons in #bcd5dc), noris CSM portal servicenow.noris.net/csm (light logo bar + petrol menu bar). Tints of noris blue = mix with white in 10% steps (matches the user's earlier style-guide values).
- Framework v1.1 (null/derived by default, Coral and Aareal output unchanged): $ui-subnav-text, $ui-subnav-hover-bg (header widget paints .sub-navbar + its dropdowns with $sp-navbar-divider-color = $ui-subnav-bg but text with $navbar-inverse-link-color; rules in overrides B with .v5ef595c1... to beat the widget's focus outline), $ui-heading-transform, $ui-heading-letter-spacing (body h1/h2/.h1/.h2; hero .description reset). Template 38119 md5 3EFE9353..., overrides 54899 md5 EDF9A0FB..., aareal 39411 md5 2B938830...; patched on instance (template theme 6f3055f4, lab theme c1b5c93c, Aareal a32169b4, overrides 39fcc978) by minimal-hunk scripts with md5 check.
- noris instance: sp_theme d71405382beacf54a5feffb86e91bf75 renamed "noris network Theme (example)", css_variables 42027 md5 3C4D59B1...; sp_css noris-fonts 057339742b7fcf10a5feffb86e91bfb1 (65462, md5 2FC43AC9..., Open Sans variable woff2 300-800 fetched by the instance from gstatic) + auto include 0d7339742b7fcf10a5feffb86e91bfb2, m2m c57339742b7fcf10a5feffb86e91bfbc order 95; UX theme 1dd33db42b7fcf10a5feffb86e91bf09 (styles 49d3f9b4.., ddd33db4..). Old generated UX theme 6e655df8 + 2 styles + 8 m2m deleted (orphaned after the rename; delete records left in Default).
- GOTCHA: m2m_sp_theme_css_include reference field is sp_css_include (not css_include) - a wrong field name silently creates an empty link.
- GOTCHA: footer logo_img_name "/<id>.iix" returns 403 for customers unless the attachment is on ZZ_YYsp_portal; footer logo max-width 100px (trimmed the white logo's viewBox to the mark: 34.7 16.8 566.9 84.2).
- GOTCHA: embed_font.py wrote CRLF on Windows -> now writes bytes with LF. Java strings in bg scripts: use '' + value before .length.
- Lab portal NOW SHOWS NORIS: theme d714.., logo f8b3b5b42b7fcf10a5feffb86e91bf2b (black, ZZ_YYsp_portal), footer logo /96053d382b3b4350ff68f76a6e91bfe2.iix (white, trimmed), org_info noris network AG / Thomas-Mann-Straße 16 – 20 / 90471 Nürnberg, copyright "© 2026 noris network AG (theme demo)". Aareal values for switching back are in examples/aareal/README.md.
- Update sets: new "Portal Brand Tokens - noris network example" 69d2f5f02b7fcf10a5feffb86e91bf30 (30 entries: theme, 16 css m2m incl. the 14 Coral + overrides links moved from Default, noris-fonts sp_css + include, UX theme + 2 styles + 8 m2m_theme_style). Framework/scratch/Aareal sets got the v1.1 entries (stale older duplicates replaced). REST current set for user claude restored to Framework afterwards.
- Screenshots 50-57 (noris home, footer, case, form, kb home, kb article, product catalog, open menu). Mobile checked: menu folds into the white header panel, readable.
- Docs: build_docs.py now compares Coral vs both examples (EXAMPLES list, darken/lighten in the evaluator, url()/rgba($var) resolution); 143 tokens; Aareal differs on 90, noris on 107.
