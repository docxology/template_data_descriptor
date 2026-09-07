# scripts - AGENTS.md

Thin orchestrators only: path bootstrap, logging, and delegated calls into
`src/data_descriptor/` entrypoints. No validation, figure-data preparation,
plotting, checksum, or serialization logic may live here.

## Script inventory

| Script | Pattern | Delegates to | Output |
|--------|---------|--------------|--------|
| `generate_figures.py` | Thin orchestrator | `data_descriptor.rendering.render_descriptor_figures`; `publish_generated_figures` (monorepo `infrastructure.documentation.generated_figure_registry`, fallback `data_descriptor.registry`) | 5 PNGs in `docs/manuscript/figures/`, mirror + `figure_registry.json` in `output/figures/` |
| `generate_release_artifacts.py` | Thin orchestrator | `data_descriptor.descriptor` (`build_descriptor_report`, `build_release_bundle_manifest`, `summarize_field_constraints`) | 3 JSON artifacts in `output/reports/` |

## Contract

- `generate_figures.py` sets `MPLBACKEND=Agg` before pyplot is imported (via
  `data_descriptor.rendering`), calls the tested renderer, and prints the
  written paths. `generate_release_artifacts.py` serializes tested
  report/manifest objects to `output/reports/`. Neither script may implement
  validation logic, compute checksums inline, or hardcode dataset values — every
  number must come from a tested `src/` function.
- Figure rendering (palette, table styling, per-figure layout) lives in
  `src/data_descriptor/rendering.py`; figure-data preparation stays
  matplotlib-free in `src/data_descriptor/figures.py`.
- `generate_figures.py` mirrors the complete PNG set to `output/figures/` and
  writes `figure_registry.json` from `DESCRIPTOR_FIGURE_SPECS`. It validates the
  full source set before copying, so a missing renderer output cannot produce a
  partial registry. In the monorepo it uses the shared
  `infrastructure.documentation.generated_figure_registry` publisher; on a
  standalone clone (no `infrastructure` package) it falls back to the
  byte-compatible `src/data_descriptor/registry.py` implementation so the mirror
  repo stays self-contained.
