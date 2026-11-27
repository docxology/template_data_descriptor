# manuscript - template_data_descriptor

Full manuscript for the data descriptor exemplar, rendered by the monorepo
pipeline (Pandoc). Sections, in render order:

- `00_abstract.md` — abstract
- `01_introduction.md` — background and what the template provides
- `02_data_description.md` — the demonstration dataset and file inventory
- `03_schema.md` — schema / data dictionary and schema fingerprint
- `04_provenance.md` — provenance chain
- `05_quality_validation.md` — validation gate and descriptor↔file verification
- `06_usage_notes.md` — regenerating artifacts and forking guidance
- `99_references.md` — references

Figures live under [`figures/`](figures/README.md) and are embedded in prose with
blocks such as `![Schema overview](figures/schema_overview.png){#fig:schema_overview}`. Configuration lives in
`config.yaml` (forkable defaults in `config.yaml.example`). Every quantitative
claim is derived from `data/example_descriptor.json` and the tested
`src/data_descriptor/` package — the prose transcribes no volatile numbers.

## Render and validate

Use a disposable standalone checkout whose physical directory name is
`template_data_descriptor`. The pinned renderer's Stage 04 checks for the
combined PDF using that directory name, which must match the final component
of `working/template_data_descriptor`. Regeneration writes to the project's
existing output tree. Install Git, uv, Pandoc, XeLaTeX, and the
PDF and Beamer dependencies in the pinned template's
[setup guide](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/guides/startup-and-setup.md).

Run these steps from the standalone checkout root. They preserve the incoming
output snapshot elsewhere so validation sees only newly generated artifacts.

```bash
descriptor_checkout="$(pwd -P)"
build_workspace="$(mktemp -d)"
mv output "$build_workspace/previous-output"
uv sync --locked --extra dev
uv run --locked python scripts/generate_figures.py
uv run --locked python scripts/generate_release_artifacts.py

template_checkout="$build_workspace/template"
git clone https://github.com/docxology/template.git "$template_checkout"
git -C "$template_checkout" checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
cd "$template_checkout"
uv sync --locked
mkdir -p projects/working
ln -s "$descriptor_checkout" projects/working/template_data_descriptor
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/template_data_descriptor
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/template_data_descriptor
```

The renderer resolves this `docs/manuscript/` directory automatically.
Inspect `output/pdf/template_data_descriptor_combined.pdf`,
`output/web/index.html`, the PDFs under `output/slides/`, and
`output/reports/validation_report.md` in the standalone checkout. Check that
the combined editions contain the expected sections, bibliography, and five
figures. Treat existing committed output as a snapshot and re-run the build
when you need output for the current revision.

From the template checkout prepared above, you can also check the source
bibliography.

```bash
uv run --no-sync python -m infrastructure.reference.citation.cli validate \
    projects/working/template_data_descriptor/docs/manuscript/references.bib --strict
```
