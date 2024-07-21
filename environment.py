from browser import Browser
from Pages.login_page import LoginPage
from Pages.news_page import WhatsNewPage
from Pages.register_page import RegisterPage
from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()
    context.new_page = WhatsNewPage()

def after_all(context):
    context.browser.close()