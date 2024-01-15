import requests
from requests_oauth2client import *


class SpotifyRequests:
    _BASE_URL = "https://api.spotify.com/v1"
    _GET_ALBUM_ENDPOINT = "/albums/"
    _GET_NEW_RELEASES_ENDPOINT = "/browse/new-releases"
    _TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token"
    _AUTH_CLIENT_SECRET_AND_PASSWORD = ("8db23dc7df104f939e925238c7aecf95", "a0f09b3dbff94993bac091741ee3166a")
    _CALLBACK_URI = "http://testitfactorypyta1"
    _TOKEN = ""

    _SCOPES = "ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing " \
              "app-remote-control streaming playlist-read-private playlist-read-collaborative " \
              "playlist-modify-private playlist-modify-public user-follow-modify user-follow-read " \
              "user-read-playback-position user-top-read user-read-recently-played user-library-modify " \
              "user-library-read user-read-email user-read-private"

    def __init__(self):
        self.generate_token()

    def generate_token(self):
        if len(self._TOKEN) < 1:
            # Instantam un client prin care obtinem tokenul
            # Clientul primeste ca parametri:
            # - token_endpoint - endpointul de generare a tokenului
            # - auth - tuplu format din client_id si client_secret
            oauth2client = OAuth2Client(token_endpoint=self._TOKEN_ENDPOINT, auth=self._AUTH_CLIENT_SECRET_AND_PASSWORD)
            self._TOKEN = f"Bearer {oauth2client.client_credentials(scope=self._SCOPES, resource=self._CALLBACK_URI)}"

    def get_token(self):
        return self._TOKEN

    def get_header_auth(self):
        return {"Authorization": self.get_token()}

    def get_album(self, album_id):
        album_endpoint = self._BASE_URL + self._GET_ALBUM_ENDPOINT + album_id
        response = requests.get(album_endpoint, headers=self.get_header_auth())
        return response

    def get_new_releases(self, country="", limit=""):
        new_releases_endpoint = self._BASE_URL + self._GET_NEW_RELEASES_ENDPOINT

        if country == "" and limit != "":
            new_releases_endpoint += f"?limit={limit}"

        elif country != "" and limit == "":
            new_releases_endpoint += f"?country={country}"

        elif country != "" and limit != "":
            new_releases_endpoint += f"?country={country}&limit={limit}"

        response = requests.get(new_releases_endpoint, headers=self.get_header_auth())
        return response



# spotify_api = SpotifyRequests()
#
# spotify_api.generate_token()
# spotify_api.generate_token()
# spotify_api.generate_token()
# spotify_api.generate_token()