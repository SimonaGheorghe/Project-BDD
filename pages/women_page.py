
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class WomenPage(BasePage):

    BUTTON_WOMEN_TEES = (By.XPATH, "//span[@class='more icon' and contains(text(), 'Women’s Tees')]")
    MESSAGE_TEES = (By.XPATH, "//span[@class='base' and @data-ui-id='page-title-wrapper']")

    def open(self, url):
        self.driver.get(url)

    def verify_url(self, url):
        assert self.driver.current_url == url

    def click_women_tees_button(self):
        self.find(self.BUTTON_WOMEN_TEES).click()

    def verify_url_women_tees(self, expected_url):
        current_url = self.driver.current_url
        print("Current URL:", current_url)

        print("Expected URL:", expected_url)
        assert self.driver.current_url == expected_url