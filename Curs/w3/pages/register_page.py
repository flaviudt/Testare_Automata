import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

import random

class RegisterPage(BasePage):

    REGISER_PAGE_URL = "https://demo.nopcommerce.com/register"
    RADIO_BUTTON_MALE = (By.ID, "gender-male")
    RADIO_BUTTON_FEMALE = (By.ID, "gender-female")
    INPUT_FIRST_NAME = (By.ID, "FirstName")
    INPUT_LAST_NAME = (By.ID, "LastName")
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_COMPANY_NAME = (By.ID, "Company")
    DROPDOWN_DAY = (By.NAME, "DateOfBirthDay")
    DROPDOWN_MONTH = (By.NAME, "DateOfBirthMonth")
    DROPDOWN_YEAR = (By.NAME, "DateOfBirthYear")
    CHECKBOX_NEWSLETTER = (By.ID, "Newsletter")
    INPUT_PASSWORD = (By.ID, "Password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "ConfirmPassword")
    BUTTON_REGISTER = (By.ID, "register-button")
    MESSAGE_SUCCESS = (By.CLASS_NAME, "result")

    def navigate_to_register_page(self):
        self.driver.get(self.REGISER_PAGE_URL)

    def click_male_radio_button(self):
        self.click(self.RADIO_BUTTON_MALE)

    def click_female_radio_button(self):
        self.click(self.RADIO_BUTTON_FEMALE)

    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_random_email(self):
        random_number = random.randint(1, 99999999999999999999999999)
        adresa_email = f'python@itfactory{random_number}.ro'
        self.type(self.INPUT_EMAIL, adresa_email)

    def set_company_name(self, text):
        self.type(self.INPUT_COMPANY_NAME, text)

    def select_day_of_birth(self, day):
        self.select_dropdown_option_by_text(self.DROPDOWN_DAY, day)

    def select_month_of_birth(self, month):
        self.select_dropdown_option_by_text(self.DROPDOWN_MONTH, month)

    def select_year_of_birth(self, year):
        self.select_dropdown_option_by_text(self.DROPDOWN_YEAR, year)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_password_confirm(self, text):
        self.type(self.INPUT_PASSWORD_CONFIRM, text)

    def click_register_button(self):
        self.click(self.BUTTON_REGISTER)

    def is_success_message_displayed(self):
        return self.is_displayed(self.MESSAGE_SUCCESS)

    def check_newsletter_checkbox(self):
        self.check_checkbox(self.CHECKBOX_NEWSLETTER)


