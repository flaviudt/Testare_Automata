import time
import unittest

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class TestElefantPage(unittest.TestCase):
    LINK = "https://www.elefant.ro/"
    SEARCH_BOX = (By.CLASS_NAME, "js-has-overlay")
    SEARCH_BUTTON = (By.CLASS_NAME, "btn-search")
    COOKIE = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    SEARCH_RESULT = (By.CLASS_NAME, "search-result-headline")
    ACCOUNT_BUTTON = (By.XPATH, "(//*[@class='material-icons'])[4]")
    CONNECT_BUTTON = (By.XPATH, "//*[@class='my-account-login btn btn-primary btn-block']")
    EMAIL_BUTTON = (By.XPATH, "(//*[@class='form-control'])[1]")
    PASSWORD_BUTTON = (By.XPATH, "(//*[@class='form-control'])[2]")
    CONECTARE_BUTTON = (By.XPATH, "//button[@class='btn btn-primary btn-block']")

    def setUp(self):
        # # v1
        # # dezactivam notificarile pop-up
        # chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.default_content_setting_values.notifications": 2}
        # chrome_options.add_experimental_option("prefs", prefs)

        ## v2
        chrome_options = webdriver.ChromeOptions()
        # Working with the 'add_argument' Method to modify Driver Default Notification
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("start-maximized")

        # cream driverul
        self.driver = webdriver.Chrome(options=chrome_options)

        # acesam linkul www.elefant.ro
        self.driver.get(self.LINK)
        time.sleep(2)

        # maximizam fereastra browser
        # self.driver.maximize_window()

        # acceptam cookies
        cookie_cancel = self.driver.find_element(*self.COOKIE)
        cookie_cancel.click()
        time.sleep(1)
        # self.driver.find_element(By.CSS_SELECTOR, '[class ="back-to-site"]').click()
        # time.sleep(2)

    def tearDown(self):
        # inchidem browserul
        self.driver.quit()

    def test_homepage(self):
        """
        4. Extrageti titlul paginii si verificati ca este corect
        """
        homepage = self.driver.title
        expected_title = "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"
        self.assertEqual(homepage, expected_title, "Titlul nu corespunde cu cel din browser")

    def test_search_iphone14_list_items(self):
        """
        2. Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
        cel putin 10 rezultate ([class="product-title"])
        """
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.click()
        search.send_keys("iphone 14")

        search_enter = self.driver.find_element(*self.SEARCH_BUTTON)
        search_enter.click()
        time.sleep(1)

        iphone14_items = self.driver.find_elements(By.CSS_SELECTOR, '[class="product-title"]')
        print(len(iphone14_items))
        self.assertGreaterEqual(len(iphone14_items), 10)

    def test_search_iphone14_result_text(self):
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.click()
        search.send_keys("iphone 14")

        search_enter = self.driver.find_element(*self.SEARCH_BUTTON)
        search_enter.click()
        time.sleep(1)
        result_headline = self.driver.find_element(*self.SEARCH_RESULT)
        result_text = result_headline.text
        result_list = result_text.split()
        print(result_list)
        total_items = result_list[-2]
        self.assertGreaterEqual(int(total_items), 10)

    def test_get_minim_price(self):
        """
        3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
        din primele 10 produse gasite
        (puteti sa va folositi de find_elements)
        """
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.click()
        search.send_keys("iphone 14")
        search_enter = self.driver.find_element(*self.SEARCH_BUTTON)
        search_enter.click()
        time.sleep(1)

        total_current_prices = self.driver.find_elements(By.CSS_SELECTOR, '[class="current-price "]')
        current_prices = total_current_prices[:10]
        print(len(current_prices))
        prices = []
        for price in total_current_prices:
            price_info = price.text
            price_info_list = price_info.split()
            price_value = price_info_list[0]
            print(price_value)
            price_value_float = float(price_value.replace(".", "").replace(",", "."))
            prices.append(price_value_float)
        min_price = min(prices)
        print(f"Cel mai ieftin produs are valoarea: {min_price} lei")
        self.assertGreater(min_price, 10)

    def test_invalid_account(self):
        """
        5. Intrati pe site, accesati butonul cont si click pe conectare.
        Identificati elementele de tip user si parola si inserati valori incorecte
        (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
        - Dati click pe butonul "conectare" si verificati urmatoarele:
                     1. Faptul ca nu s-a facut logarea in cont
                    2. Faptul ca se returneaza eroarea corecta
        """
        self.driver.find_element(*self.ACCOUNT_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.CONNECT_BUTTON).click()
        email = self.driver.find_element(*self.EMAIL_BUTTON)
        password = self.driver.find_element(*self.PASSWORD_BUTTON)
        email.click()
        email.send_keys("flaviu@gmail.abc")
        password.click()
        password.send_keys("flaviu")
        time.sleep(1)
        self.driver.find_element(*self.CONECTARE_BUTTON).click()
        current_error = self.driver.find_element(By.XPATH, "//*[@class='alert alert-danger']").text
        expected_error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
        current_url = self.driver.current_url
        expected_url = "https://www.elefant.ro/INTERSHOP/web/WFS/elefant-elefantRO-Site/ro_RO/-/RON/ViewUserAccount-ProcessLogin"
        self.assertEqual(current_error, expected_error, "Eroarea afisata nu este acceasi cu cea asteptata!")
        self.assertEqual(current_url, expected_url, "Url-urile nu coincid")

    def test_invalid_email(self):
        """
        6. Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
        si verificati faptul ca butonul "conectare" este dezactivat
        """
        self.newsletter_cancel()
        self.driver.find_element(*self.ACCOUNT_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.CONNECT_BUTTON).click()
        email = self.driver.find_element(*self.EMAIL_BUTTON)
        time.sleep(1)
        email.send_keys("flaviu")
        conectare = self.driver.find_element(*self.CONECTARE_BUTTON)
        actual = conectare.get_property("disabled")
        expected = True
        self.assertEqual(actual, expected)

    def newsletter_cancel(self):
        newletter_x_button = (By.CLASS_NAME, "close")
        newletter_box = (By.CSS_SELECTOR, '[class ="weblayer--bar-subscription"]')
        ## class="weblayer--bar-subscription vertical-center horizontal-center enter-slide-up"
        try:
            self.driver.find_element(*newletter_x_button).click()
        except selenium.common.exceptions.NoSuchElementException:
            pass

