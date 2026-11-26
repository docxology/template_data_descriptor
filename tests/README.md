# tests - template_data_descriptor

Zero-mock tests over real fixture dictionaries, real temporary files, and real
generated PNGs. See [`AGENTS.md`](AGENTS.md) for the full contract and
per-file coverage map.

Run from the standalone checkout root:

```bash
uv run --locked --extra dev pytest --cov=src --cov-fail-under=90
```
