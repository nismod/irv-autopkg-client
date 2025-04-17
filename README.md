# irv-autopkg-client

[![PyPI](https://img.shields.io/pypi/v/irv-autopkg-client)](https://pypi.org/project/irv-autopkg-client/)

A client library for accessing the irv-autopkg API, currently hosted at
[global.infrastructureresilience.org](https://global.infrastructureresilience.org/extract/redoc).

The irv-autopkg service allows users to extract portions of global datasets
pertaining to climate risk and resilience. This Python package is a client for
communicating with the irv-autopkg API.

## Installation

Install from PyPI with:

```
pip install irv-autopkg-client
```

## Usage

Create a client object to establish a session:

```
import irv_autopkg_client
client = irv_autopkg_client.Client()
```

For a list of available methods, try:

```
help(client)
```

## Quick start

Is the API responding?

```
client.server_readiness()
```

Which boundaries can we create extracts for?

```
client.boundary_list()
```

Which datasets are available?

```
client.dataset_list()
```

Get information on a specific dataset:

```
client.dataset("wri_aqueduct.version_2")
```

Get the boundary of a territory:

```
boundary = client.boundary_geometry("bgd")
```

Download some extracted data:

```
client.extract_download(
    "bgd",
    "data",
    # there may be other datasets available, but only download the following
    dataset_filter=[
        "gri_osm.roads_and_rail_version_1",
        "wri_aqueduct.version_2"
    ],
    overwrite=True
)
```

## Development

First clone this repository (currently hosted at
[nismod/irv-autopkg-client](https://github.com/nismod/irv-autopkg-client.git)).

To install the package in editable mode, run:

```
pip install -e .
pip install vcrpy~=7.0
```

Alternatively, if you have [`poetry`](https://python-poetry.org/docs/), run:

```
poetry install
```

## Testing

To run the bundled tests, try:

```
python -m unittest
```

With `poetry`, either work within `poetry shell`, or run single commands in the
virtual environment:

```
poetry run python -m unittest
```


## Acknowledgments

This research received funding from the FCDO Climate Compatible Growth Programme. The views expressed here do not necessarily reflect the UK government's official policies. 
