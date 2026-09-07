# scripts - template_data_descriptor

Thin orchestrators. All computation is delegated to `src/data_descriptor/`; these
scripts only bootstrap paths, invoke module entrypoints, and print output paths.

Use the monorepo pipeline scripts from the repository root for normal
test/render stages. Two project-local scripts are provided:

| Script | Purpose | Delegates to | Command |
|--------|---------|--------------|---------|
| `generate_figures.py` | Render the five manuscript figures, mirror them to `output/figures/`, write `figure_registry.json` | `data_descriptor.rendering.render_descriptor_figures` + a `publish_generated_figures` publisher | `uv run python projects/templates/template_data_descriptor/scripts/generate_figures.py` |
| `generate_release_artifacts.py` | Create descriptor-review artifacts under `output/reports/` | `data_descriptor.descriptor` reporters | `uv run python projects/templates/template_data_descriptor/scripts/generate_release_artifacts.py` |

## `generate_figures.py`

Renders the five manuscript figures into `docs/manuscript/figures/` from
`data/example_descriptor.json` and the fixture bytes (schema overview, file
inventory, provenance flow, quality gate, checksum verification):

```bash
uv run python projects/templates/template_data_descriptor/scripts/generate_figures.py
```

Module logic:

- `src/data_descriptor/rendering.py` — all matplotlib rendering (palette, table styling, per-figure layout)
- `src/data_descriptor/figures.py` — plot-ready data preparers and figure provenance specs
- `src/data_descriptor/verification.py` — descriptor↔file byte checks feeding the verification figure

Outputs:

- `docs/manuscript/figures/*.png` — the five embedded manuscript figures
- `output/figures/figure_registry.json` — provenance registry; the complete PNG set is mirrored to `output/figures/`

## `generate_release_artifacts.py`

Creates deterministic descriptor-review artifacts under `output/reports/`:
descriptor readiness report, metadata-only release bundle manifest, and
field-constraint summary:

```bash
uv run python projects/templates/template_data_descriptor/scripts/generate_release_artifacts.py
```

Module logic:

- `src/data_descriptor/descriptor.py` — `build_descriptor_report`, `build_release_bundle_manifest`, `summarize_field_constraints`

Outputs (`output/reports/`):

- `descriptor_report.json` — validation findings and readiness score
- `release_bundle_manifest.json` — metadata-only release bundle manifest
- `field_constraints.json` — per-field constraint summary
