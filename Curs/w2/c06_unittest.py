import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
########### Libraria unittest ###########

Libraria unittest ofera suport pentru crearea de teste rulabile direct in interiorul clasei.
Se implementeaza prin mostenirea clasei TestCase din libraria unittest
Orice clasa de teste trebuie sa mosteneasca clasa TestCase si sa aiba urmatoarele particularitati:
1. metoda setUp() -> toate activitatile care trebuie sa fie executate inainte de ORICE TEST din clasa respectiva
2. metoda teardown() -> toate activitatile care trebuie sa fie executate dupa de ORICE TEST din clasa respectiva
3. toate metodele de test trebuie sa aiba prefixul test_

* = despachetare tuplu
driver.find_elements(*BUTTON_JS_ALERT_SIMPLE) <=> driver.find_elements(By.CSS_SELECTOR, "[onclick='jsAlert()']")
"""


class Test(unittest.TestCase):
    driver = None
    LOGIN_LINK = "https://the-internet.herokuapp.com/login"
    BUTTON_LOGIN = (By.CLASS_NAME, "fa-sign-in")
    MESSAGE_SUCCESS = (By.CLASS_NAME, "alert-success")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SECURE_AREA = (By.XPATH, "//div[@class='flash success']")

    # suprascriem metoda setUp care va rula inainte de fiecare test
    def setUp(self):
        # print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver = webdriver.Chrome()
        self.driver.get(self.LOGIN_LINK)
        self.driver.maximize_window()
        time.sleep(1)

    # suprascriem metoda tearDown care va rula dupa fiecare test
    def tearDown(self):
        # print(f"Se executa ce este in tearDown() pentru {self._testMethodName}\n")
        self.driver.quit()

    # TEST 1
    # - Verifica daca URL-ul paginii este corect
    def test_url(self):
        actual_url = self.driver.current_url

        # assert expected_url == actual_url, f"Unexpected URL, expected {expected_url}, but found {actual_url}"

        # Varianta unittest pentru assert de egalitate
        self.assertEqual(self.LOGIN_LINK, actual_url, "Unexpected URL")

    # TEST 2
    # - Verifica daca titlul paginii apare corect
    def test_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title

        # assert expected_title == actual_title, f"Unexpected title, expected {expected_title}, but found {actual_title}"
        self.assertEqual(expected_title, actual_title, "Unexpected title")

    # TEST 3
    # - Verifica daca textul de pe elementul xpath=//h2 e corect
    def test_h2_text(self):
        text_h2 = self.driver.find_element(By.XPATH, "//h2").text
        expected_text = "Login Page"
        # assert expected_text == text_h2, f"Invalid h2 text, expected {expected_text}, but found {text_h2}"
        # Observam ca folosind assertEqual, nu mai trebuie scrisa partea cu 'expected x but
        # found y' deoarece se specifica implicit prin aceasta metoda
        self.assertEqual(expected_text, text_h2, "Textul h2 este incorect")

    # TEST 4
    # - Verifica daca butonul de login este displayed
    def test_buton_login_display(self):
        login_button = self.driver.find_element(*self.BUTTON_LOGIN)
        assert login_button.is_displayed(), "Butonul de Login nu este afisat"

    # TEST 5
    # - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_atribut_href(self):
        expected_href = "http://elementalselenium.com/"

        # luam atributul de tip "href" de pe acel element de tip a
        actual_href = self.driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']").get_attribute("href")

        self.assertEqual(expected_href, actual_href, "Link-ul 'href' este incorect")

    # TEST 6
    # - Lasă goale user și pass;
    # - Click login;
    # - Verifică dacă eroarea e displayed
    def test_blank_login(self):
        # Facem click pe butonul de login fara sa completam vreun camp
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        eroare = self.driver.find_element(By.ID, "flash")
        assert eroare.is_displayed(), "Eroarea nu este afisata dupa logare fara Username/Password"

    # TEST 7
    # - Completează cu user și pass invalide;
    # - Click login;
    # - Verifică dacă mesajul de pe eroare e corect;
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos:
    #   expected = 'Your username is invalid!'
    #   self.assertTrue(expected in actual, 'Error message text is incorrect')
    def test_invalid_login(self):
        username = self.driver.find_element(*self.USERNAME)
        username.send_keys("wrong_user")
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("wrong_password")
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        expected_message = "Your username is invalid!"
        actual_message = self.driver.find_element(By.ID, "flash").text  # luam textul; am testat si ia inclusiv *

        # Assert pentru a verifica daca o expresie este adevarata
        # Metoda assertTrue() primeste 2 parametri:
        #   * primul param - expresia de evaluat
        #   * al doilea param - (optional) mesajul de eroare afisat
        self.assertTrue(expected_message in actual_message, "Mesajul de eroare nu este corect")

    # metoda ajutatoare - ea nu va fi rulata ca test pentru ca nu are prefixul test_
    # metoda are 2 parametri:
    # 1 - element_locator: locatorul elementului dupa care asteptam sa apara
    # 2 - seconds_to_wait: numarul maxim de secunde de asteptare pentru ca elementul sa apara
    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

    # metoda ajutatoare - asteapta ca un element sa devina ABSEENT in HTML (absent != invizibil)
    # metoda are 2 parametri:
    # 1 - element_locator: locatorul elementului dupa care asteptam sa dispara
    # 2 - seconds_to_wait: numarul maxim de secunde de asteptare pentru ca elementul sa dispare
    # Observate: cu EC.none_of() se neaga conditia din EC (EC = expected_condition)
    def wait_for_element_to_disappear(self, element, timp):
        wait = WebDriverWait(self.driver, timp)
        return wait.until(EC.none_of(EC.presence_of_element_located(element)))

    # metoda ajutatoare - returneaza TRUE daca elementul este PREZENT (prezent nu inseamna ca e si vizibil neaparat)
    # - metoda are ca parametru variabila element_locator: locatorul elementului dupa care asteptam sa dispara
    # - folosind driver.find_elements() putem sa ne dam seama daca un element este sau nu prezent
    # - driver.find_elements() nu da eroare daca nu gaseste un element dupa un locator dat, ci returneaza o lista goala
    # - daca lista e goala, inseamna ca nu e elementul prezent [len(lista) = 0 deci return FALSE]
    # - daca lista nu e goala, inseamna ca avem cel putin un element gasit [len(lista) > 0 deci return TRUE]
    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0  # daca nu gaseste nimic, returneaza o lista goala

    # TEST 8
    # - Lasă goale user și pass;
    # - Click login;
    # - Apasă x la eroare;
    # - Verifică dacă eroarea a dispărut
    def test_eroare_message_disappears_on_click(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        self.driver.find_element(By.CLASS_NAME, "close").click()
        self.wait_for_element_to_disappear((By.ID, "flash"),
                                           3)  # pt ca nu dispare din prima, dureaza putin sa dispara dupa ce dai x
        # self.assertFalse(self.is_element_present((By.ID, "flash")), "Mesajul de eroare nu a disparut")
        self.assertTrue(not self.is_element_present((By.ID, "flash")), "Mesajul de eroare nu a disparut")

    # TEST 9 - Ia ca o listă toate //label; - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
    # - Aici e ok să avem 2 asserturi

    def test_text_asteptat(self):
        lista_label = self.driver.find_elements(By.XPATH, "//label")
        # print(lista_label)
        expected_label_text_1 = "Username"
        actual_label_text_1 = lista_label[0].text
        expected_label_text_2 = "Password"
        actual_label_text_2 = lista_label[1].text
        self.assertEqual(expected_label_text_1, actual_label_text_1, "Textul de pe label nu coincide")
        self.assertEqual(expected_label_text_2, actual_label_text_2, "Textul de pe label nu coincide")

    # TEST 10
    # - Completează cu user și pass valide;
    # - Click login;
    # - Verifică ca noul url CONTINE stringul /secure;
    # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # - Verifică dacă elementul cu clasa=’flash succes’ este displayed;
    # - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    def test_valid_login(self):
        username = self.driver.find_element(*self.USERNAME)
        username.send_keys("tomsmith")
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("SuperSecretPassword!")
        self.driver.find_element(*self.BUTTON_LOGIN).click()

        actual_url = self.driver.current_url
        self.assertIn("/secure", actual_url), "Noul URL nu contine '/secure'"
        element_flash_success = self.wait_for_element_to_be_present(self.SECURE_AREA, 3)
        self.assertTrue(element_flash_success.is_displayed(), "Elementul nu este afisat")

        mesaj = self.driver.find_element(*self.SECURE_AREA).text
        self.assertIn("secure area", mesaj, "Mesajul nu contine textul 'secure area!'")

    # TEST 11
    # - Completează cu user și pass valide;
    # - Click login;
    # - Click logout;
    # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    def test_logout(self):
        self.test_valid_login()
        logout_button = self.driver.find_element(By.CLASS_NAME, "icon-signout")
        logout_button.click()
        actual_url = self.driver.current_url
        self.assertEqual(self.LOGIN_LINK, actual_url, "Linkurile nu sunt la fel")

    # TEST 12 - Completează user tomsmith;
    # - Găsește elementul //h4;
    # - Ia textul de pe el și fă split după spațiu.
    # - Consideră fiecare cuvânt ca o potențială parolă;
    # - Folosește o structură iterativă prin care să introduci rând pe rând parolele și să apeși pe login;
    # - La final trebuie afisam in consola fie ‘Nu am reușit să găsesc parola’, fie ‘Parola secretă este... [parola]’
    def test_brute_force(self):
        element_h4 = self.driver.find_element(By.XPATH, "//h4").text
        potentiale_parole = element_h4.split(" ")
        for parola in potentiale_parole:
            username = self.driver.find_element(*self.USERNAME)
            username.send_keys("tomsmith")
            password = self.driver.find_element(*self.PASSWORD)
            password.send_keys(str(parola))
            self.driver.find_element(*self.BUTTON_LOGIN).click()
            mesaj_eroare = (By.XPATH, "//div[@class='flash error']")
            if self.is_element_present(mesaj_eroare):
                print("Inca nu am gasit parola")
            else:
                print(f"Parola secreta este '{parola}'")
                break

    # Excludem testul in timpul rularii cu ajutorul decoratorului @unittest.skip
    @unittest.skip
    def test_picat(self):
        assert False, "Test picat"

    # def test_login1(self):
    #     pass
    #
    # def test_login2(self):
    #     self.login3()
    #     pass
    #
    # def login3(self):
    #     print("Se executa codul din login3()")
    #     pass
