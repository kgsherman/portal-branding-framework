# Aareal Bank - example client theme

A showcase of what one client's Section 1 can do. The brand was taken from aareal-bank.com (October 2026).

![Aareal home](../../docs/screenshots/30-aareal-home.jpg)

## The brand, and where each part went

| Aareal brand | Where it is set |
|---|---|
| Navy `#002A5F` for brand, links, headings | `$palette-primary`, `$palette-secondary`, `$ui-heading-color` |
| Sky blue `#79BFE8` call to action with bold navy text | `$ui-button-primary-bg`, `$ui-button-primary-text` (hover darkens automatically) |
| Navy header, menu bar and footer | `$ui-header-bg`, `$ui-header-text`; menus, hover states and footer follow |
| Angled "light shard" artwork (four royal blues from their footer SVG) | `$ui-hero-bg`: one hard-stop `linear-gradient(121deg, …)`; reaches the home and knowledge banners |
| Cream `#F6F5EE` and sand `#EDEBDD` surfaces | `$palette-neutral-5`, `-10`; neutrals 20-95 graded from sand into navy with `mix()` |
| Selected state and focus | Royal blues from the artwork: `$palette-accent`, `$palette-focus` |
| Square, flat cards; 4px only on buttons and tags | `$ui-radius-md/-lg: 0px`, `$ui-shadow-card: none` |
| Slab headings (ITC Lubalin Graph) over Helvetica Neue | `$ui-font-family-heading: "Arvo", …` (open-source stand-in), `$ui-font-family: "Helvetica Neue", …` |

Contrast checked: input borders 4.4:1 on white, muted text 8.7:1 on cream, navy on sky blue 7:1, focus ring 7.5:1.

## Files

| File | What it is |
|---|---|
| `css_variables.aareal.scss` | The theme's complete CSS Variables. Only Section 1 differs from `theme/css_variables.template.scss`. |
| `aareal-fonts.scss` | sp_css with Arvo 400/700 embedded as base64 WOFF2 (made with `tools/embed_font.py`). CSS include, order 95. |
| `fonts/arvo-*.woff2` | Arvo, Copyright 2010-2013 Anton Koovit, SIL Open Font License 1.1 |
| `aareal-logo-white.svg` | Aareal's white logo from aareal-bank.com, used on the lab portal only. Trademark of Aareal Bank AG - for demos only. |

## Beyond Section 1

- **Font include** `aareal-fonts` on the theme (order 95).
- **Logo** on the portal record (`sp_portal.logo`). The lab portal uses the white SVG.
- **Footer** logo, address and copyright in the portal record's footer settings (`quick_start_config` > `footer`): `logo_img_name: "/<logo attachment sys_id>.iix"`, `org_info`, `copyright`.
- **Sync Next Experience theme** once, so the Product Catalog and other Next Experience components pick up the navy and the fonts.

## On the kev instance

| Record | sys_id |
|---|---|
| sp_theme *Aareal Bank Theme (example)* | `a32169b42b7bcf10a5feffb86e91bf12` |
| sp_css / include *aareal-fonts* | `1b5161302b374350ff68f76a6e91bf01` / `5f5161302b374350ff68f76a6e91bf02` |
| Generated UX theme | `c761e1302b374350ff68f76a6e91bfe4` |
| Update set *Portal Brand Tokens - Aareal Bank example* | `6ff06d7c2bf34350ff68f76a6e91bf6d` |
| Live on | lab portal `/theme_lab` (`5db5c93c2b7f0350ff68f76a6e91bff6`) |

To put the lab portal back on the plain template: set its theme to *zz Theme Lab* (`c1b5c93c2b7f0350ff68f76a6e91bf70`), its logo to `7818298cffd82210aa38fffffffffff7`, and its footer to `logo_img_name: "business_portal_coral_servicenow_footer_logo.png"`, `org_info: ["2225 Lawson Lane,", "Santa Clara, CA 95054"]`, `copyright: " © ServiceNow. All rights reserved."`.

## Framework fixes this example uncovered

The Coral look never exercised a dark header or a light call-to-action. Building Aareal fixed three things in `portal-brand-tokens-overrides` for every client:

1. Loading dots in the header used body text colour (black on navy). They now use `$ui-header-text`.
2. The knowledge banner took the hero background but kept navy/black text. Its title and counts now follow `$ui-hero-text` when the theme sets `$ui-hero-bg`.
3. The Now Assist onboarding modal's primary-button hover used the dark brand hover behind the CTA text. It now darkens the CTA colour.
