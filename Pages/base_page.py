import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from browser import Browser


class BasePage(Browser):
    INPUT_SEARCH = (By.ID, "search")
    BUTTON_ACTION_SEARCH = (By.CSS_SELECTOR, ".action.search")
    CART_QTY = (By.CLASS_NAME, "counter-number")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def set_search_term(self, text):
        self.type(self.INPUT_SEARCH, text)

    def click_search_magnifying_button(self):
        self.find(self.BUTTON_ACTION_SEARCH).click()

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def verify_cart_quantity(self, expected):
        time.sleep(5)
        assert f'{expected}' in self.find(self.CART_QTY).text