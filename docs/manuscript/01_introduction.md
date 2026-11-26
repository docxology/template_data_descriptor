# Introduction {#sec:introduction}

A data descriptor records what a dataset contains, how it was produced,
how it is licensed, and which quality checks its release supports. The FAIR guiding principles — Findable, Accessible, Interoperable,
Reusable [@wilkinson2016fair] — frame why this matters: a dataset is only
reusable to the extent that its structure and provenance are legible to both
humans and machines. Datasheets and the Data Package specification provide
examples of structured dataset documentation and machine-readable packaging
[@gebru2021datasheets; @frictionless2023datapackage].

## What this template provides

This exemplar packages the recurring moving parts of a data descriptor so that a
fork can start from a working, tested baseline:

- A **schema / data dictionary**: named fields with declared types,
  nullability, units, and value constraints (patterns, enumerations, numeric
  bounds).
- A **file inventory**: each shipped file with its media type, a sha256
  checksum, and a row count.
- A **provenance chain**: the ordered steps and agents that produced the release.
- A **license boundary**: an explicit reuse license, and the discipline of
  publishing *metadata and checksums* rather than bundling restricted bytes.
- A **validation gate**: a tested library that rejects malformed, unsafe, or
  incomplete descriptors and verifies declared checksums against real bytes.

## Scope and honesty

The checked-in synthetic dataset enables local replay of schema and byte
checks. Its observed values provide evidence about the release workflow.
A fork should adapt its descriptor, byte readers, tests, and figures to the
structure and media types of the dataset it intends to publish.
