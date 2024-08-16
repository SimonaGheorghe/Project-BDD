import random
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    INPUT_FIRST_NAME = (By.ID, "firstname")
    INPUT_LAST_NAME = (By.ID, "lastname")
    INPUT_EMAIL = (By.ID, "email_address")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_PASSWORD_CONFIRMATION = (By.ID, "password-confirmation")
    BUTTON_REGISTER = (By.CSS_SELECTOR, ".action.submit")
    MESSAGE_SUCCESS_REGISTER = (By.CLASS_NAME, "message-success")
    REGISTER_PAGE_URL = 'https://magento.softwaretestingboard.com/customer/account/create/'

    ERROR_FIRST_NAME = (By.ID, "firstname-error")
    ERROR_LAST_NAME = (By.ID, "lastname-error")
    ERROR_EMAIL = (By.ID, "email_address-error")
    ERROR_PASSWORD = (By.ID, "password-error")
    ERROR_PASSWORD_CONFIRMATION = (By.ID, "password-confirmation-error")


    def open(self):
        self.driver.get(self.REGISTER_PAGE_URL)

    def set_first_name(self, first_name):
        # self.driver.find_element(*self.INPUT_FIRST_NAME).send_keys(first_name)
        self.type(self.INPUT_FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.type(self.INPUT_LAST_NAME, last_name)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_unique_email(self):
        number = random.randint(0, 99999)
        email_address = f"Popa-{number}@yahoo.com"
        self.set_email(email_address)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_password_confirm(self, text):
        self.type(self.INPUT_PASSWORD_CONFIRMATION, text)

    def click_register_button(self):
        self.find(self.BUTTON_REGISTER).click()

    def verify_success_message_displayed(self):
        assert self.find(self.MESSAGE_SUCCESS_REGISTER).is_displayed()

    def verify_success_message_contains_text(self, text):
        assert self.find(self.MESSAGE_SUCCESS_REGISTER).text == text

    def verify_url(self):
        assert self.driver.current_url == self.REGISTER_PAGE_URL


    def verify_first_name_error_displayed(self):
        assert self.find(self.ERROR_FIRST_NAME).is_displayed(), "first name not found"

    def verify_last_name_error_displayed(self):
        assert self.find(self.ERROR_LAST_NAME).is_displayed(), "last name not found"

    def verify_email_error_displayed(self):
        assert self.find(self.ERROR_EMAIL).is_displayed(), 'email not found'

    def verify_password_error_displayed(self):
        assert self.find(self.ERROR_PASSWORD).is_displayed(), 'password not found'

    def verify_error_displayed(self, locator, expected_message):
        element = self.find(locator)
        assert element.is_displayed(), "Error message is not displayed"
        assert element.text.strip() == expected_message, f"Expected message '{expected_message}', but got '{element.text.strip()}'"