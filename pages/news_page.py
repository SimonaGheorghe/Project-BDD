from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class WhatsNewPage(BasePage):

    BUTTON_NEW_YOGA = (By.CSS_SELECTOR, ".more.button")
    MESSAGE_NEW_LUMA = (By.ID, "page-title-heading")

    def open(self, url):
        self.driver.get(url)

    def verify_url(self, url):
        assert self.driver.current_url == url

    def click_shop_new_yoga_button(self):
        self.find(self.BUTTON_NEW_YOGA).click()
    def verify_url_new_collection(self, expected_url):
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)

        print("URL-ul asteptat:", expected_url)
        assert self.driver.current_url == expected_url
    def verify_success_new_message_displayed(self, title):
        assert self.find(self.MESSAGE_NEW_LUMA).is_displayed(title)