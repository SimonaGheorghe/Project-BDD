from behave import *

@given("I am on the Create an Account page")
def step_impl(context):
    context.register_page.open()

@when ('I enter "{text}" in the first name input')
def step_impl(context, text):
    context.register_page.set_first_name(text)

@when ('I enter "{text}" in the last name input')
def step_impl(context, text):
    context.register_page.set_last_name(text)

@when ('I enter random email adress in the email input')
def step_impl(context):
    context.register_page.set_unique_email()

@when ('I enter "{text}" in the password input')
def step_impl(context, text):
    context.register_page.set_password(text)

@when ('I enter "{text}" in the password confirm input')
def step_impl(context, text):
    context.register_page.set_password_confirm(text)

@when ('I click the Create an Account button')
def step_impl(context):
    context.register_page.click_register_button()

@then ('Success message is displayed')
def step_impl(context):
    context.register_page.verify_success_message_displayed()

@then('The success message is "{text}"')
def step_impl(context, text):
    context.register_page.verify_success_message_contains_text(text)

@then('The URL of the Create an Account page is correct')
def step_impl(context):
    context.register_page.verify_url()

@Then('First name error is displayed')
def step_impl(context):
    context.register_page.verify_first_name_error_displayed()

@Then('Last name error is displayed')
def step_impl(context):
    context.register_page.verify_last_name_error_displayed()

@Then('Email error is displayed')
def step_impl(context):
    context.register_page.verify_email_error_displayed()

@Then('Password error is displayed')
def step_impl(context):
    context.register_page.verify_password_error_displayed()

@Then('Confirm Password error is displayed')
def step_impl(context):
    context.register_page.verify_confirm_password_error_displayed()