from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class WhatsNewPage(BasePage):

    BUTTON_ECO = (By.XPATH, "//span[contains(@class, 'more icon') and contains(text(), 'Shop Eco Friendly')]")
    MESSAGE_ECO = (By.XPATH, "//span[@class='base' and contains(text(), 'Eco Collection New')]")
    BUTTON_LAYLA = (By.CSS_SELECTOR, 'strong.product-item-name a.product-item-link[title="Layla Tee"]')
    BUTTON_WISHLIST = (By.CSS_SELECTOR, 'a.action.towishlist')
    MESSAGE_LAYLA = (By.CLASS_NAME, 'message-success')
    BUTTON_ADDTOCART = (By.CSS_SELECTOR, 'button[data-role="all-tocart"]')
    MESSAGE_ERROR = (By.CSS_SELECTOR, 'div.messages')


    def open(self, url):
        self.driver.get(url)

    def verify_url(self, url):
        assert self.driver.current_url == url

    def click_shop_eco_button(self):
        self.find(self.BUTTON_ECO).click()

    def verify_url_new_collection(self, expected_url):
        current_url = self.driver.current_url
        print("Current URL:", current_url)

        print("Expected URL:", expected_url)
        assert self.driver.current_url == expected_url

    def verify_success_message_contains_text(self, expected_text="Eco Collection New"):
        success_message_element = self.find(self.MESSAGE_ECO)
        success_message = success_message_element.text
        print("Actual success message:", success_message)
        print("Expected text:", expected_text)
        assert expected_text in success_message, f"Expected '{expected_text}' to be in '{success_message}'"

    def open2(self, url):
        self.driver.get(url)
        time.sleep(5)

    def click_item_tee(self):
        self.find(self.BUTTON_LAYLA).click()

    def click_wishlist(self):
        self.find(self.BUTTON_WISHLIST).click()
        time.sleep(5)

    def verify_url_wishlist(self, expected_base_url):
        current_url = self.driver.current_url
        print("Current URL:", current_url)

        base_url_part = current_url.split('/wishlist_id/')[0]

        if base_url_part == expected_base_url:
            print("URL verification passed.")
        else:
            print("URL verification failed.")
            raise AssertionError(f"Expected URL to start with '{expected_base_url}', but got '{current_url}'")


    def verify_message_layla(self, expected_text = "Layla Tee has been added to your Wish List. Click here to continue shopping."):
        success_message_element = self.find(self.MESSAGE_LAYLA)
        success_message = success_message_element.text
        print("Actual success message:", success_message)
        print("Expected text:", expected_text)
        assert expected_text in success_message, f"Expected '{expected_text}' to be in '{success_message}'"
        time.sleep(3)

    def click_addtocart(self):
        self.find(self.BUTTON_ADDTOCART).click()

    def verify_error_message(self, expected_error='You need to choose options for your item for "Layla Tee".'):
        error_message_element = self.find(self.MESSAGE_ERROR)
        error_message = error_message_element.text
        print("Actual success message:", error_message)
        print("Expected text:", expected_error)
        assert expected_error in error_message, f"Expected '{expected_error}' to be in '{error_message}'"