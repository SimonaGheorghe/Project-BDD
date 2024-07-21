from behave import *

@given('I am on the login page "{url}"')
def step_impl(context, url):
    context.login_page.open(url)

@when("I click Consent button to use of my date")
def step_impl(context):
    context.login_page.click_consent_button()


@then('The login URL of the page is "{url}"')
def step_impl(context, url):
    context.login_page.verify_url(url)

@when('I enter "{text}" as email')
def step_impl(context, text):
    context.login_page.set_email(text)

@when('I enter "{text}" as password')
def step_impl(context, text):
    context.login_page.set_password(text)

@when("I click the signin button")
def step_impl(context):
    context.login_page.click_signin_button()

@then('I should see "{message}" message')
def step_impl(context, message):
    context.login_page.verify_signin_error_message(message)