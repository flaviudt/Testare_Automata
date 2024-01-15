import unittest
import HtmlTestRunner

from SW5.tests.test_carts import TestCartsRequests
from SW5.tests.test_users import TestUsersRequests
from SW5.tests.test_products import TestProductsRequests
from SW5.tests.test_posts import TestPostsRequests


class TestSuite(unittest.TestCase):

    def test_suite(self):

        suita_teste = unittest.TestSuite()

        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestProductsRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUsersRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCartsRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPostsRequests)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API test report",
            report_name="Dummyjson API Test Results"
        )

        runner.run(suita_teste)

