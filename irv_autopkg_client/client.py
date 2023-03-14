import urllib.parse

import logging
import requests
from typing import Optional


BASE_URL: str = "https://global.infrastructureresilience.org/extract/v1/"

# requests will log requests @ debug level
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)


class Client:
    """

    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        timeout: The maximum amount of a time in seconds a request can take.
        _session: A requests.Session used for all requests
    """

    def __init__(
        self,
        base_url: str = BASE_URL,
        timeout: float = 20,
        **kwargs
    ):
        self.base_url = base_url
        self.timeout = timeout
        self._session = requests.Session()

    def request(self, verb: str, route: str, *args, **kwargs) -> requests.Response:
        """
        Wrap requests' request and prepend self.base_url to the requested route.
        """

        if "timeout" in kwargs:
            timeout = kwargs.pop("timeout")
        else:
            timeout = self.timeout

        url = urllib.parse.urljoin(self.base_url, route)

        response = self._session.request(
            verb,
            url,
            *args,
            timeout=timeout,
            **kwargs
        )

        response.raise_for_status()

        return response.json()

    def list_boundaries(self) -> list:
        """

        """
        return self.request("GET", "boundaries")

    def boundary(self, name: str) -> dict:
        """

        """
        return self.request("GET", f"boundaries/{name}")

    def boundary_search(
        self,
        *,
        name: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None
    ) -> dict:
        """

        """
        query_params = {}
        if name is not None:
            query_params["name"] = name
        if latitude is not None:
            query_params["latitude"] = latitude
        if longitude is not None:
            query_params["longitude"] = longitude

        return self.request("GET", "boundaries/search", params=query_params)

    def job(self, uuid: str) -> dict:
        """

        """


# "/jobs/{job_id}".format(client.base_url, job_id=job_id)
# "/jobs".format(client.base_url)
# "/packages".format(client.base_url)
# "/packages/{boundary_name}".format(client.base_url, boundary_name=boundary_name)
# "/liveness".format(client.base_url)
# "/readiness".format(client.base_url)
# "/processors".format(client.base_url)
