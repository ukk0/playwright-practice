from playwright_models.checkout_page import CheckoutPage


def test_payer_info_is_required_at_checkout(page, playwright, login_cookie, cart_fill_script):
    check = CheckoutPage(page, playwright)

    # Skip login and navigate to checkout with a pre-filled shopping cart
    page.context.add_cookies([login_cookie])
    page.context.add_init_script(cart_fill_script)
    page.goto(url="https://www.saucedemo.com/checkout-step-one.html")

    # Try to proceed from the page without filling in required information


def test_item_prices_match_total():
    pass
