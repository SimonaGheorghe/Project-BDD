from behave import *

@given('I am on the Whats New page "{url}"')
def step_impl(context, url):
    context.new_page.open(url)

@then('The new URL of the page is "{url}"')
def step_impl(context, url):
    context.new_page.verify_url(url)

@when('I click the Shop New Yoga button')
def step_impl(context):
    context.new_page.click_shop_new_yoga_button()

@then('I am redirected on the New Luma Yoga Collection page "{url}"')
def step_impl(context, url):
    context.new_page.verify_url_new_collection(url)
@then('I should see the "{title}" Message')
def step_impl(context, title):
    context.search_results_page.verify_success_message_contains_text(title)