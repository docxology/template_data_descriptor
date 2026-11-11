# template_data_descriptor TODO

This backlog is future-only. Completed validation and dated review evidence are preserved in
[`docs/maintenance/exemplar-backlog-history.md`](../../../docs/maintenance/exemplar-backlog-history.md)
or in source-owned generated receipts. Each active row must retain a stable ID, size, dependency,
next action, proving artifact, acceptance command, and negative control; absence of an owner or external receipt
keeps a capability blocked rather than silently promoting it.

## Backlog operating rules

- Keep deterministic and offline defaults unchanged unless an upcoming row explicitly scopes an opt-in.
- Do not close a row until its producer, artifact, consumer, gate, and failing negative control are present.
- Treat unavailable network, LLM, container, formal-tool, and publication paths as explicit skips
  or blockers.
- Re-derive counts and receipts from live source data; never copy measurements into this planning file.

## Integrity and template-status gaps

- Keep rendered manuscript outputs, figures, and descriptor-review artifacts regenerated after schema or fixture changes. Recompute fixture checksums/row counts and update `data/example_descriptor.json` whenever `data/fixtures/` changes.
- Re-run `scripts/generate_figures.py` and `scripts/generate_release_artifacts.py` after any change to `src/data_descriptor/` so `output/figures/figure_registry.json` and `output/reports/*` stay in sync with the source.

## Configurable-surface gaps

- Extend `docs/manuscript/config.yaml.example` when new descriptor fields become first-class.

## Documentation and signposting gaps

- Keep README, AGENTS, STANDALONE, and the per-directory README/AGENTS pairs aligned with the descriptor validator, verification, and figure modules.

## Current test and validator contract

- The deterministic fixture descriptor is covered locally; live checks for larger
  tables or non-CSV media remain external-data work and are represented by the
  two blocked Medium rows below.

## Minor upcoming

| ID | Status | Size | Dependency | Next action / unblock condition | Proving artifact | Acceptance command | Negative control |
| --- | --- | --- | --- | --- | --- | --- | --- |
No active rows are currently scoped at this size.

## Medium upcoming

| ID | Status | Size | Dependency | Next action / unblock condition | Proving artifact | Acceptance command | Negative control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DATA-PUBLICATION-1` | blocked-external | Medium | A real fork and owner receipt | Obtain the required owner or external receipt to unblock; run project tests and standalone export check and attach publication receipt + standalone replay. | publication receipt + standalone replay | `uv run pytest projects/templates/template_data_descriptor/tests -q --no-cov` | fabricated publication receipt must fail |
| `DATA-MEDIA-1` | blocked-external | Medium | Real licensed non-CSV fixture | Obtain a real licensed non-CSV fixture and attach its checksum/row manifest before promoting the media claim. | media checksum/row manifest + license receipt | `uv run pytest projects/templates/template_data_descriptor/tests -q --no-cov` | unsupported media, malformed rows, symlink escape, or wrong checksum must fail |

## Major upcoming

| ID | Status | Size | Dependency | Next action / unblock condition | Proving artifact | Acceptance command | Negative control |
| --- | --- | --- | --- | --- | --- | --- | --- |
No active rows are currently scoped at this size.

## Backlog status

Rows remain active until the acceptance command and negative control pass in the same source revision.
A blocked row is a deliberate boundary, not a skipped success.

## Workflowz review — 2026-11-10

- [ ] **WFZ-DD-1 — P1 — Make malformed `fields` descriptors return findings instead of raising.** Outcome: `validate_descriptor` and `build_descriptor_report` handle a non-iterable `fields` value through the normal invalid-descriptor result path, while valid descriptors retain their existing fingerprints. Evidence: `src/data_descriptor/descriptor.py:63-72` iterates `fields` directly even though report construction later guards non-list values at `src/data_descriptor/descriptor.py:96-103`. Acceptance probe from the standalone repository root: `uv run python -c 'from data_descriptor.descriptor import build_descriptor_report; report = build_descriptor_report({"name":"n","version":"1","license":"CC-BY-4.0","files":[],"fields":None,"provenance":[]}); assert not report.valid; assert report.field_count == 0; assert report.findings'`; run the same probe before the fix to confirm it currently raises `TypeError`. Dependencies/constraints: none external; preserve deterministic fingerprint ordering and the existing malformed-container validation vocabulary where applicable.

- [ ] **WFZ-DD-2 — P2 — Distinguish an unsafe/non-file declared path from a genuinely absent file.** Outcome: a declared existing directory or other non-regular path receives a failing verification status rather than the non-failure `absent` classification, so metadata-only release semantics remain limited to files that are actually not present. Evidence: `src/data_descriptor/verification.py:10-12` defines absent files as legitimately referenced but not bundled, whereas `src/data_descriptor/verification.py:211-221` combines `not path` and `not resolved.is_file()` into `STATUS_ABSENT`; the summary only counts verified/absent/mismatch statuses at `src/data_descriptor/verification.py:164-176`. Acceptance probe from the standalone repository root: `uv run python -c 'import tempfile; from pathlib import Path; from data_descriptor.verification import STATUS_ABSENT, verify_descriptor_files, verification_summary; root=Path(tempfile.mkdtemp()); (root/"fixtures").mkdir(); result=verify_descriptor_files({"files":[{"path":"fixtures","checksum":"sha256:"+"0"*64,"rows":0,"media_type":"text/csv"}]}, root)[0]; assert result.status != STATUS_ABSENT; assert verification_summary((result,))["mismatch"] == 1'`. Dependencies/constraints: no new media reader or network access; preserve `absent` for genuinely missing metadata-only files and retain the existing symlink/escape checks at `src/data_descriptor/verification.py:186-210`.
