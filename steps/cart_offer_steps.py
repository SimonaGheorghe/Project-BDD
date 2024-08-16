from behave import *

@given('I am on the Women page "{url}"')
def step_impl(context, url):
    context.women_page.open(url)

@then('The URL of the page should be "{url}"')
def step_impl(context, url):
    context.women_page.verify_url(url)

@when('I click the "Women’s Tees" button')
def step_impl(context):
    context.women_page.click_women_tees_button()

@then('I am redirected to the Tees page "{url}"')
def step_impl(context, url):
    context.women_page.verify_url_women_tees(url)


@when('I click the "Desiree Fitness Tee" button')
def step_impl(context):
    context.cart_offer_page.click_product_item()

@when('I select the size')
def step_impl(context):
    context.cart_offer_page.click_size()

@when('I select the color')
def step_impl(context):
    context.cart_offer_page.click_color()

@when('I click the "Add to cart" button')
def step_impl(context):
    context.cart_offer_page.click_add_to_cart()

@then('I click the cart details')
def step_impl(context):
    context.cart_offer_page.click_show_cart_qty()

@then('I click the "View and Edit Cart" button')
def step_impl(context):
    context.cart_offer_page.click_view_cart_details()

@then('I check the discount in the cart')
def step_impl(context):
    context.cart_offer_page.discount()

@when('I am on the Shipping page "{url}"')
def step_impl(context, url):
    context.cart_offer_page.verify_url_shipping(url)

@when('I enter Street Address "{text}"')
def step_impl(context, text):
    context.cart_offer_page.set_street_address(text)

@when('I enter City "{text}"')
def step_impl(context, text):
    context.cart_offer_page.set_city(text)

@when('I select State "{text}"')
def step_impl(context, text):
    context.cart_offer_page.select_state(text)

@when('I enter Postal Code "{number}"')
def step_impl(context, number):
    context.cart_offer_page.set_postal_code(number)

@when('I select Country "{text}"')
def step_impl(context, text):
    context.cart_offer_page.select_country(text)

@when('I enter Phone Number "{number}"')
def step_impl(context, number):
    context.cart_offer_page.set_phone_number(number)

@when('I choose Shipping Methods')
def step_impl(context):
    context.cart_offer_page.click_shipping_methods()

@when('I click the Next button')
def step_impl(context):
    context.cart_offer_page.click_next_button()

@when('I click the Place Order button')
def step_impl(context):
    context.cart_offer_page.click_place_order_button()

@then('I am redirected to the success order page "{url}"')
def step_impl(context, url):
    context.cart_offer_page.verify_url_order(url)

@then ('Success order message is displayed')
def step_impl(context):
    context.cart_offer_page.verify_success_message_displayed()

@then('The success order message is "{text}"')
def step_impl(context, text):
    context.cart_offer_page.verify_success_message_contains_text(text)

@given('I am on Home Page {url}')
def step_impl(context, url):
    context.hope_page.open(url)

@when('I access the drop down from User Account')
def step_impl(context):
    context.cart_offer_page.my_account_menu()

@when('I click on Sign Out button')
def step_impl(context):
    context.cart_offer_page.click_sign_out()

@then('The Sign out message desplayed is {message}')
def step_impl(context, message):
    context.cart_offer_page.sign_out_message(message)



