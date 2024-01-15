import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCarturestiPage(unittest.TestCase):
    LINK = "https://carturesti.ro/"
    COOKIE = (By.XPATH, "//div[@class='cookieInfo container']//button")
    COMMAND_BUTTON = (By.XPATH, '//div[@class="homePage"]//a[@href="/coupon-checkout"]')
    H4_ELEMENT = (By.XPATH, '(//div[@class="homePage"]//h4)[1]')
    LOGIN_BTN = (By.XPATH, "(//button[@class='md-button md-ink-ripple'])[2]")
    USER_BTN = (By.ID, "loginTrigger")
    EMAIL_BTN = (By.ID, "loginform-email")
    PASSWORD_BTN = (By.ID, "loginform-password")
    AUTHENTICATION = (By.NAME, "login-button")
    SEARCH_BOX = (By.ID, "search-input")
    SORT_BOX_DROPDOWN = (By.ID, "select_value_label_4")
    ADD_TO_CART = (By.CLASS_NAME, "adauga-in-cos")
    CART = (By.CLASS_NAME, "checkout__text")
    ORDER_CONFIRM = (By.CLASS_NAME, "butonFinalizare")
    REMOVE_PRODUCT = (By.CLASS_NAME, "remove-product")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        cookie_cancel = self.driver.find_element(*self.COOKIE)
        cookie_cancel.click()

    def tearDown(self):
        self.driver.quit()

    def test_find_comamnd_button(self):
        """
        1. XPATH - Gaseste butonul "COMANDA-L AICI", incepand de la elementul div cu clasa homePage
        Verifica ca tag-ul acestuia este a.
        Da click pe buton si verifica ca link-ul curent este cel asteptat.
        """
        self.driver.find_element(*self.COMMAND_BUTTON).click()
        expected_url = "https://carturesti.ro/coupon-checkout"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Nu esti pe pagina asteptata!")

    def test_find_element(self):
        """
        2. XPATH - Gaseste elementul cu textul 'Împachetare gratuită'
        Verifica ca tag-ul acestuia este h4.
        """
        actual_tag = self.driver.find_element(*self.H4_ELEMENT).tag_name
        expected_tag = "h4"
        self.assertEqual(actual_tag, expected_tag, "Tag-urile difera")

    def test_find_div_element(self):
        """
        3. XPATH - cauta elementul div care se afla imediat dupa
        elementul de tip i cu clasa 'cartu-icons-giftbox'
        """
        div_element = self.driver.find_element(By.XPATH, '//*[@class="cartu-icons-giftbox"]/following-sibling::div')
        actual = div_element.tag_name
        expected = 'div'
        self.assertEqual(actual, expected, "Not Equal")

    def test_find_h4_element(self):
        """
        4. XPATH - cauta elementul h4 care se afla exact ianintea elementului
        span cu textul 'peste 120.000 de produse! '
        """
        actual = self.driver.find_element(By.XPATH, "(//span[@class='hidden-xs'])[1]/preceding-sibling::h4").tag_name
        expected = 'h4'
        self.assertEqual(actual, expected, "Not Equal")

    def test_login_existing_user(self):
        """
        5.LOGIN -> UTILIZATOR EXISTENT -> INTRODUCETI DATELE -> AUTENTIFICARE -> VERIFICARE EROARE
        """
        self.driver.find_element(*self.LOGIN_BTN).click()
        time.sleep(1)
        self.driver.find_element(*self.USER_BTN).click()
        time.sleep(1)
        email = self.driver.find_element(*self.EMAIL_BTN)
        password = self.driver.find_element(*self.PASSWORD_BTN)
        email.click()
        email.send_keys("flaviu@gmail.abc")
        password.click()
        password.send_keys("flaviu")
        time.sleep(2)
        self.driver.find_element(*self.AUTHENTICATION).click()
        time.sleep(1)
        error = self.driver.find_element(By.XPATH, "(//*[@class='help-block'])[3]")
        actual_error = error.text
        expected_error = "Adresă de email sau parolă incorectă."
        self.assertEqual(actual_error, expected_error, "Not Equal")

    def test_cautare_python_books(self):
        """
        6.CAUTARE -> "python" -> ENTER -> SORTARE -> PRET(descendent) -> PRIMA -> ADAUGA IN COS -> COS ->
        -> FINALIZARE COMANDA -> X (sterge produsul)
        """
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.click()
        search.send_keys("PYTHON")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(*self.SORT_BOX_DROPDOWN).click()
        time.sleep(2)
        self.driver.find_element(By.ID, "select_option_31").click()
        time.sleep(2)
        first = self.driver.find_element(By.XPATH, "(//*[@class='md-title ng-binding'])[1]")
        first.click()
        time.sleep(2)
        self.driver.find_element(*self.ADD_TO_CART).click()
        self.driver.find_element(*self.CART).click()
        time.sleep(4)
        self.driver.find_element(*self.ORDER_CONFIRM).click()
        time.sleep(2)
        self.driver.find_element(*self.REMOVE_PRODUCT).click()
        time.sleep(1)
        current_url = self.driver.current_url
        expected_url = "https://carturesti.ro/site/empty-cart"
        self.assertEqual(current_url, expected_url, "Eroare")

    def test_get_minim_price(self):
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.click()
        search.send_keys("istorie")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        total_current_prices = self.driver.find_elements(By.CSS_SELECTOR, '[class ="suma"]')
        prices = []
        for price in total_current_prices:
            price_info = price.text
            price_value_float = float(price_info)
            print(price_value_float)
            prices.append(price_value_float)
        min_price = min(prices)
        print(f"Cel mai ieftin produs are valoarea {min_price} lei")
        self.assertLess(min_price, 100)

