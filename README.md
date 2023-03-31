# irv-autopkg-client
A client library for accessing the irv-autopkg API.

The irv-autopkg service allows users to extract portions of global datasets pertaining to climate risk and resilience. This Python package is a client for communicating with the irv-autopkg API.

## Installation

Install from PyPI with:
```
pip install irv-autopkg-client
```

## Usage

Create a client object to establish a session
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

To submit an extract job:
```
job_id = client.job_submit(
    country_iso,
    [
        "gri_osm.roads_and_rail_version_1",
        "wri_aqueduct.version_2"
    ]
)
```

We can then check if the job is complete:
```
client.job_complete(job_id)
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
