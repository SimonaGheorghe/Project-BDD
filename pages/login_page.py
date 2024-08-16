from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    BUTTON_FIRST_ACTION = (By.CLASS_NAME, "fc-button-label")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "pass")
    BUTTON_LOGIN = (By.ID, "send2")
    DIV_ERROR = (By.CLASS_NAME, "message-error")

    def open(self, url):
        self.driver.get(url)

    def click_consent_button(self):
        self.find(self.BUTTON_FIRST_ACTION).click()

    def verify_url(self, url):
        assert self.driver.current_url == url


    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_signin_button(self):
        self.find(self.BUTTON_LOGIN).click()

    def verify_signin_error_message(self, text):
        assert text in self.find(self.DIV_ERROR).text