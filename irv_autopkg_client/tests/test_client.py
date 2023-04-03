import unittest

import vcr

from irv_autopkg_client import Client


class TestClient(unittest.TestCase):
    """
    Tests for the API client.

    Utilises VCR (network requests and responses are only made if not available
    in a local cache known as a cassette). If you wish to receive a fresh
    response from the server, delete the tapes and re-run the tests.

    Methods that do not yet have test coverage:
        test_download_file
        test_request
        test_extract_download
        test_job_submit
        test_job_status
        test_job_complete
    """

    def setUp(self):
        self.client = Client()

    @vcr.use_cassette()
    def test_boundary(self):
        expected_keys = set(
            ["name", "name_long", "admin_level", "geometry", "envelope"]
        )
        assert expected_keys == set(self.client.boundary("vat").keys())

    @vcr.use_cassette()
    def test_boundary_geometry(self):
        vatican_geojson = {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [12.453136917, 41.902751941],
                        [12.452714082, 41.903016213],
                        [12.452766936, 41.903439049],
                        [12.453031208, 41.903914738],
                        [12.453982588, 41.903861884],
                        [12.454035442, 41.902751941],
                        [12.453136917, 41.902751941],
                    ]
                ]
            ],
        }
        geom = self.client.boundary_geometry("vat")
        assert vatican_geojson == geom

    @vcr.use_cassette()
    def test_boundary_search_by_coordinates(self):
        expected = [{"name": "gbr", "name_long": "United Kingdom"}]
        assert expected == self.client.boundary_search(longitude=-1, latitude=52)

    @vcr.use_cassette()
    def test_boundary_search_by_name(self):
        expected = [{"name": "gbr", "name_long": "United Kingdom"}]
        assert expected == self.client.boundary_search(name="united kingdom")

    @vcr.use_cassette()
    def test_boundary_search_no_kwargs(self):
        with self.assertRaises(RuntimeError):
            self.client.boundary_search()

    @vcr.use_cassette()
    def test_boundary_list(self):
        response = self.client.boundary_list()
        assert type(response) == list
        for boundary in response:
            assert type(boundary) == dict
            assert set(["name", "name_long"]) == boundary.keys()

    @vcr.use_cassette()
    def test_extract(self):
        expected_keys = set(
            ["boundary_name", "uri", "boundary", "processors", "datapackage"]
        )
        assert expected_keys == self.client.extract("mar").keys()

    @vcr.use_cassette()
    def test_extract_list(self):
        response = self.client.extract_list()
        assert type(response) == list
        for extract in response:
            assert type(extract) == dict
            assert set(["boundary_name", "uri"]) == extract.keys()

    @vcr.use_cassette()
    def test_dataset(self):
        expected_keys = set(
            [
                "name",
                "description",
                "version",
                "status",
                "uri",
                "data_author",
                "data_title",
                "data_title_long",
                "data_summary",
                "data_citation",
                "data_license",
                "data_origin_url",
                "data_formats",
            ]
        )
        assert (
            expected_keys
            == self.client.dataset("gri_osm.roads_and_rail_version_1").keys()
        )

    @vcr.use_cassette()
    def test_dataset_list(self):
        response = self.client.dataset_list()
        assert type(response) == list
        for dataset in response:
            assert type(dataset) == str
            assert len(dataset.split(".")) == 2

    @vcr.use_cassette()
    def test_server_liveness(self):
        assert self.client.server_liveness()

    @vcr.use_cassette()
    def test_server_readiness(self):
        assert self.client.server_readiness()

    def tearDown(self):
        self.client._session.close()
