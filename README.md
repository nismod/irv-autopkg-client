# irv-autopkg-client
A client library for accessing IRV Autopackage API

## Usage
First, create a client:

```python
from irv_autopkg_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from irv_autopkg_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use the models:

```python
# which countries have already had some data generated?

from irv_autopkg_client.api.packages import get_packages_v1_packages_get as get_packages

response = get_packages.sync(client=client)
for pkg in response:
    print(pkg.boundary_name, pkg.uri)
```

Another example:
```python
# which data processors can we deploy against some country boundary?

from irv_autopkg_client.api.processors import get_processors_v1_processors_get as get_processors

response = get_processors.sync(client=client)
for p in response:
    for v in p.versions:
        print(v.processor.name)
        print(f"  {v.processor.description}\n")
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl=False
)
```

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info.

Things to know:
- Every path/method combo becomes a Python module with four functions:
 - `sync`: Blocking request that returns parsed data (if successful) or `None`
 - `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
 - `asyncio`: Like `sync` but async instead of blocking
 - `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

- All path/query params, and bodies become method arguments.
- If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
- Any endpoint which did not have a tag will be in `irv_autopkg_client.api.default`

## Building / publishing this Client

This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
- Update the metadata in pyproject.toml (e.g. authors, version)
- Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
- If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
- If that project is not using Poetry:
 - Build a wheel with `poetry build -f wheel`
 - Install that wheel from the other project `pip install <path-to-wheel>`
