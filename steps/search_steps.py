from behave import *

@given('I am on the home page')
def step_impl(context):
    context.home_page.open()

@when('I enter "{text}" in the search filed')
def step_impl(context, text):
    context.home_page.set_search_term(text)

@when('I click the search magnifying button')
def step_impl(context):
    context.home_page.click_search_magnifying_button()

@when('I am redirected on the search results page')
def step_impl(context):
    context.search_results_page.verify_url()

@when('There are some results displayed')
def step_impl(context):
    context.search_results_page.verify_search_results_displayed()
@when("I click Reviews button")
def step_impl(context):
    context.search_results_page.click_review_button()
@when('I click 5 stars Rating')
def step_impl(context):
    context.search_results_page.click_rating_rev()
@when('I write the Nickname "{text}"')
def step_impl(context, text):
    context.search_results_page.set_nickname(text)
@when('I write the summary "{text}"')
def step_impl(context, text):
    context.search_results_page.set_summary(text)
@when('I write the Review "{text}"')
def step_impl(context, text):
    context.search_results_page.set_review(text)

@then('I click on the Submit Review button')
def step_impl(context):
    context.search_results_page.click_submit_review_button()

