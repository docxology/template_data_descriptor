# Abstract

This exemplar demonstrates a **data descriptor** workflow in which the schema,
file inventory, provenance chain, license boundary, and validation gate are
treated as first-class research artifacts rather than afterthoughts. It ships a
public synthetic measurement and subject tables and a machine-readable descriptor
(`data/example_descriptor.json`) that declares each file's media type, sha256
checksum, and row count alongside a typed data dictionary. The validation library checks the
descriptor's shape and recomputes the checksum and row count for each
available file. It can also generate a metadata-only manifest for release
review. The synthetic fixtures demonstrate how to describe and verify a
dataset release.
