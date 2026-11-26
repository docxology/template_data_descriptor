# Usage notes {#sec:usage}

## Regenerating the artifacts

Run these commands from the standalone project root with uv installed.

```bash
uv run --locked python scripts/generate_figures.py
uv run --locked python scripts/generate_release_artifacts.py
```

The first command updates the manuscript PNGs and publishes their
mirrors and registry under `output/figures/`. The second command
writes a descriptor report, field-constraint summary, and metadata-only
release manifest to `output/reports/`. Inspect the descriptor report's
findings, then use the checksum verification results to check the files.

## Adapting the descriptor

Replace the fixture-specific inventory, data dictionary, primary key,
license, and provenance when adapting the project. Compute hashes and
row counts from the bytes intended for release. Keep restricted files in
their authorized storage and record the access conditions in the dataset
documentation. Retain negative controls that detect changed bytes and
invalid descriptors.

The metadata manifest supports review. An actual publication receipt
requires explicit owner approval bound to the artifact digest.
