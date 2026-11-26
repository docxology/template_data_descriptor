# Data description {#sec:data}

The demonstration dataset consists of two comma-separated files under
`data/fixtures/`, described by the machine-readable descriptor
`data/example_descriptor.json` [@descriptor-example].

- `fixtures/measurements.csv` — one row per synthetic sample, with a bounded
  measurement, an assignment group, a capture instrument, and a collection date.
- `fixtures/subjects.csv` — one row per synthetic subject, with an enrollment
  site and date. Each measurement references a subject through the `subject_id`
  foreign key. The subject table carries its own enrollment fields. The
  descriptor's field dictionary covers the measurement table.

## File inventory

The descriptor declares each file's media type, sha256 checksum, and row count.
The file inventory figure shows the declared row counts, read directly from the
descriptor by `file_inventory_rows()` in `src/data_descriptor/figures.py` and plotted by `scripts/generate_figures.py`.

![File inventory: declared row counts per file, from `file_inventory_rows()`. The measurement table is the larger of the two files; the subject table is its dimension companion. Both are declared as `text/csv`. The bars show the counts declared in the descriptor. Byte verification compares these declarations with actual file rows.](figures/file_inventory.png){#fig:file_inventory fig-alt="Bar chart comparing declared row counts for the measurement and subject CSV files."}

File paths in the descriptor resolve relative to its directory. Rerun the
figure producer after changing the descriptor or fixtures so the embedded
figures and their provenance registry reflect the same inputs.

## Release boundary

The descriptor is deliberately a *metadata* object. For a real dataset, the
descriptor and its checksums can be published even when the underlying bytes are
access-controlled: the checksums let a downstream user verify integrity once they
obtain the files through the appropriate channel. In this template the fixture
bytes are public and small, so they are shipped alongside the descriptor and used
to demonstrate end-to-end verification.
