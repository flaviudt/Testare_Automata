"""
1. Intrati pe site-ul https://www.elefant.ro/
"""
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestElefantPage(unittest.TestCase):
    LINK = 'https://www.elefant.ro/'
    SEARCH_BAR = (By.NAME, "SearchTerm")
    SEARCH_BTN = (By.NAME, "search")
    SITE_COOKIES = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    PRODUCT_PRICE = (By.CLASS_NAME, "current-price")
    ACCOUNT_BTN = (By.XPATH, "//*[@href='#account-layer']")
    SIGN_IN_BTN = (By.CLASS_NAME, "my-account-login")
    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BTN = (By.XPATH, "//button[@name='login']")
    ERROR_LOGIN_MSG = (By.XPATH, "//div[@role='alert']")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(1)

        # accept cookies
        cookies_btn_accept = self.driver.find_element(*self.SITE_COOKIES)
        cookies_btn_accept.click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_search_result_list(self):
        """
        - Cautam un produs la alegere (iphone 14)
        - Verificam ca s-au returnat
        cel putin 10 rezultate ([class="product-title"])
        """
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys('Iphone 14')
        time.sleep(2)

        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        search_btn.click()
        time.sleep(10)

        results = self.driver.find_elements(By.CLASS_NAME, "product-title")
        self.assertGreaterEqual(len(results), 10)

    def test_home_page_title(self):
        """
        4. Extrageti titlul paginii si verificati ca este corect
        """
        expected_page_title = "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"

        actual_page_title = self.driver.title
        self.assertEqual(expected_page_title, actual_page_title)

    def test_lowest_price_search_bar_results(self):
        """
        3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
        din primele 10 produse gasite
        (puteti sa va folositi de find_elements)
        """
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys('Iphone 14')
        time.sleep(2)

        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        search_btn.click()
        time.sleep(10)

        price_elements = self.driver.find_elements(*self.PRODUCT_PRICE)
        print(price_elements)

        prices = []

        for price_element in price_elements[:11]:
            price_list = price_element.text.split()
            print(price_list)
            price = float(price_list[0].replace(".", "").replace(",", "."))
            print(price)
            prices.append(price)
        print(prices)
        self.assertEqual(min(prices), 41.79)

    def test_login_invalid_credentials(self):
        """
        5. Intrati pe site, accesati butonul cont si click pe conectare.
        Identificati elementele de tip user si parola si inserati valori incorecte
        (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
        - Dati click pe butonul "conectare" si verificati urmatoarele:
                     1. Faptul ca nu s-a facut logarea in cont
                    2. Faptul ca se returneaza eroarea corecta
        """
        account_btn = self.driver.find_element(*self.ACCOUNT_BTN)
        account_btn.click()

        sign_in_button = self.driver.find_element(*self.SIGN_IN_BTN)
        sign_in_button.click()

        email = self.driver.find_element(*self.EMAIL)
        email.send_keys('invalidmail@yahoo.ro')
        time.sleep(2)

        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys('invalidpass')
        time.sleep(2)

        login_btn = self.driver.find_element(*self.LOGIN_BTN)
        login_btn.click()

        error_msg = self.driver.find_element(*self.ERROR_LOGIN_MSG)

        expected_error_msg = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
        actual_error_msg = error_msg.text
        self.assertEqual(expected_error_msg, actual_error_msg)

        self.assertNotIn('my-account', self.driver.current_url)

    def test_invalid_email_format(self):
        """
        6. Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
        si verificati faptul ca butonul "conectare" este dezactivat
        """
        account_btn = self.driver.find_element(*self.ACCOUNT_BTN)
        account_btn.click()

        sign_in_button = self.driver.find_element(*self.SIGN_IN_BTN)
        sign_in_button.click()

        email = self.driver.find_element(*self.EMAIL)
        email.send_keys("invalidemail")

        login_btn = self.driver.find_element(*self.LOGIN_BTN)
        self.assertFalse(login_btn.is_enabled())
