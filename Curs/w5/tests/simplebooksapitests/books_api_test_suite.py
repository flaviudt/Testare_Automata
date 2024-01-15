import unittest

import HtmlTestRunner

from Curs.w5.tests.simplebooksapitests.test_api_status import TestApiStatus
from Curs.w5.tests.simplebooksapitests.test_delete_order import TestDeleteOrder
from Curs.w5.tests.simplebooksapitests.test_get_all_books import TestGetAllBooks
from Curs.w5.tests.simplebooksapitests.test_submit_order import TestSubmitOrder
from Curs.w5.tests.simplebooksapitests.test_update_order import TestUpdateOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):

        suita_teste = unittest.TestSuite()

        # adaugam testele in suita
        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteOrder)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API test report",
            report_name="Books API Test Results"
        )

        runner.run(suita_teste)