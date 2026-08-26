# Generated catalog

The catalog is generated from accepted artifact front matter.

- `artifacts.jsonl` is the canonical machine-readable index.
- `artifacts.csv` supports spreadsheet review and simple analysis.

Do not edit generated files manually.

```bash
python scripts/build_catalog.py
python scripts/build_catalog.py --check
```

The JSONL index intentionally contains concise metadata. Retrieve the artifact file for full context and the original source for current product-specific claims.
