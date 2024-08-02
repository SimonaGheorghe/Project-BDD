from behave import *

@given('I am on the Whats New page "{url}"')
def step_impl(context, url):
    context.new_page.open(url)

@then('The new URL of the page is "{url}"')
def step_impl(context, url):
    context.new_page.verify_url(url)

@when('I click the Shop Eco Friendly button')
def step_impl(context):
    context.new_page.click_shop_eco_button()

@then('I am redirected on the Eco Collection New page "{url}"')
def step_impl(context, url):
    context.new_page.verify_url_new_collection(url)
@then('I should see the "{title}" Message')
def step_impl(context, title):
    context.new_page.verify_success_message_contains_text(title)

@given('I am on Eco Collection New Page "{url}"')
def step_impl(context,url):
    context.new_page.open2(url)

@when('I click the item Layla Tee')
def step_impl(context):
    context.new_page.click_item_tee()

@when('I click the button ADD TO WISH LIST')
def step_impl(context):
    context.new_page.click_wishlist()

@then('I am redirected to My Wish List page "{url}"')
def step_impl(context,url):
    context.new_page.verify_url_wishlist(url)

@then('I should see the success message')
def step_impl(context):
    context.new_page.verify_message_layla()

@when('I click the "I click the "Add all to cart" button from wish list')
def step_impl(context):
    context.new_page.click_addtocart()
@then('I should see the error message')
def step_impl(context):
    context.new_page.verify_error_message()
