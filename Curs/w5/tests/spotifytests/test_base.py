import unittest


# Clasa de baza in care se pot pune metodele pe care le folosim mai des
class TestBase(unittest.TestCase):

    def verify_status_code(self, expected, actual):
        self.assertEqual(expected, actual, "Unexpected status code")

    def verify_response_size(self, expected, actual):
        self.assertEqual(expected, len(actual), "Unexpected response size")
