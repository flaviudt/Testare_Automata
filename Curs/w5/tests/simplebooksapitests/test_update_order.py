import unittest

from w5.requests.simplebooksapi.simple_books_requests import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):
    access_token = ""

    def setUp(self) -> None:
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_update_order_status_code(self):
        book_id = 1
        customer_name = "PYTA1"

        place_order_response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 201
        actual_status_code = place_order_response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Cannot place order")

        order_id = place_order_response.json()["orderId"]

        new_customer_name = "PYTA1_UPDATED"

        update_order_response = self.books_api.update_order(self.access_token, order_id, new_customer_name)

        expected_status_code = 204
        actual_status_code = update_order_response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")
