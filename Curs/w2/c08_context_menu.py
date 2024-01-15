import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


"""
Clasa ActionChains din Selenium ne ajuta sa simulam anumite actiuni pe care driverul (clasa WebDriver) 
nu le are implementate:

- Context click (click dreapta)
- Dublu click
- Drag and drop
- Scroll
- Apasare du butoane, inclusiv cele speciale (CTRL, ALT, etc) sau combinatii de butoane (CTRL + A)
- etc
"""

class TestContextMenu(unittest.TestCase):
    BOX = (By.ID, "hot-spot")

    def setUp(self) -> None:
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    # vom deschide un meniu cu click dreapta
    def test_context_menu(self):
        action = ActionChains(self.driver)
        elem = self.driver.find_element(*self.BOX)
        action.context_click(elem).perform()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
