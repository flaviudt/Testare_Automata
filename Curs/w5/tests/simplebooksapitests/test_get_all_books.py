import unittest

from w5.requests.simplebooksapi.simple_books_requests import SimpleBooksRequests


class TestGetAllBooks(unittest.TestCase):

    def setUp(self):
        self.books_api = SimpleBooksRequests()

    def test_get_all_books_status_code_without_filter(self):
        response = self.books_api.get_all_books()

        expected_status_code = 200
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

    def test_get_all_books_number_of_results_without_filter(self):
        response = self.books_api.get_all_books()

        expected_number_of_results = 6
        actual_number_of_results = len(response.json())

        # print(response.json()[0])

        self.assertEqual(expected_number_of_results, actual_number_of_results, "Unexpected number of result")

    def test_get_all_books_filter_by_valid_limit(self):

        response = self.books_api.get_all_books(limit=3)

        expected_number_of_results = 3
        actual_number_of_results = len(response.json())

        # print(response.json())

        self.assertEqual(expected_number_of_results, actual_number_of_results, "Unexpected number of result")

    def test_get_all_books_filter_by_invalid_limit_greater_than_20(self):

        response = self.books_api.get_all_books(limit=25)

        expected_status_code = 400
        actual_status_code = response.status_code

        expected_error_message = "Invalid value for query parameter 'limit'. Cannot be greater than 20."
        actual_error_message = response.json()["error"]

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")
        self.assertEqual(expected_error_message, actual_error_message)

    def test_get_all_books_filter_by_invalid_limit_less_than_0(self):

        response = self.books_api.get_all_books(limit=-1)

        expected_status_code = 400
        actual_status_code = response.status_code

        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 0."
        actual_error_message = response.json()["error"]

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")
        self.assertEqual(expected_error_message, actual_error_message)

    def test_get_all_books_filter_by_type_fiction(self):

        response = self.books_api.get_all_books(book_type="fiction")

        expected_status_code = 200
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status")

        expected_type = "fiction"

        for i in range(len(response.json())):
            current_book = response.json()[i]
            actual_type = current_book["type"]

            self.assertEqual(expected_type, actual_type, f"Unexpected type for book '{current_book['name']}'")

    def test_get_all_books_filter_by_type_non_fiction(self):

        response = self.books_api.get_all_books(book_type="non-fiction")

        expected_status_code = 200
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status")

        expected_type = "non-fiction"

        for i in range(len(response.json())):
            current_book = response.json()[i]
            actual_type = current_book["type"]

            self.assertEqual(expected_type, actual_type, f"Unexpected type for book '{current_book['name']}'")
