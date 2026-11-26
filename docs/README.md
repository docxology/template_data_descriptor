# Data descriptor documentation

- [Set up and test](#set-up-and-test)
- [Inputs and configuration](#inputs-and-configuration)
- [Generate and verify outputs](#generate-and-verify-outputs)
- [Manuscript and render instructions](manuscript/README.md)
- [Adapt the exemplar to a dataset](forking.md)

## Set up and test

Install uv and use Python 3.11 or newer. From the standalone repository root:

```bash
uv sync --locked --extra dev
uv run --locked --extra dev pytest --cov=src --cov-fail-under=90
```

The tests exercise the checked-in descriptor and fixture files, checksum and
row-count negative controls, and both artifact-generation scripts.

## Inputs and configuration

- [Descriptor JSON](../data/example_descriptor.json) defines the dataset
  identity, license, file inventory, field contracts, primary key, and
  provenance. Its file paths resolve relative to `data/`.
- [Fixture tables](../data/fixtures/README.md) are public synthetic CSVs.
  Keep their recorded hashes and data-row counts in sync with the inventory.
- [Manuscript configuration](manuscript/config.yaml) controls publication and
  render metadata. See the [forkable example](manuscript/config.yaml.example).
- The [domain profile](../domain_profile.yaml) and
  [experiment plan](../experiment_plan.yaml) describe the exemplar's scope.

## Generate and verify outputs

```bash
uv run --locked python scripts/generate_figures.py
uv run --locked python scripts/generate_release_artifacts.py
```

The figure producer regenerates the embedded PNGs in
[manuscript/figures](manuscript/figures/README.md), mirrors them into
`output/figures/`, and writes their figure registry. The release producer
writes `descriptor_report.json`, `field_constraints.json`, and
`release_bundle_manifest.json` under `output/reports/`. Override its input
with `--descriptor` and destination with `--output-dir`.

Inspect the report's `valid` field and findings. The release producer can
write a report for an invalid descriptor. Verify the fixture bytes separately
by inspecting the checksum-verification figure or calling
`verify_descriptor_files(descriptor, descriptor_path.parent)`. Its row
readers support CSV, JSON arrays or objects containing a `rows`, `data`, or
`records` list, and newline-delimited JSON. These checks compare hashes
and row counts. Field constraint validation checks the declarations in
the descriptor. The release manifest contains metadata and checksums.
