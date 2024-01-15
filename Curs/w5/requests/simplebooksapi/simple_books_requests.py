import requests

import random


# Se instalează package-urile:
# - requests
# - html-testRunner

class SimpleBooksRequests:
    # definim BASE URL si endpoint-urile din aplicatie
    # vom adauga un underscore la numele variabilelor ca sa le ascundem in clasele de test ( _ )
    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_AUTH_ENDPOINT = "/api-clients/"
    _API_STATUS_ENDPOINT = "/status"
    _GET_ALL_BOOKS_ENDPOINT = "/books"
    _ORDERS_ENDPOINT = "/orders"

    # metoda care va returna
    def get_api_status(self):
        api_status_url = self._BASE_URL + self._API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    # metoda care va avea niște parametri impliciți
    # Parametrii sunt:
    # - book_type (fiction sau non-fiction)
    # - limit (numar intre 1-20)
    # Parametrii vor fi folosiți în cazul în care vrem să filtrăm rezultatele pe care ni le trimite API-ul,
    # iar în funcție de asta vom construi URL-ul apelat
    def get_all_books(self, book_type="", limit=""):

        get_all_books_url = self._BASE_URL + self._GET_ALL_BOOKS_ENDPOINT
        # https://simple-books-api.glitch.me/books

        # Adaugam parametrii la link in cazul in care avem filtrare
        # Daca avem parametru type
        if book_type != "" and limit == "":
            get_all_books_url += f"?type={book_type}"

        # Daca avem parametru limit
        elif book_type == "" and limit != "":
            get_all_books_url += f"?limit={limit}"

        # Daca am si type si limit
        elif book_type != "" and limit != "":
            get_all_books_url += f"?type={book_type}&limit={limit}"

        response = requests.get(get_all_books_url)

        return response

    # metoda care ne va returna token-ul de acces
    def generate_token(self):
        auth_url = self._BASE_URL + self._API_AUTH_ENDPOINT

        random_number = random.randint(1, 9999999999999999999999999999)

        request_body = {
            "clientName": "PYTA1",
            "clientEmail": f"testautomation{random_number}@example.com"
        }

        response = requests.post(auth_url, json=request_body)

        return response.json()["accessToken"]

    def submit_order(self, access_token, book_id, customer_name):

        submit_orders_url = self._BASE_URL + self._ORDERS_ENDPOINT

        header_params = {"Authorization": access_token}

        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        response = requests.post(submit_orders_url, json=request_body, headers=header_params)

        return response

    def update_order(self, access_token, order_id, new_customer_name):

        order_update_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {"Authorization": access_token}

        request_body = {
            "customerName": new_customer_name
        }

        response = requests.patch(order_update_url, json=request_body, headers=header_params)

        return response

    def delete_order(self, access_token, order_id):

        order_update_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {"Authorization": access_token}

        response = requests.delete(order_update_url, headers=header_params)

        return response
