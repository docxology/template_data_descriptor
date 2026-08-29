# AGENTS.md — docs/ (template_data_descriptor)

## Layout

- `README.md` — human entry point (what this repo is, directory map, run/test)
- `AGENTS.md` — this file: conventions for maintaining docs/

## Key modules (pointer, not duplication)

Authoritative per-package rules live in `../AGENTS.md` (root), `src/AGENTS.md`,
`scripts/AGENTS.md`, and `manuscript/AGENTS.md`; `../STANDALONE.md` documents
standalone operation.

## Conventions observed in this repo

- FAIR contract: schema, file inventory, data dictionary, provenance chain,
  license boundary, quality checks, and machine-readable descriptor must
  stay mutually consistent before publication (from `../README.md`).
- Publication metadata: concept DOI 10.5281/zenodo.21298883, version DOI
  10.5281/zenodo.21298884 (root `README.md` publishing block).
- Business logic in `src/`; `scripts/` are thin orchestrators.
- Zero unresolved `{{TOKEN}}` placeholders in manuscript markdown (verified
  2026-08-29 audit).

## Maintaining these docs

Keep both files short (30–80 lines), factual, and derived only from repo
files. Do not duplicate module-level rules here.
