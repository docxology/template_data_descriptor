---
name: template-data-descriptor
description: FAIR data descriptor exemplar for schema, provenance, license, and dataset release-readiness validation.
version: 0.1.0
author: docxology
license: MIT
tags: [exemplar, data, fair, provenance]
---

# template-data-descriptor

Load this skill when working on the data descriptor exemplar.

## When to Use

- Creating or reviewing a dataset descriptor project.
- Validating schema, file inventory, provenance, and license boundaries.
- Forking a FAIR data-paper scaffold.

## Quick Reference

```bash
uv run --locked --extra dev pytest --cov=src --cov-fail-under=90
```

## Pitfalls

- Keep claims about the data package, not unsupported scientific effects.
- Do not commit restricted raw data to this public exemplar.
- Regenerate figure provenance through `scripts/generate_figures.py`; it emits
  `output/figures/figure_registry.json` only for a complete five-figure run.
