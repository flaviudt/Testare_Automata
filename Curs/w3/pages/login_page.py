from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    # (By.XPATH, "//div[contains(@class, 'message-error')]")
    ERROR_MESSAGE_MAIN = (By.CSS_SELECTOR, "div.message-error")
    ERROR_MESSAGE_EMAIL = (By.ID, "Email-error")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        self.type(self.INPUT_EMAIL, email)

    def set_password(self, password):
        # self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.type(self.INPUT_PASSWORD, password)

    def click_login_button(self):
        # self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.click(self.BUTTON_LOGIN)

    def is_main_error_message_displayed(self):
        # return self.find(self.ERROR_MESSAGE_MAIN).is_displayed()
        return self.is_displayed(self.ERROR_MESSAGE_MAIN)

    def get_main_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE_MAIN)

    def is_email_error_message_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE_EMAIL)

    def get_email_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE_EMAIL)

