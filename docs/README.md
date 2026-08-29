# docs/ — template_data_descriptor

Human-facing documentation entry point. Agent-facing rules:
[`AGENTS.md`](AGENTS.md). Root overview: [`../README.md`](../README.md).

## What this repo is

`template_data_descriptor` (v0.1.0, CC-BY-4.0 — `../pyproject.toml`): a
public exemplar for FAIR-style data descriptor papers and dataset release
packets. The dataset, schema, provenance, licensing, and validation report
are treated as the research object under test.

## Directory map

- `src/` — `data_descriptor` package (business logic; see `src/README.md`,
  `src/AGENTS.md`)
- `scripts/` — `generate_figures.py`, `generate_release_artifacts.py`
  (thin orchestrators; see `scripts/README.md`)
- `manuscript/` — FAIR data-descriptor manuscript (sections
  `00_abstract`..`99_references`, `config.yaml`, `references.bib`,
  `figures/`; see `manuscript/README.md`)
- `data/`, `output/` — dataset inputs and generated release artifacts
- `docs/` — this documentation folder

## How to run / test

(from `../README.md`) Run via the template monorepo from the repository
root:

```bash
uv run python scripts/pipeline/stage_01_test.py --project templates/template_data_descriptor --project-only
```

Forks: copy `manuscript/config.yaml.example` to `manuscript/config.yaml`,
preserve template integrity, and keep output artifacts regenerated from
source.

## Maintenance

Docs here are short and factual, derived from the repo's own files. Update
the map above when top-level layout changes.
