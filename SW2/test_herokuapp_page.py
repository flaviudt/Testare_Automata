import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TestHeroukappPage(unittest.TestCase):
    LINK = 'https://the-internet.herokuapp.com/'
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CLASS_NAME, "radius")
    LOGOUT_BTN = (By.CLASS_NAME, "radius")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_get_to_form_authentication(self):
        """
        2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
        Incearca mai multe variante posibile.
        """
        login_page = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        login_page.click()
        curent_title = self.driver.title
        expected_title = "The Internet"
        self.assertEqual(curent_title, expected_title)

    def test_check_login_page(self):
        """
        3. Identifica elementul ce contine textul "Login Page"
        si verifica, folosind un assert, ca acest element are textul asteptat
        """
        self.driver.find_element(By.XPATH, "//a[@href='/login']").click()
        login_page = self.driver.find_element(By.XPATH, "//h2")
        actual = login_page.text
        expected = "Login Page"
        self.assertEqual(actual, expected)

    def test_login(self):
        """
        4. Identifica input-urile username si password,
        introdu valori valide, si da click pe butonul login
        """
        self.driver.find_element(By.XPATH, "//a[@href='/login']").click()
        self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        time.sleep(1)
        self.driver.find_element(*self.LOGIN_BTN).click()
        time.sleep(1)
        expected_url = "https://the-internet.herokuapp.com/secure"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)

    def test_logout(self):
        """
        6. Da click pe butonul logout
        """
        self.test_login()
        time.sleep(1)
        self.driver.find_element(*self.LOGOUT_BTN).click()
        actual = self.driver.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual,expected)

    def test_invalid_login(self):
        """
        7. Introdu un username corect si o parola incorecta.
        Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
        """
        self.test_logout()
        time.sleep(1)
        self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPass")
        self.driver.find_element(*self.LOGIN_BTN).click()
        expected_error = 'Your password is invalid!'
        actual_error = self.driver.find_element(By.XPATH, '//*[@id="flash"]').text
        self.assertIn(expected_error, actual_error)

    def test_split_password(self):
        """
        8. Introdu un username corect.
        Gaseste elementul cu tag-ul h4.
        Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
        Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
        La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este [parola]"
        """
        self.driver.find_element(By.XPATH, "//a[@href='/login']").click()
        h4 = self.driver.find_element(By.CLASS_NAME,"subheader")
        possible_pass = h4.text.split()
        for elem in possible_pass:
            username = self.driver.find_element(*self.USERNAME)
            username.send_keys("tomsmith")
            password = self.driver.find_element(*self.PASSWORD)
            password.send_keys(str(elem))
            self.driver.find_element(*self.LOGIN_BTN).click()

            expected_url = "https://the-internet.herokuapp.com/secure"
            actual_url = self.driver.current_url
            if expected_url == actual_url:
                print(f"Parola secreta este {elem}")
                break
        else:
            print("Nu am reusit sa gasesc parola")








