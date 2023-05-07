from playwright_models.checkout_page import CheckoutPage


def test_payer_info_is_required_at_checkout(page, playwright, login_cookie, cart_fill_script):
    check = CheckoutPage(page, playwright)

    # Skip login and navigate to checkout with a pre-filled shopping cart
    page.context.add_cookies([login_cookie])
    page.context.add_init_script(cart_fill_script)
    page.goto(url="https://www.saucedemo.com/checkout-step-one.html")

    # Try to proceed from the page without filling in required information
    check.proceed_to_final_checkout()
    assert check.missing_info_warning() == "Error: First Name is required"
    check.fill_first_name(first_name="FIRST")

    check.proceed_to_final_checkout()
    assert check.missing_info_warning() == "Error: Last Name is required"
    check.fill_last_name(last_name="LAST")

    check.proceed_to_final_checkout()
    assert check.missing_info_warning() == "Error: Postal Code is required"
    check.fill_zip_code(zip_code="123456")

    # Proceed successfully to final checkout page
    check.proceed_to_final_checkout()
    page.expect_navigation(url="https://www.saucedemo.com/checkout-step-two.html")


def test_item_prices_match_total(page, playwright, login_cookie, cart_fill_script):
    check = CheckoutPage(page, playwright)

    # Skip login and payment info and navigate to final checkout with a pre-filled shopping cart
    page.context.add_cookies([login_cookie])
    page.context.add_init_script(cart_fill_script)
    page.goto(url="https://www.saucedemo.com/checkout-step-two.html")

