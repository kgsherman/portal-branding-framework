# Variable inventory

Every variable declared by the stock **Customer Experience Coral Theme** (`css_variables`), plus the widget-level variables the framework adds, and where each one now points.

* **live** - read by Bootstrap core, a Coral theme include, the header/footer or an OOTB widget. Mapped in Section 3.
* **legacy** - declared by Coral but read by nothing on the Business Portal (instance-wide search, 2026-10). Kept in Section 4, mapped to a token, so custom widgets that still reference it keep compiling.
* **added** - not declared by Coral; OOTB widgets fall back to a hidden `!default` (often a hardcoded colour) unless the theme sets it.

Usage counts = how often the variable's sentinel value appeared in the compiled CSS of a canary theme (core = `sp-bootstrap-rem.scss`; theme/widgets = theme includes + widget CSS on the public pages; header/footer = header and footer widget CSS). `-` = 0 on those pages; several of those are still used on authenticated pages or by widgets not on the sampled pages, which is why the status column, not the count, is authoritative.

| Variable | Group | Origin | Status | Maps to | Usage (canary hits) |
|---|---|---|---|---|---|
| `$alert-danger-bg` | Alerts & form states | Coral | live | `$ui-danger-bg` | core 2 |
| `$alert-danger-border` | Alerts & form states | Coral | live | `$ui-danger` | core 2 |
| `$alert-danger-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 2 |
| `$alert-info-bg` | Alerts & form states | Coral | live | `$ui-info-bg` | core 2 |
| `$alert-info-border` | Alerts & form states | Coral | live | `$ui-info` | core 2 |
| `$alert-info-message-bg` | Alerts & form states | Coral | live | `$ui-info-bg` | theme/widgets 8 |
| `$alert-info-message-border` | Alerts & form states | Coral | live | `$ui-info` | theme/widgets 8 |
| `$alert-info-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 2, theme/widgets 8 |
| `$alert-padding` | Alerts & form states | Coral | live | `$ui-space-lg` | core 1 |
| `$alert-success-bg` | Alerts & form states | Coral | live | `$ui-success-bg` | core 2 |
| `$alert-success-border` | Alerts & form states | Coral | live | `$ui-success` | core 2 |
| `$alert-success-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 2 |
| `$alert-warning-bg` | Alerts & form states | Coral | live | `$ui-warning-bg` | core 2, theme/widgets 8 |
| `$alert-warning-border` | Alerts & form states | Coral | live | `$ui-warning` | core 2 |
| `$alert-warning-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 2 |
| `$state-danger-bg` | Alerts & form states | Coral | live | `$ui-danger-bg` | core 7 |
| `$state-danger-border` | Alerts & form states | Coral | live | `$ui-danger` | core 10, theme/widgets 16 |
| `$state-danger-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 16 |
| `$state-info-bg` | Alerts & form states | Coral | live | `$ui-info-bg` | core 6, theme/widgets 8 |
| `$state-info-border` | Alerts & form states | Coral | live | `$ui-info` | core 4, theme/widgets 8 |
| `$state-info-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 10, theme/widgets 8 |
| `$state-success-bg` | Alerts & form states | Coral | live | `$ui-success-bg` | core 8 |
| `$state-success-border` | Alerts & form states | Coral | live | `$ui-success` | core 5, theme/widgets 16 |
| `$state-success-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 14 |
| `$state-warning-bg` | Alerts & form states | Coral | live | `$ui-warning-bg` | core 8 |
| `$state-warning-border` | Alerts & form states | Coral | live | `$ui-warning` | core 4 |
| `$state-warning-text` | Alerts & form states | Coral | live | `$ui-status-text` | core 14 |
| `$background-primary` | Backgrounds & borders | Coral | live | `$ui-surface` | core 2, theme/widgets 288, header/footer 5 |
| `$background-secondary` | Backgrounds & borders | Coral | live | `$ui-surface-subtle` | core 4, theme/widgets 17 |
| `$background-tertiary` | Backgrounds & borders | Coral | live | `$ui-surface-strong` | core 1, theme/widgets 16, header/footer 1 |
| `$body-bg` | Backgrounds & borders | Coral | live | `$ui-page-bg` | core 8, theme/widgets 7 |
| `$border` | Backgrounds & borders | Coral | live | `$ui-border-subtle` | theme/widgets 16, header/footer 1 |
| `$border-primary` | Backgrounds & borders | Coral | live | `$ui-border-strong` | core 5, theme/widgets 88 |
| `$border-secondary` | Backgrounds & borders | Coral | live | `$ui-border` | theme/widgets 16, header/footer 2 |
| `$border-tertiary` | Backgrounds & borders | Coral | live | `$ui-border-subtle` | core 1, theme/widgets 183, header/footer 1 |
| `$kb-tile-border` | Backgrounds & borders | Coral | live | `$ui-border-subtle` | theme/widgets 16 |
| `$line-separator-color` | Backgrounds & borders | Coral | live | `$ui-border-subtle` | theme/widgets 8, header/footer 1 |
| `$sp-b-border-color` | Backgrounds & borders | Coral | live | `$ui-border-subtle` | core 6 |
| `$brand-danger` | Brand | Coral | live | `$ui-danger` | core 4 |
| `$brand-info` | Brand | Coral | live | `$ui-info` | core 10 |
| `$brand-primary` | Brand | Coral | live | `$ui-primary` | core 18, theme/widgets 153, header/footer 1 |
| `$brand-primary-darker` | Brand | Coral | live | `$ui-primary-hover` | core 5, theme/widgets 40 |
| `$brand-primary-darkest` | Brand | Coral | live | `$palette-primary-darkest` | - |
| `$brand-primary-lighter` | Brand | Coral | live | `$palette-primary-light` | core 10 |
| `$brand-primary-lightest` | Brand | Coral | live | `$ui-primary-subtle` | core 2, theme/widgets 112 |
| `$brand-success` | Brand | Coral | live | `$ui-success` | core 5 |
| `$brand-warning` | Brand | Coral | live | `$ui-warning` | core 4, theme/widgets 1 |
| `$btn-secondary-color-hover` | Brand | Coral | live | `$ui-primary-hover` | theme/widgets 8 |
| `$danger` | Brand | Coral | live | `$ui-danger` | core 2 |
| `$info` | Brand | Coral | live | `$ui-info` | core 1 |
| `$primary` | Brand | Coral | live | `$ui-primary` | core 7 |
| `$sp-agent-chat-bg` | Brand | Coral | live | `$ui-primary` | core 1 |
| `$success` | Brand | Coral | live | `$ui-success` | core 1 |
| `$warning` | Brand | Coral | live | `$ui-warning` | core 1 |
| `$abbr-border-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-border-subtle` | core 1 |
| `$blockquote-border-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-border-subtle` | core 2 |
| `$blockquote-small-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-text-muted` | core 1 |
| `$breadcrumb-active-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-text` | core 1 |
| `$breadcrumb-bg` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-page-bg` | core 1 |
| `$breadcrumb-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-text-muted` | core 1 |
| `$breadcrumb-padding-horizontal` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-space-lg` | core 1 |
| `$breadcrumb-padding-vertical` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-space-sm` | core 1 |
| `$carousel-indicator-active-bg` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-primary` | core 3 |
| `$code-bg` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-surface-strong` | core 1 |
| `$code-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$palette-danger-dark` | core 1 |
| `$headings-small-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-text-muted` | core 1 |
| `$hr-border` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-border-subtle` | core 1, header/footer 1 |
| `$kbd-bg` | Breadcrumbs, carousel, code, typography details | Coral | live | `$palette-neutral-95` | core 1 |
| `$kbd-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-text-inverse` | core 1 |
| `$page-header-border-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-border-subtle` | core 1 |
| `$pre-bg` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-surface-subtle` | core 1 |
| `$pre-border-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$ui-border-subtle` | core 2 |
| `$pre-color` | Breadcrumbs, carousel, code, typography details | Coral | live | `$palette-neutral-95` | core 1 |
| `$border-tertiary-actionable` | Buttons | Coral | live | `$ui-button-secondary-border` | - |
| `$btn-danger-bg` | Buttons | Coral | live | `$ui-danger` | core 3, header/footer 2 |
| `$btn-danger-border` | Buttons | Coral | live | `$ui-danger` | core 2 |
| `$btn-danger-color` | Buttons | Coral | live | `$ui-text-inverse` | core 6 |
| `$btn-default-bg` | Buttons | Coral | live | `$ui-button-secondary-bg` | core 4 |
| `$btn-default-border` | Buttons | Coral | live | `$ui-button-secondary-border` | core 3 |
| `$btn-default-color` | Buttons | Coral | live | `$ui-button-secondary-text` | core 9, theme/widgets 16 |
| `$btn-font-weight` | Buttons | Coral | live | `$ui-font-weight-strong` | core 1, theme/widgets 2 |
| `$btn-info-bg` | Buttons | Coral | live | `$palette-info-mid` | core 3 |
| `$btn-info-border` | Buttons | Coral | live | `$palette-info-mid` | core 2 |
| `$btn-info-color` | Buttons | Coral | live | `$ui-text` | core 6 |
| `$btn-link-disabled-color` | Buttons | Coral | live | `$ui-text-muted` | core 1 |
| `$btn-primary-bg` | Buttons | Coral | live | `$ui-button-primary-bg` | core 8, theme/widgets 14 |
| `$btn-primary-border` | Buttons | Coral | live | `$ui-button-primary-bg` | core 3, theme/widgets 6 |
| `$btn-primary-color` | Buttons | Coral | live | `$ui-button-primary-text` | core 7, theme/widgets 24 |
| `$btn-success-bg` | Buttons | Coral | live | `$ui-success` | core 3 |
| `$btn-success-border` | Buttons | Coral | live | `$ui-success` | core 2 |
| `$btn-success-color` | Buttons | Coral | live | `$ui-text-inverse` | core 6 |
| `$btn-warning-bg` | Buttons | Coral | live | `$palette-warning-mid` | core 3 |
| `$btn-warning-border` | Buttons | Coral | live | `$palette-warning-mid` | core 2 |
| `$btn-warning-color` | Buttons | Coral | live | `$ui-text` | core 6 |
| `$secondary-button-active-border-color` | Buttons | Coral | live | `$ui-button-secondary-active-border` | theme/widgets 16 |
| `$secondary-button-hover-border-color` | Buttons | Coral | live | `$ui-button-secondary-hover-border` | theme/widgets 16 |
| `$tox-primary-bg` | Buttons | Coral | live | `$ui-button-primary-bg` | theme/widgets 8 |
| `$tox-primary-hover-bg` | Buttons | Coral | live | `$ui-primary-hover` | theme/widgets 48 |
| `$tox-secondary-bg` | Buttons | Coral | live | `$ui-surface` | theme/widgets 8 |
| `$tox-secondary-hover-bg` | Buttons | Coral | live | `$ui-surface-subtle` | theme/widgets 8 |
| `$dropdown-bg` | Dropdowns | Coral | live | `$ui-surface` | core 1 |
| `$dropdown-border` | Dropdowns | Coral | live | `$ui-border-subtle` | core 1 |
| `$dropdown-divider-bg` | Dropdowns | Coral | live | `$ui-border-subtle` | core 1 |
| `$dropdown-fallback-border` | Dropdowns | Coral | live | `$ui-border-subtle` | core 1 |
| `$dropdown-header-color` | Dropdowns | Coral | live | `$ui-text-muted` | core 1 |
| `$dropdown-link-active-bg` | Dropdowns | Coral | live | `$ui-selected` | core 1 |
| `$dropdown-link-active-color` | Dropdowns | Coral | live | `$ui-on-selected` | core 1 |
| `$dropdown-link-color` | Dropdowns | Coral | live | `$ui-text` | core 1 |
| `$dropdown-link-disabled-color` | Dropdowns | Coral | live | `$ui-text-muted` | core 1 |
| `$dropdown-link-hover-bg` | Dropdowns | Coral | live | `$ui-surface-subtle` | core 1 |
| `$dropdown-link-hover-color` | Dropdowns | Coral | live | `$ui-text` | core 1 |
| `$form-label-bg-color` | Forms | Coral | live | `mix(#FFFFFF, $palette-info, 64%)` | theme/widgets 8 |
| `$input-bg` | Forms | Coral | live | `$ui-surface` | core 4 |
| `$input-bg-disabled` | Forms | Coral | live | `$ui-surface-subtle` | core 4 |
| `$input-border` | Forms | Coral | live | `$ui-border-strong` | core 18, theme/widgets 12 |
| `$input-border-focus` | Forms | Coral | live | `$ui-focus` | core 38, theme/widgets 157 |
| `$input-color` | Forms | Coral | live | `$ui-text` | core 3 |
| `$input-color-placeholder` | Forms | Coral | live | `$ui-text-muted` | core 3 |
| `$input-group-addon-bg` | Forms | Coral | live | `$ui-surface-subtle` | core 1 |
| `$input-group-addon-border-color` | Forms | Coral | live | `$ui-border-strong` | core 1 |
| `$legend-border-color` | Forms | Coral | live | `$ui-border-subtle` | core 1 |
| `$legend-color` | Forms | Coral | live | `$ui-text-secondary` | core 1 |
| `$sc-field-error-color` | Forms | Coral | live | `$ui-text-secondary` | - |
| `$sc-reqd-focus-outline` | Forms | Coral | live | `0px solid $ui-primary` | composite |
| `$sc-reqd-focus-outline-offset` | Forms | Coral | live | `0px` | - |
| `$color-darker` | Greys (Bootstrap) | Coral | live | `$palette-neutral-85` | theme/widgets 56 |
| `$color-darkest` | Greys (Bootstrap) | Coral | live | `$palette-neutral-100` | theme/widgets 8 |
| `$color-light` | Greys (Bootstrap) | Coral | live | `$palette-neutral-30` | - |
| `$color-lighter` | Greys (Bootstrap) | Coral | live | `$palette-neutral-10` | - |
| `$gray` | Greys (Bootstrap) | Coral | live | `$palette-neutral-85` | core 1, header/footer 1 |
| `$gray-base` | Greys (Bootstrap) | Coral | live | `$palette-black` | - |
| `$gray-dark` | Greys (Bootstrap) | Coral | live | `$palette-neutral-95` | core 6 |
| `$gray-darker` | Greys (Bootstrap) | Coral | live | `$palette-neutral-100` | core 1, theme/widgets 27 |
| `$gray-light` | Greys (Bootstrap) | Coral | live | `$palette-neutral-70` | core 5 |
| `$gray-lighter` | Greys (Bootstrap) | Coral | live | `$palette-neutral-5` | core 3, theme/widgets 14 |
| `$navbar-default-link-hover-color` | Header (navbar) | Coral | live | `$ui-header-hover-bg` | core 4 |
| `$navbar-height` | Header (navbar) | Coral | live | `$ui-header-height` | core 3 |
| `$navbar-inverse-bg` | Header (navbar) | Coral | live | `$ui-header-bg` | core 1, theme/widgets 16, header/footer 5 |
| `$navbar-inverse-border` | Header (navbar) | Coral | live | `$ui-header-border` | core 3 |
| `$navbar-inverse-brand-color` | Header (navbar) | Coral | live | `$ui-header-text` | core 1 |
| `$navbar-inverse-brand-hover-bg` | Header (navbar) | Coral | live | `transparent` | core 1 |
| `$navbar-inverse-brand-hover-color` | Header (navbar) | Coral | live | `$ui-header-text` | core 1 |
| `$navbar-inverse-color` | Header (navbar) | Coral | live | `$ui-header-text-muted` | core 1 |
| `$navbar-inverse-link-active-bg` | Header (navbar) | Coral | live | `$ui-header-active-bg` | core 3, theme/widgets 48 |
| `$navbar-inverse-link-active-color` | Header (navbar) | Coral | live | `$ui-header-text` | core 3 |
| `$navbar-inverse-link-color` | Header (navbar) | Coral | live | `$ui-header-text` | core 4, theme/widgets 8, header/footer 22 |
| `$navbar-inverse-link-disabled-bg` | Header (navbar) | Coral | live | `transparent` | core 2 |
| `$navbar-inverse-link-disabled-color` | Header (navbar) | Coral | live | `$ui-header-disabled-text` | core 3 |
| `$navbar-inverse-link-hover-bg` | Header (navbar) | Coral | live | `$ui-header-hover-bg` | core 2 |
| `$navbar-inverse-link-hover-color` | Header (navbar) | Coral | live | `$ui-header-text` | core 4, theme/widgets 8, header/footer 18 |
| `$navbar-secondary-color` | Header (navbar) | Coral | live | `$ui-text-muted` | theme/widgets 8 |
| `$sp-logo-margin-x` | Header (navbar) | Coral | live | `$ui-logo-margin-x` | - |
| `$sp-logo-margin-y` | Header (navbar) | Coral | live | `$ui-logo-margin-y` | header/footer 1 |
| `$sp-logo-max-height` | Header (navbar) | Coral | live | `$ui-logo-max-height` | header/footer 1 |
| `$sp-navbar-divider-color` | Header (navbar) | Coral | live | `$ui-subnav-bg` | header/footer 3 |
| `$sp-navbar-height` | Header (navbar) | Coral | live | `$ui-header-height` | - |
| `$sp-tagline-color` | Header (navbar) | Coral | live | `$ui-header-text` | - |
| `$filter-group-and-color` | Links | Coral | live | `$ui-link` | theme/widgets 16 |
| `$filter-group-or-color` | Links | Coral | live | `$ui-filter-or` | theme/widgets 16 |
| `$link-color` | Links | Coral | live | `$ui-link` | core 12, theme/widgets 193 |
| `$link-hover-color` | Links | Coral | live | `$ui-link-hover` | core 4, theme/widgets 96 |
| `$sp-loading-color` | Loaders | Coral | live | `$ui-text` | core 2 |
| `$modal-backdrop-bg` | Modals | Coral | live | `$palette-black` | core 1 |
| `$modal-backdrop-opacity` | Modals | Coral | live | `.5` | core 1 |
| `$modal-content-bg` | Modals | Coral | live | `$ui-surface` | core 1 |
| `$modal-content-border-color` | Modals | Coral | live | `$ui-border-subtle` | core 1 |
| `$modal-content-fallback-border-color` | Modals | Coral | live | `$ui-border-subtle` | core 1 |
| `$modal-footer-border-color` | Modals | Coral | live | `$ui-border-subtle` | core 1 |
| `$modal-header-border-color` | Modals | Coral | live | `$ui-border-subtle` | core 1 |
| `$modal-inner-padding` | Modals | Coral | live | `$ui-space-lg` | core 2 |
| `$modal-title-padding` | Modals | Coral | live | `$ui-space-lg` | core 1 |
| `$nav-disabled-link-color` | Navs, tabs, pills | Coral | live | `$ui-text-muted` | core 1 |
| `$nav-disabled-link-hover-color` | Navs, tabs, pills | Coral | live | `$ui-text-muted` | core 1 |
| `$nav-link-hover-bg` | Navs, tabs, pills | Coral | live | `$ui-surface-subtle` | core 2 |
| `$nav-link-padding` | Navs, tabs, pills | Coral | live | `$ui-space-sm $ui-space-lg` | composite |
| `$nav-pills-active-link-hover-bg` | Navs, tabs, pills | Coral | live | `$ui-selected` | core 1 |
| `$nav-pills-active-link-hover-color` | Navs, tabs, pills | Coral | live | `$ui-on-selected` | core 1 |
| `$nav-tabs-active-link-hover-bg` | Navs, tabs, pills | Coral | live | `$ui-selected` | core 1 |
| `$nav-tabs-active-link-hover-border-color` | Navs, tabs, pills | Coral | live | `$ui-selected` | core 1 |
| `$nav-tabs-active-link-hover-color` | Navs, tabs, pills | Coral | live | `$ui-on-selected` | core 1 |
| `$nav-tabs-border-color` | Navs, tabs, pills | Coral | live | `$ui-border-subtle` | core 2 |
| `$nav-tabs-justified-active-link-border-color` | Navs, tabs, pills | Coral | live | `$ui-selected` | core 2 |
| `$nav-tabs-justified-link-border-color` | Navs, tabs, pills | Coral | live | `transparent` | core 4 |
| `$nav-tabs-link-hover-border-color` | Navs, tabs, pills | Coral | live | `transparent` | core 2 |
| `$now-sp-nass-base-shadow-color` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `#383838` | - |
| `$now-sp-nass-bg-color` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `transparent` | - |
| `$now-sp-nass-color-alert-info-2` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `$ui-info` | - |
| `$now-sp-nass-color-alert-moderate-3` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `#7B56FF` | - |
| `$now-sp-nass-color-background-secondary-actionable` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `$palette-neutral-90` | - |
| `$now-sp-nass-color-neutral-10` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `$palette-neutral-80` | - |
| `$now-sp-nass-color-primary-0` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `$palette-primary-lightest` | - |
| `$now-sp-nass-color-primary-2` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `$palette-primary-dark` | - |
| `$now-sp-nass-color-text-primary-actionable` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `$ui-on-primary` | - |
| `$now-sp-nass-color-text-tertiary` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `$palette-neutral-80` | - |
| `$now-sp-nass-overlay-area-color` | Next-gen AI Search (NASS) - only compiled when AI Search is enabled | Coral | live | `transparent` | - |
| `$pagination-active-bg` | Pagination | Coral | live | `$ui-primary` | core 1 |
| `$pagination-active-border` | Pagination | Coral | live | `$ui-primary` | core 1 |
| `$pagination-active-color` | Pagination | Coral | live | `$ui-on-primary` | core 1 |
| `$pagination-bg` | Pagination | Coral | live | `$ui-surface` | core 3 |
| `$pagination-border` | Pagination | Coral | live | `$ui-border-subtle` | core 2 |
| `$pagination-color` | Pagination | Coral | live | `$ui-link` | core 1 |
| `$pagination-disabled-bg` | Pagination | Coral | live | `$ui-surface` | core 1 |
| `$pagination-disabled-border` | Pagination | Coral | live | `$ui-border-subtle` | core 1 |
| `$pagination-disabled-color` | Pagination | Coral | live | `$ui-text-muted` | core 2 |
| `$pagination-hover-bg` | Pagination | Coral | live | `$ui-surface-subtle` | core 2 |
| `$pagination-hover-border` | Pagination | Coral | live | `$ui-border` | core 1 |
| `$pagination-hover-color` | Pagination | Coral | live | `$ui-link-hover` | core 1 |
| `$badge-active-bg` | Popovers, labels, badges | Coral | live | `$ui-surface` | core 1 |
| `$badge-active-color` | Popovers, labels, badges | Coral | live | `$ui-link` | core 1 |
| `$badge-bg` | Popovers, labels, badges | Coral | live | `$palette-neutral-70` | core 1 |
| `$badge-color` | Popovers, labels, badges | Coral | live | `$ui-text-inverse` | core 1 |
| `$badge-link-hover-color` | Popovers, labels, badges | Coral | live | `$ui-text-inverse` | core 1 |
| `$label-color` | Popovers, labels, badges | Coral | live | `$ui-text` | core 1 |
| `$label-danger-bg` | Popovers, labels, badges | Coral | live | `$ui-danger-bg` | core 1 |
| `$label-default-bg` | Popovers, labels, badges | Coral | live | `$palette-neutral-20` | core 1 |
| `$label-info-bg` | Popovers, labels, badges | Coral | live | `$ui-info-bg` | core 1 |
| `$label-link-hover-color` | Popovers, labels, badges | Coral | live | `$ui-text` | core 1 |
| `$label-primary-bg` | Popovers, labels, badges | Coral | live | `$palette-primary-pale` | core 1 |
| `$label-success-bg` | Popovers, labels, badges | Coral | live | `$ui-success-bg` | core 1 |
| `$label-warning-bg` | Popovers, labels, badges | Coral | live | `$ui-warning-bg` | core 1 |
| `$popover-bg` | Popovers, labels, badges | Coral | live | `$ui-surface` | core 5 |
| `$popover-border-color` | Popovers, labels, badges | Coral | live | `$ui-border-subtle` | core 5 |
| `$popover-fallback-border-color` | Popovers, labels, badges | Coral | live | `$ui-border-subtle` | core 1 |
| `$popover-title-bg` | Popovers, labels, badges | Coral | live | `$ui-surface-subtle` | core 1 |
| `$list-group-active-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-selected` | core 1 |
| `$list-group-active-border` | Progress, list groups, panels, wells | Coral | live | `$ui-selected` | core 1 |
| `$list-group-active-color` | Progress, list groups, panels, wells | Coral | live | `$ui-on-selected` | core 1 |
| `$list-group-active-text-color` | Progress, list groups, panels, wells | Coral | live | `$ui-on-selected` | core 1 |
| `$list-group-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-surface` | core 1 |
| `$list-group-border` | Progress, list groups, panels, wells | Coral | live | `$ui-border-subtle` | core 1 |
| `$list-group-disabled-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-surface-subtle` | core 1 |
| `$list-group-disabled-color` | Progress, list groups, panels, wells | Coral | live | `$ui-text-muted` | core 1 |
| `$list-group-disabled-text-color` | Progress, list groups, panels, wells | Coral | live | `$ui-text-muted` | core 1 |
| `$list-group-hover-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-surface-subtle` | core 1 |
| `$list-group-link-color` | Progress, list groups, panels, wells | Coral | live | `$ui-text` | core 1 |
| `$list-group-link-heading-color` | Progress, list groups, panels, wells | Coral | live | `$ui-text` | core 1 |
| `$list-group-link-hover-color` | Progress, list groups, panels, wells | Coral | live | `$ui-text` | core 1 |
| `$panel-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-surface` | core 7, theme/widgets 36 |
| `$panel-body-padding` | Progress, list groups, panels, wells | Coral | live | `0 $ui-space-xl $ui-space-xl $ui-space-xl` | composite |
| `$panel-default-border` | Progress, list groups, panels, wells | Coral | live | `$ui-border-subtle` | core 4 |
| `$panel-default-heading-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-surface-subtle` | core 2 |
| `$panel-default-text` | Progress, list groups, panels, wells | Coral | live | `$ui-text` | core 2 |
| `$panel-footer-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-surface-subtle` | core 1 |
| `$panel-heading-padding` | Progress, list groups, panels, wells | Coral | live | `$ui-space-xl` | core 22, theme/widgets 8 |
| `$panel-inner-border` | Progress, list groups, panels, wells | Coral | live | `$ui-border-subtle` | core 3 |
| `$panel-primary-text` | Progress, list groups, panels, wells | Coral | live | `$ui-on-primary` | core 9 |
| `$progress-bar-color` | Progress, list groups, panels, wells | Coral | live | `$ui-on-primary` | core 1 |
| `$progress-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-surface-strong` | core 1 |
| `$thumbnail-border` | Progress, list groups, panels, wells | Coral | live | `$ui-border-subtle` | core 2 |
| `$thumbnail-caption-padding` | Progress, list groups, panels, wells | Coral | live | `$ui-space-sm` | core 1 |
| `$thumbnail-padding` | Progress, list groups, panels, wells | Coral | live | `$ui-space-xs` | core 2 |
| `$well-bg` | Progress, list groups, panels, wells | Coral | live | `$ui-page-bg` | core 1 |
| `$well-border` | Progress, list groups, panels, wells | Coral | live | `$ui-border-subtle` | core 1 |
| `$fav-star-color` | Ratings & favourites | Coral | live | `$ui-rating-star` | - |
| `$fav-star-color-off` | Ratings & favourites | Coral | live | `$palette-white` | - |
| `$fav-star-outline` | Ratings & favourites | Coral | live | `-1px 0 $ui-rating-star-outline, 0 1px $ui-rating-star-outline, 1px ...` | composite |
| `$fav-star-outline-color` | Ratings & favourites | Coral | live | `$ui-rating-star-outline` | - |
| `$component-active-bg` | Selection | Coral | live | `$ui-selected` | core 1 |
| `$component-active-color` | Selection | Coral | live | `$ui-on-selected` | - |
| `$select-primary` | Selection | Coral | live | `$ui-selected` | theme/widgets 200 |
| `$select-primary-darker` | Selection | Coral | live | `$ui-selected-strong` | theme/widgets 40 |
| `$border-radius-base` | Shape & elevation | Coral | live | `$ui-radius` | core 35, theme/widgets 32, header/footer 9 |
| `$border-radius-large` | Shape & elevation | Coral | live | `$ui-radius-lg` | core 13, theme/widgets 217 |
| `$border-radius-small` | Shape & elevation | Coral | live | `$ui-radius-sm` | core 10, header/footer 1 |
| `$btn-border-radius-base` | Shape & elevation | Coral | live | `$ui-radius-button` | core 6 |
| `$btn-border-radius-large` | Shape & elevation | Coral | live | `$ui-radius-button-lg` | core 1 |
| `$btn-border-radius-small` | Shape & elevation | Coral | live | `$ui-radius-button-sm` | core 2 |
| `$nav-pills-border-radius` | Shape & elevation | Coral | live | `$ui-radius` | core 1 |
| `$pager-border-radius` | Shape & elevation | Coral | live | `$ui-radius-pill` | core 1 |
| `$panel-border-radius` | Shape & elevation | Coral | live | `$ui-radius-card` | core 2 |
| `$sp-panel-box-shadow` | Shape & elevation | Coral | live | `$ui-shadow-card` | composite |
| `$flex-paperclip-margin-left` | Spacing | Coral | live | `15px` | theme/widgets 8 |
| `$form-group-margin-bottom` | Spacing | Coral | live | `$ui-space-lg` | core 2 |
| `$form-textbox-button-height` | Spacing | Coral | live | `36px` | theme/widgets 24 |
| `$grid-gutter-width` | Spacing | Coral | live | `$ui-grid-gutter` | - |
| `$label-margin-bottom` | Spacing | Coral | live | `$ui-space-xs` | core 1 |
| `$padding-base-horizontal` | Spacing | Coral | live | `$ui-space-lg` | core 9, theme/widgets 7 |
| `$padding-base-vertical` | Spacing | Coral | live | `6px` | core 4, theme/widgets 106 |
| `$padding-large-horizontal` | Spacing | Coral | live | `$ui-space-xl` | core 8 |
| `$padding-large-vertical` | Spacing | Coral | live | `$ui-space-sm` | core 5 |
| `$padding-small-horizontal` | Spacing | Coral | live | `$ui-space-md` | core 8 |
| `$padding-small-vertical` | Spacing | Coral | live | `$ui-space-xs` | core 5 |
| `$padding-xs-horizontal` | Spacing | Coral | live | `$ui-space-sm` | core 1, theme/widgets 24 |
| `$padding-xs-vertical` | Spacing | Coral | live | `$ui-space-xs` | core 1 |
| `$sp-page-padding-bottom` | Spacing | Coral | live | `$ui-page-padding` | core 2 |
| `$sp-page-padding-left` | Spacing | Coral | live | `$ui-page-padding` | core 2, theme/widgets 8 |
| `$sp-page-padding-right` | Spacing | Coral | live | `$ui-page-padding` | core 2 |
| `$sp-page-padding-top` | Spacing | Coral | live | `$ui-page-padding` | core 2 |
| `$sp-space--3xl` | Spacing | Coral | live | `$ui-space-3xl` | theme/widgets 16, header/footer 1 |
| `$sp-space--3xs` | Spacing | Coral | live | `$ui-space-3xs` | theme/widgets 32 |
| `$sp-space--lg` | Spacing | Coral | live | `$ui-space-lg` | core 1, theme/widgets 682, header/footer 26 |
| `$sp-space--md` | Spacing | Coral | live | `$ui-space-md` | theme/widgets 186, header/footer 25 |
| `$sp-space--sm` | Spacing | Coral | live | `$ui-space-sm` | core 1, theme/widgets 191, header/footer 21 |
| `$sp-space--xl` | Spacing | Coral | live | `$ui-space-xl` | core 9, theme/widgets 920, header/footer 6 |
| `$sp-space--xs` | Spacing | Coral | live | `$ui-space-xs` | theme/widgets 205, header/footer 18 |
| `$sp-space--xxl` | Spacing | Coral | live | `$ui-space-xxl` | theme/widgets 48, header/footer 1 |
| `$sp-space--xxs` | Spacing | Coral | live | `$ui-space-xxs` | theme/widgets 200, header/footer 14 |
| `$table-bg` | Tables | Coral | live | `transparent` | core 1 |
| `$table-bg-accent` | Tables | Coral | live | `$ui-surface-subtle` | core 1 |
| `$table-bg-hover` | Tables | Coral | live | `$ui-surface-strong` | core 2 |
| `$table-border-color` | Tables | Coral | live | `$ui-border-subtle` | core 7 |
| `$table-cell-padding` | Tables | Coral | live | `$ui-space-sm` | core 3 |
| `$table-condensed-cell-padding` | Tables | Coral | live | `$ui-space-xs` | core 1 |
| `$text-color` | Text | Coral | live | `$ui-text` | core 11, theme/widgets 110 |
| `$text-muted` | Text | Coral | live | `$ui-text-muted` | core 7, theme/widgets 28, header/footer 1 |
| `$text-primary` | Text | Coral | live | `$ui-text` | core 9, theme/widgets 163 |
| `$text-secondary` | Text | Coral | live | `$ui-text-secondary` | core 3, theme/widgets 69 |
| `$text-tertiary` | Text | Coral | live | `$ui-text-muted` | core 5, theme/widgets 28 |
| `$text-white` | Text | Coral | live | `$ui-text-inverse` | theme/widgets 32 |
| `$font-family-sans-serif` | Typography | Coral | live | `$ui-font-family` | core 3, theme/widgets 8 |
| `$font-size-3xl` | Typography | Coral | live | `ceil(($font-size-base * 2.25))` | - |
| `$font-size-base` | Typography | Coral | live | `$ui-font-size-base` | core 8, theme/widgets 118, header/footer 1 |
| `$font-size-h1` | Typography | Coral | live | `ceil(($font-size-base * 2))` | core 1, theme/widgets 1 |
| `$font-size-h2` | Typography | Coral | live | `ceil(($font-size-base * 1.5))` | core 1, theme/widgets 2 |
| `$font-size-h3` | Typography | Coral | live | `ceil(($font-size-base * 1.25))` | core 1, theme/widgets 1 |
| `$font-size-h4` | Typography | Coral | live | `ceil(($font-size-base * 1.125))` | core 1, theme/widgets 12 |
| `$font-size-h5` | Typography | Coral | live | `$font-size-base` | core 1, theme/widgets 1 |
| `$font-size-h6` | Typography | Coral | live | `ceil(($font-size-base * 0.875))` | core 1 |
| `$font-size-large` | Typography | Coral | live | `ceil(($font-size-base * 1.25))` | core 8, theme/widgets 64, header/footer 5 |
| `$font-size-md` | Typography | Coral | live | `$font-size-base` | theme/widgets 64, header/footer 2 |
| `$font-size-sm` | Typography | Coral | live | `ceil(($font-size-base * 0.938))` | core 1 |
| `$font-size-small` | Typography | Coral | live | `ceil(($font-size-base * 0.875))` | core 12, theme/widgets 243, header/footer 4 |
| `$font-size-xl` | Typography | Coral | live | `ceil(($font-size-base * 1.5))` | theme/widgets 100, header/footer 3 |
| `$font-size-xs` | Typography | Coral | live | `ceil(($font-size-base * 0.75))` | theme/widgets 48, header/footer 4 |
| `$font-size-xxl` | Typography | Coral | live | `ceil(($font-size-base * 1.875))` | core 3, theme/widgets 8 |
| `$font-weight-small` | Typography | Coral | live | `$ui-font-weight-medium` | theme/widgets 24 |
| `$headings-font-family` | Typography | Coral | live | `$ui-font-family-heading` | core 1 |
| `$headings-font-weight` | Typography | Coral | live | `$ui-font-weight-heading` | core 1, theme/widgets 7 |
| `$headings-line-height` | Typography | Coral | live | `$ui-line-height-tight` | core 1, theme/widgets 16 |
| `$line-height-base` | Typography | Coral | live | `$ui-line-height` | core 18, theme/widgets 10 |
| `$line-height-small` | Typography | Coral | live | `$ui-line-height-tight` | core 6 |
| `$now-sp-font-family-sans-serif` | Typography | Coral | live | `$ui-font-family` | core 1 |
| `$input-border-radius` | Shape & elevation | added | added (live) | `$ui-radius-input` | widget-level / hidden default |
| `$input-border-radius-large` | Shape & elevation | added | added (live) | `$ui-radius-input-lg` | widget-level / hidden default |
| `$input-border-radius-small` | Shape & elevation | added | added (live) | `$ui-radius-input-sm` | widget-level / hidden default |
| `$headings-color` | Typography | added | added (live) | `$ui-heading-color` | widget-level / hidden default |
| `$background-button-default` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface-strong` | widget-level / hidden default |
| `$banner-secondary-btn-bgcolor` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `transparent` | widget-level / hidden default |
| `$data-table-selected` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-selected-subtle` | widget-level / hidden default |
| `$default-comment-border-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-border-subtle` | widget-level / hidden default |
| `$kb-attachment-content` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text` | widget-level / hidden default |
| `$kb-attachment-icon-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface-strong` | widget-level / hidden default |
| `$kb-attachment-star-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-rating-star` | widget-level / hidden default |
| `$kb-attachment-star-empty` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$palette-neutral-40` | widget-level / hidden default |
| `$kb-attachment-star-shadow` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-rating-star-outline` | widget-level / hidden default |
| `$kb-attchment-content` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text` | widget-level / hidden default |
| `$kb-border` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-border-subtle` | widget-level / hidden default |
| `$kb-comment-author-link` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text` | widget-level / hidden default |
| `$kb-comment-bg` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface-subtle` | widget-level / hidden default |
| `$kb-comment-disbaled` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text-muted` | widget-level / hidden default |
| `$kb-comment-likes-border` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-border` | widget-level / hidden default |
| `$kb-comment-text-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text-muted` | widget-level / hidden default |
| `$kb-create-comment-bg` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface` | widget-level / hidden default |
| `$kb-helpicon-box-shadow-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-border-strong` | widget-level / hidden default |
| `$kb-icon-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface-strong` | widget-level / hidden default |
| `$kb-reply-btn-bg` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface-subtle` | widget-level / hidden default |
| `$login-btn-bg` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-button-primary-bg` | widget-level / hidden default |
| `$login-btn-border` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-button-primary-bg` | widget-level / hidden default |
| `$login-mask-btn-bg` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface-subtle` | widget-level / hidden default |
| `$note-comment-background-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `rgba($ui-warning-bg, .2)` | widget-level / hidden default |
| `$note-comment-border-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-warning-bg` | widget-level / hidden default |
| `$sc-field-error-text-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text-inverse` | widget-level / hidden default |
| `$sc-label-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text-muted` | widget-level / hidden default |
| `$sp-clear-all-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-primary-hover` | widget-level / hidden default |
| `$sp-faceted-search-interactive-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-link` | widget-level / hidden default |
| `$sp-homepage-bg` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface` | widget-level / hidden default |
| `$sp-list-cell-color-selected` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-text` | widget-level / hidden default |
| `$sp-nav-tabs-active-tab` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-primary` | widget-level / hidden default |
| `$sp-nav-tabs-hover-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-primary` | widget-level / hidden default |
| `$sp-now-tabs-border-color-hover` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-border` | widget-level / hidden default |
| `$sp-now-tabs-color-active` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-selected-strong` | widget-level / hidden default |
| `$sp-now-tabs-color-hover` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-selected` | widget-level / hidden default |
| `$sp-now-tabs-color-selected` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-selected` | widget-level / hidden default |
| `$sp-page-bg` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-surface` | widget-level / hidden default |
| `$sp-sc-category-list-hover-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-primary` | widget-level / hidden default |
| `$sp-search-results-highlight-color` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-highlight-bg` | widget-level / hidden default |
| `$table-heading` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-primary` | widget-level / hidden default |
| `$timeline-badge-success` | Widget-level knobs (OOTB widgets declare these with !default) | added | added (live) | `$ui-success` | widget-level / hidden default |
| `$brand-danger-darker` | Legacy | Coral | legacy | `$palette-danger-dark` | - |
| `$brand-info-darker` | Legacy | Coral | legacy | `$palette-info-dark` | - |
| `$brand-low` | Legacy | Coral | legacy | `#757681` | - |
| `$brand-low-darker` | Legacy | Coral | legacy | `#585961` | - |
| `$brand-moderate` | Legacy | Coral | legacy | `#7B56FF` | - |
| `$brand-moderate-darker` | Legacy | Coral | legacy | `#6245CC` | - |
| `$brand-success-darker` | Legacy | Coral | legacy | `$palette-success-dark` | - |
| `$brand-warning-darker` | Legacy | Coral | legacy | `$palette-warning-dark` | - |
| `$color-accent` | Legacy | Coral | legacy | `$ui-selected` | - |
| `$color-accent-light` | Legacy | Coral | legacy | `$palette-accent-light` | - |
| `$color-accent-lightest` | Legacy | Coral | legacy | `$ui-selected-subtle` | - |
| `$color-blue-dark` | Legacy | Coral | legacy | `#0F55C1` | - |
| `$color-blue-light` | Legacy | Coral | legacy | `#89B7FD` | - |
| `$color-blue-lightest` | Legacy | Coral | legacy | `#C4DBFE` | - |
| `$color-dark` | Legacy | Coral | legacy | `$palette-neutral-80` | - |
| `$color-disabled` | Legacy | Coral | legacy | `$palette-neutral-50` | - |
| `$color-green-dark` | Legacy | Coral | legacy | `#004B2D` | - |
| `$color-grey` | Legacy | Coral | legacy | `#B8BCBC` | - |
| `$color-lightest` | Legacy | Coral | legacy | `$palette-white` | - |
| `$complete` | Legacy | Coral | legacy | `#757681` | - |
| `$container-min-height` | Legacy | Coral | legacy | `420px` | core 1 |
| `$due-later` | Legacy | Coral | legacy | `$ui-success` | - |
| `$due-today` | Legacy | Coral | legacy | `$ui-warning` | - |
| `$error` | Legacy | Coral | legacy | `$ui-danger` | - |
| `$font-size-2xl` | Legacy | Coral | legacy | `ceil(($font-size-base * 1.375))` | - |
| `$font-size-h1-3x` | Legacy | Coral | legacy | `ceil(($font-size-base * 2.812))` | - |
| `$in-progress` | Legacy | Coral | legacy | `$ui-success` | - |
| `$label-success-background` | Legacy | Coral | legacy | `$ui-success-bg` | - |
| `$now-sp-tabs--border-color` | Legacy | Coral | legacy | `$ui-border-subtle` | - |
| `$now-sp-tabs--color--hover` | Legacy | Coral | legacy | `$ui-selected` | - |
| `$now-sp-tabs--selected--background-color` | Legacy | Coral | legacy | `$ui-selected` | - |
| `$now-sp-tabs--selected--color` | Legacy | Coral | legacy | `$ui-selected` | - |
| `$overdue` | Legacy | Coral | legacy | `$ui-danger` | - |
| `$panel-primary` | Legacy | Coral | legacy | `$ui-border-subtle` | - |
| `$preview-outline` | Legacy | Coral | legacy | `#1A4E70` | - |
| `$preview-outline-text-color` | Legacy | Coral | legacy | `#FFFFFF` | - |
| `$progress-bar` | Legacy | Coral | legacy | `$ui-primary` | - |
| `$rp-default-bg` | Legacy | Coral | legacy | `$ui-surface` | - |
| `$select-primary-lighter` | Legacy | Coral | legacy | `$ui-selected-subtle` | - |
| `$sp-body-bg` | Legacy | Coral | legacy | `$ui-page-bg` | - |
| `$sp-nav-subnav` | Legacy | Coral | legacy | `$ui-subnav-bg` | - |
| `$sp-navbar-inverse-bg` | Legacy | Coral | legacy | `$ui-header-bg` | - |
| `$table-hover` | Legacy | Coral | legacy | `$palette-primary-pale` | - |
