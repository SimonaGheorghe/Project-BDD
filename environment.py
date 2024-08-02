from browser import Browser
from Pages.login_page import LoginPage
from Pages.news_page import WhatsNewPage
from Pages.register_page import RegisterPage
from Pages.women_page import WomenPage
from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage
from Pages.cart_offer_page import WomenOffer

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