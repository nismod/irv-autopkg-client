## Publishing

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging.

To publish, first update the metadata (authors, version, etc.) in:
- pyproject.toml
- irv_autopkg_client/__init__.py

Then publish to PyPI with `poetry publish --build`.
