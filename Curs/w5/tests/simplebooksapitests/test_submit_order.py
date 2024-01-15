import unittest

from Curs.w5.requests.simplebooksapi.simple_books_requests import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):

    # Declaram access_token la nivel de clasa, ca sa folosim acelasi token la toate testele.
    # Initial va fi egal cu ""
    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_submit_order_status_code(self):
        book_id = 1
        customer_name = "PYTA1"

        response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 201
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        expected_created_message = True
        actual_created_message = response.json()["created"]

        self.assertEqual(expected_created_message, actual_created_message, "Unexpected message")

    def test_submit_order_with_invalid_book_id(self):
        book_id = -545
        customer_name = "PYTA1"

        response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 400
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        expected_error_message = "Invalid or missing bookId."
        actual_error_message = response.json()["error"]

        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error message.")
