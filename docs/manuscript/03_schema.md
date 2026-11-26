# Schema and data dictionary {#sec:schema}

The descriptor's `fields` list is the dataset's **data dictionary**: it names
each column of the primary measurement table and declares its type, nullability,
optional unit, and value constraints. The schema figure renders this dictionary from the descriptor via `schema_table_rows()` in
`src/data_descriptor/figures.py`.

![Field schema / data dictionary: one row per declared field, with type, nullability, unit, and a compact constraint label, from `schema_table_rows()`. Identifier fields carry regular-expression patterns; the categorical fields carry closed enumerations; the quantitative field carries a unit and numeric bounds. The table is generated from `data/example_descriptor.json`.](figures/schema_overview.png){#fig:schema_overview fig-alt="Table listing measurement fields, types, nullability, units, and declared constraints."}

## Field contract

The declared fields exercise the constraint vocabulary the validator
understands:

- **`sample_id`** (`string`, not null) — the primary key, constrained to the
  pattern `^S[0-9]{3}$`.
- **`subject_id`** (`string`, not null) — foreign key into `fixtures/subjects.csv`,
  constrained to `^P[0-9]{3}$`.
- **`group`** (`category`, not null) — a closed enumeration of `control` and
  `treatment`.
- **`value`** (`number`, not null) — the measurement, carrying the unit
  `normalized_score` and numeric bounds `[0, 1]`.
- **`collected_on`** (`date`, not null) — an ISO-8601 collection date.
- **`instrument`** (`category`, not null) — a closed enumeration of `sensor_a`
  and `sensor_b`.

## Schema fingerprint

`descriptor_fingerprint()` reduces the field list to a stable, order-independent
sha256 fingerprint over `(name, type, nullable)` triples. Reordering the fields
leaves the fingerprint unchanged, so two descriptors with the same schema hash
identically regardless of authoring order — the property is asserted directly in
the test suite. The fingerprint is what lets a release manifest reference "the
field shape" without depending on authoring order. Units, bounds, descriptions,
patterns, and allowed values fall outside this fingerprint. The release
manifest separately records a hash of the full descriptor.

## Constraint validation

The validator flags quantitative fields that lack a unit, categorical fields that
lack allowed values, enumerations that are present but empty, numeric bounds where
the minimum exceeds the maximum, and patterns declared on non-text fields. The
shipped descriptor passes these checks. Field constraints are checked as
declarations. Byte verification counts rows and checks digests, leaving cell
values, key uniqueness, and foreign-key membership to dataset-specific checks.
