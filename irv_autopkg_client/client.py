import logging
import os
import urllib.parse
import requests
from typing import Optional

from shapely.geometry import shape


BASE_URL: str = "https://global.infrastructureresilience.org/extract/v1/"

# N.B. requests will log request URLs @ debug level
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)


class Client:
    """
    For interacting with an irv-autopkg server. Persists a session between
    requests.

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

    @staticmethod
    def download_file(url: str, file_path: str) -> None:
        """
        Download a file to disk.

        Args:
            url: URL of resource
            file_path: Location on disk to save remote resource to
        """
        with open(file_path, "wb") as file:
            response = requests.get(url)
            file.write(response.content)

    def request(self, verb: str, route: str, *args, **kwargs) -> dict:
        """
        Wrap requests' request and prepend self.base_url to the requested route.

        Args:
            verb: HTTP verb to use on route
            route: URL that is a relative path from self.base_url

        Returns:
            Decoded JSON response from server
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

    def boundary(self, name: str) -> dict:
        """
        Detailed view of a given boundary.

        Args:
            name: Identifier for boundary (e.g. 'egy' for Egypt)
        """
        return self.request("GET", f"boundaries/{name}")

    def boundary_geometry(self, name: str) -> shape:
        """
        Boundary geometry.

        Args:
            name: Identifier for boundary (e.g. 'egy' for Egypt)

        Returns:
            Shapely geometry of boundary
        """
        return shape(self.boundary(name)["geometry"])

    def boundary_search(
        self,
        *,
        name: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None
    ) -> dict:
        """
        Search for a boundary by name or latitude, longitude coordinate pair.

        Args:
            name: Identifier for boundary (e.g. 'egy' for Egypt)
            latitude: Latitude in decimal degrees
            longitude: Longitude in decimal degrees
        """
        query_params = {}
        if name is not None:
            query_params["name"] = name
        if (latitude is not None) and (longitude is not None):
            query_params["latitude"] = latitude
            query_params["longitude"] = longitude

        return self.request("GET", "boundaries/search", params=query_params)

    def boundary_list(self) -> list:
        """
        List of available boundaries.
        """
        return self.request("GET", "boundaries")

    def extract(self, boundary_name: str) -> dict:
        """
        Details of existing extract.

        Args:
            boundary_name: Identifier for boundary (e.g. 'egy' for Egypt)
        """
        return self.request("GET", f"packages/{boundary_name}")

    def extract_download(
        self,
        boundary_name: str,
        download_dir: str,
        dataset_filter: Optional[list[str]] = None,
        overwrite: bool = False
    ) -> None:
        """
        Download the files contained within an extract to a given directory.
        Files will be grouped in dataset directories.

        Args:
            boundary_name: Name of the boundary to extract for
            download_dir: Location on disk to download files. Will be created
                if necessary.
            dataset_filter: List of datasets to download. If not supplied, will
                download all processed datasets for this boundary.
            overwrite: Whether to overwrite any existing files or folders.
        """
        extract = self.extract(boundary_name)

        url_to_file_path = {}
        for dataset in extract["datapackage"]["resources"]:

            dataset_id = ".".join([dataset["name"], dataset["version"]])
            if dataset_filter is not None:
                if dataset_id not in dataset_filter:
                    # we've filtered out this dataset, don't download the files
                    continue

            folder_name = "_".join([dataset["name"], dataset["version"]])
            folder_path = os.path.join(download_dir, boundary_name, folder_name)
            os.makedirs(folder_path, exist_ok=overwrite)

            for url in dataset["path"]:
                filename = url.split("/")[-1]
                url_to_file_path[url] = os.path.join(folder_path, filename)

        for i, (url, filepath) in enumerate(url_to_file_path.items()):
            logging.info(f"Downloading {i + 1} of {len(url_to_file_path)} to {filepath}")
            self.download_file(url, filepath)

    def extract_list(self) -> list:
        """
        List of boundaries with already processed data extracts.
        """
        return self.request("GET", "packages")

    def dataset(self, name_version: str) -> dict:
        """
        Return details on a given dataset.

        Args:
            name_version: Identifier for dataset including version,
                e.g. gri_osm.roads_and_rail_version_1
        """
        name, version = name_version.split(".")
        response = self.request("GET", "processors")
        dataset, = [dataset for dataset in response if dataset["name"] == name]
        version, = [version for version in dataset["versions"] if version["name"] == name_version]
        return version

    def dataset_list(self) -> list:
        """
        List of dataset identifiers available to extract from.
        """
        response = self.request("GET", "processors")
        return [version["name"] for dataset in response for version in dataset["versions"]]

    def job_submit(self, boundary_name: str, datasets: list[str]) -> str:
        """
        Submit a new extract job to the queue. If successfully submitted,
        returns UUID of created job.

        Args:
            boundary_name: Name of the boundary to extract
            datasets: List of datasets to extract, in the name.version style,
                e.g. ["gri_osm.roads_and_rail_version_1"]

        Returns:
            Extract job ID
        """
        response = self.request(
            "POST",
            "jobs",
            json = {
                "boundary_name": boundary_name,
                "processors": datasets
            }
        )
        return response["job_id"]

    def job_status(self, uuid: str) -> dict:
        """
        Information on job.

        Args:
            uuid: Unique ID that references an extract job.
        """
        return self.request("GET", f"jobs/{uuid}")

    def job_complete(self, uuid: str) -> bool:
        """
        Check if a processing job is completed, return True if so.

        Args:
            uuid: Unique ID that references an extract job.
        """
        return self.job_status(uuid)["job_group_status"] == "COMPLETE"

    def server_liveness(self) -> bool:
        """
        Check the API is alive.
        """
        return self.request("GET", "liveness")["status"] == "alive"

    def server_readiness(self) -> bool:
        """
        Check the API and the database are ready.
        """
        return self.request("GET", "readiness")["status"] == "ready"
