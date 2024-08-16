from browser import Browser
from pages.cart_offer_page import WomenOffer
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.news_page import WhatsNewPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage
from pages.women_page import WomenPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.search_results_page = SearchResultsPage()
    context.new_page = WhatsNewPage()
    context.women_page = WomenPage()
    context.cart_offer_page = WomenOffer()
    context.home_page = HomePage()

def after_all(context):
    context.browser.close()