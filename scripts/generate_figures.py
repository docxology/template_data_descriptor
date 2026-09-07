#!/usr/bin/env python3
"""Render descriptor figures, mirror them to output, and register provenance."""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(PROJECT_ROOT / "src"), str(PROJECT_ROOT.parents[2])]

import data_descriptor as dd  # noqa: E402
from data_descriptor.rendering import render_descriptor_figures  # noqa: E402

try:  # Monorepo; standalone clones fall back to the project-local publisher.
    from infrastructure.documentation.generated_figure_registry import publish_generated_figures  # noqa: E402
except ModuleNotFoundError:
    from data_descriptor.registry import publish_generated_figures  # noqa: E402


def main(project_root: Path | None = None) -> list[Path]:
    root = project_root or PROJECT_ROOT
    rendered = render_descriptor_figures(root)
    published = publish_generated_figures(
        root / "output" / "figures",
        dd.DESCRIPTOR_FIGURE_SPECS,
        rendered,
        schema_version=dd.FIGURE_REGISTRY_SCHEMA,
    )
    written = [*rendered, *published]
    print("\n".join(str(path) for path in written))
    return written


if __name__ == "__main__":
    main()
