import unittest

from w5.requests.simplebooksapi.simple_books_requests import SimpleBooksRequests


class TestDeleteOrder(unittest.TestCase):

    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_delete_order_status_code(self):
        book_id = 1
        customer_name = "PYTA1"

        place_order_response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_order_status_code = 201
        actual_order_status_code = place_order_response.status_code

        self.assertEqual(expected_order_status_code, actual_order_status_code, "Unexpected status code for new order")

        order_id = place_order_response.json()["orderId"]

        delete_order_response = self.books_api.delete_order(self.access_token, order_id)

        expected_delete_status_code = 204
        actual_delete_status_code = delete_order_response.status_code
        
        self.assertEqual(expected_delete_status_code, actual_delete_status_code, "Unexpected status code for deleted order")
