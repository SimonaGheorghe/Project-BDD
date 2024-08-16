from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    BUTTON_ALL_REVIEWS = (By.CSS_SELECTOR, ".action.view")
    INPUT_YOUR_RATING = (By.ID, 'Rating_5_label')
    INPUT_ALIAS = (By.ID, "nickname_field")
    INPUT_SUMMARY = (By.ID, "summary_field")
    INPUT_REVIEW = (By.ID, "review_field")
    BUTTON_SUBMIT_THE_REVIEW = (By.CSS_SELECTOR, ".action.submit")
    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")

    def verify_url(self):
        assert "https://magento.softwaretestingboard.com/catalogsearch/result/?q=shorts" in self.driver.current_url

    def click_review_button(self):
        self.find(self.BUTTON_ALL_REVIEWS).click()

    def click_rating_rev(self):
        button_rating = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.INPUT_YOUR_RATING))

        self.driver.execute_script("arguments[0].scrollIntoView();", button_rating)

        ActionChains(self.driver).move_to_element(button_rating).click().perform()


    def set_nickname(self, text):
        self.type(self.INPUT_ALIAS, text)

    def set_summary(self, text):
        self.type(self.INPUT_SUMMARY, text)

    def set_review(self, text):
        self.type(self.INPUT_REVIEW, text)

    def click_submit_review_button(self):
        self.find(self.BUTTON_SUBMIT_THE_REVIEW).click()

    def verify_search_results_displayed(self):
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results)>0