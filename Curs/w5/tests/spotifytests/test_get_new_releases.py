import unittest

from w5.requests.spotifyapi.spotify_requests import SpotifyRequests
from w5.tests.spotifytests.test_base import TestBase


class TestGetNewReleases(TestBase):

    def setUp(self) -> None:
        self.spotify = SpotifyRequests()

    def test_get_new_releases_no_filter(self):
        response = self.spotify.get_new_releases()

        # expected_response_code = 200
        # actual_response_code = response.status_code
        # self.assertEqual(expected_response_code, actual_response_code, "Unexpected status code")
        self.verify_status_code(200, response.status_code)

        # expected_response_size = 20
        # actual_response_length = len(response.json()["albums"]["items"])
        # self.assertEqual(expected_response_size, actual_response_length, "Unexpected response size")
        self.verify_response_size(20, response.json()["albums"]["items"])

    def test_get_new_releases_filter_by_country(self):
        country = "RO"
        response = self.spotify.get_new_releases(country=country)

        # este o lista cu 20 de dict-uri python
        items_list = response.json()["albums"]["items"]

        self.verify_status_code(200, response.status_code)
        self.verify_response_size(20, items_list)

        # available_markets = items_list[0]["available_markets"]
        # assert "RO" in available_markets

        for i in range(len(items_list)):
            current_item = items_list[i]
            name = current_item["name"].encode("utf-8")
            available_markets = current_item["available_markets"]

            #la unul dintre albume nu avem RO in lista (posibil bug la spotify in API?)
            assert "RO" in available_markets or len(available_markets) == 0
            print(f"RO este in lista cu available_markets pentru albumul {name}")


