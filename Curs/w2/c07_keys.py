import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestKeys(unittest.TestCase):

    USERNAME = (By.ID, "username")

    def setUp(self) -> None:
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.implicitly_wait(1)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_keys(self):
        user = self.driver.find_element(*self.USERNAME)
        user.send_keys("tmsmith")
        time.sleep(2)
        user.clear()
        user.send_keys("tmsmith")
        time.sleep(1)
        user.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        user.send_keys("tmsmith")
        time.sleep(1)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(1)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(1)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)
