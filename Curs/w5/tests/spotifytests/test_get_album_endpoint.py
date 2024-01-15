import unittest

from w5.requests.spotifyapi.spotify_requests import SpotifyRequests
from w5.tests.spotifytests.test_base import TestBase


class TestGetAlbum(TestBase):

    def setUp(self):
        self.spotify = SpotifyRequests()

    def test_get_album_status_code_and_name(self):
        thriller_album_id = "2ANVost0y2y52ema1E9xAZ"
        response = self.spotify.get_album(thriller_album_id)

        self.verify_status_code(200, response.status_code)

        expected_album_name = "Thriller"
        actual_album_name = response.json()["name"]

        self.assertEqual(expected_album_name, actual_album_name, "Unexpected album name")