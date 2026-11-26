# Adapt the exemplar

Start with a checkout or fork of this standalone repository. If you maintain
the project inside the shared template, its
[copy helper](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/scripts/audit/copy_exemplar.py)
can create an exemplar-based workspace from a template checkout containing
the source project.

1. Update [the descriptor](../data/example_descriptor.json) with your dataset
   identity, license, file paths, media types, SHA-256 digests, row counts, field
   constraints, primary key, and provenance. Resolve file paths relative to the
   descriptor directory. Keep restricted bytes outside the public repository.
2. Update [the manuscript configuration](manuscript/config.yaml) from its
   [example](manuscript/config.yaml.example) using your project's identity.
   Update the citation sidecars, [domain profile](../domain_profile.yaml), and
   [experiment plan](../experiment_plan.yaml) to match. Replace the exemplar's
   publication identifiers with your project's own recorded identifiers.
3. Review the fixture-specific tests and adapt their expected records and
   negative controls. Use the [validation and regeneration commands](README.md)
   to build new evidence and the [manuscript guide](manuscript/README.md) to
   build the publication outputs.

The metadata-only release manifest is a review artifact. A publication receipt
requires explicit owner attestation and an artifact digest matching the owner's
approval. The sample descriptor and the exemplar's DOI document the published
template. Your fork needs its own publication evidence.
