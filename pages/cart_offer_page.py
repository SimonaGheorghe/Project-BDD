
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


import time

from pages.base_page import BasePage


class WomenOffer(BasePage):

    BUTTON_WOMEN = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/women.html' and @id='ui-id-4']")
    BUTTON_WOMEN_TEES = (By.XPATH, "//span[@class='more icon' and contains(text(), 'Women’s Tees')]")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "a.product-item-link[href='https://magento.softwaretestingboard.com/desiree-fitness-tee.html']")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".action.primary.tocart")
    BUTTON_SELECT_SIZE = (By.ID, "option-label-size-143-item-167")
    BUTTON_SELECT_COLOR = (By.ID, 'option-label-color-93-item-49')
    BUTTON_SHOW_CART = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/checkout/cart/' and contains(@class, 'action showcart')]")
    BUTTON_EDIT_CART = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/checkout/cart/' and contains(@class, 'action viewcart')]")
    BUTTON_EDIT_QTY = (By.CSS_SELECTOR, 'input[data-cart-item-id="WS05-S-Black"]')
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, 'button[data-role="proceed-to-checkout"]')
    SUMMARY_SECTION = (By.CSS_SELECTOR, '.cart-summary')


    INPUT_STREET = (By.NAME, 'street[0]')
    INPUT_CITY = (By.NAME, 'city')
    SELECT_STATE = (By.NAME, 'region_id')
    INPUT_POSTCODE = (By.NAME, 'postcode')
    SELECT_COUNTRY = (By.NAME, 'country_id')
    INPUT_TELEPHONE = (By.NAME, 'telephone')
    SHIPPING_METHODS = (By.NAME, 'ko_unique_1')
    BUTTON_NEXT = (By.CSS_SELECTOR, 'button[data-role="opc-continue"]')
    BUTTON_PLACE_ORDER = (By.CSS_SELECTOR, 'button.action.primary.checkout')
    MESSAGE_ORDER_SUCCESS = (By.CLASS_NAME, "page-title")
    ACCOUNT_MENU = (By.XPATH, '//button[@class="action switch" and @data-action="customer-menu-toggle"]')
    SIGN_OUT_BUTTON = (By.XPATH, '//li[@class="link authorization-link"]')
    SIGN_OUT_MESSAGE =  (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')


    def click_product_item(self):
        self.find(self.PRODUCT_TITLE).click()

    def click_size(self):
        self.find(self.BUTTON_SELECT_SIZE).click()
    def click_color(self):
        self.find(self.BUTTON_SELECT_COLOR).click()
    def click_add_to_cart(self):
        self.find(self.BUTTON_ADD_TO_CART).click()
        time.sleep(10)


    def click_show_cart_qty(self):
        cart_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.BUTTON_SHOW_CART))
        cart_button.click()

    def click_view_cart_details(self):
        button_edit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BUTTON_EDIT_CART))
        button_edit.click()


    def discount(self):
        time.sleep(10)
        cart_price_selector = "span.cart-price span.price"
        total_price_selector = "span.price[data-bind='text: getValue()']"
        checkout_button_selector = 'button[data-role="proceed-to-checkout"]'
        quantity_label_xpath = "//input[contains(@class, 'input-text qty') and @data-role='cart-item-qty']"


        cart_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, cart_price_selector))
        )
        cart_price = cart_price_element.text.strip().replace('$', '')


        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, total_price_selector))
        )
        total_price = total_price_element.text.strip().replace('$', '')

        if cart_price == total_price:
            quantity_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, quantity_label_xpath)))
            quantity_input.click()
            quantity_input.clear()
            quantity_input.send_keys('4')
            quantity_input.send_keys(Keys.RETURN)

            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element_value((By.XPATH, quantity_label_xpath), '4')
            )

            checkout_button = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, checkout_button_selector))
            )
            checkout_button.click()

        else:
            checkout_button = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, checkout_button_selector))
            )
            checkout_button.click()


    def verify_url_shipping(self, expected_url):
        current_url = self.driver.current_url
        print("Current URL:", current_url)
        print("Expected URL:", expected_url)
        assert self.driver.current_url == expected_url

    def set_street_address(self, text):
        self.type(self.INPUT_STREET, text)

    def set_city(self, text):
        self.type(self.INPUT_CITY, text)

    def select_state(self, text):
        dropdown = self.find(self.SELECT_STATE)
        Select(dropdown).select_by_visible_text(text)

    def set_postal_code(self, number):
        self.type(self.INPUT_POSTCODE, number)

    def select_country(self, text):
        dropdown = self.find(self.SELECT_COUNTRY)
        Select(dropdown).select_by_visible_text(text)

    def set_phone_number(self, number):
        self.type(self.INPUT_TELEPHONE, number)

    def click_shipping_methods(self):
        self.find(self.SHIPPING_METHODS).click()

    def click_next_button(self):
        self.find(self.BUTTON_NEXT).click()

    def click_place_order_button(self):
        time.sleep(3)
        self.find(self.BUTTON_PLACE_ORDER).click()

    def verify_url_order(self, expected_url):
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)

        print("URL-ul asteptat:", expected_url)
        assert self.driver.current_url == expected_url

    def verify_success_message_displayed(self):
        self.driver.implicitly_wait(10)
        assert self.find(self.MESSAGE_ORDER_SUCCESS).is_displayed()

    def verify_success_message_contains_text(self, text):
        success_message = self.find(self.MESSAGE_ORDER_SUCCESS).text
        print("Succes message is: ", success_message)
        print("Expected message is: ", text)
        assert success_message == text
        time.sleep(5)


    def my_account_menu(self):
        self.find(self.ACCOUNT_MENU).click()

    def click_sign_out(self):
        self.find(self.SIGN_OUT_BUTTON).click()

    def sign_out_message(self):
        self.driver.implicitly_wait(1)
        assert self.find(self.SIGN_OUT_MESSAGE).is_displayed()
