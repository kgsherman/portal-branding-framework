# Portal Branding Framework

Per-client theming for the ServiceNow Business Portal (Customer Experience Coral base). A client's whole rebrand lives in Section 1 of the theme's CSS Variables.

- **Guide**: [docs/README.md](docs/README.md) - new-client steps, architecture, palette roles, edge cases, maintenance, deployment
- **Token reference**: [docs/token-reference.md](docs/token-reference.md) - all 139 tokens
- **Variable inventory**: [docs/variable-inventory.md](docs/variable-inventory.md) - all 375 Coral variables and where they point
- **Team page**: [docs/brand-tokens.html](docs/brand-tokens.html) (published as a private artifact)

| Folder | Contents |
|---|---|
| `theme/` | The deliverables: CSS Variables template, shared override stylesheet, `PortalBrandTokensUx` script include, UI action scripts |
| `examples/aareal/` | Showcase client theme (Aareal Bank): Section 1, embedded slab font, logo, notes on what lives outside the theme |
| `examples/noris/` | Earlier test theme |
| `docs/` | Documentation and screenshots |
| `tools/` | `docs/build_docs.py` regenerates the generated docs; `embed_font.py` turns WOFF2 files into an embeddable font stylesheet |
| `audit/` | How the framework was derived: notes with every instance record id, scanner/crawler scripts, per-variable usage table |

Regenerate the docs after changing anything in `theme/`:

```bash
python tools/docs/build_docs.py
```
