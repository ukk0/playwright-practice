import pytest

from playwright_models.shopping_cart_page import ShoppingCart

CART_URL = "https://www.saucedemo.com/cart.html"
CHECKOUT_URL = "https://www.saucedemo.com/checkout-step-one.html"
SHOP_URL = "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize("next_step", ["return", "proceed"])
def test_remove_shopping_cart_items_and_proceed(page, playwright, next_step, login_cookie, cart_fill_script):
    cart = ShoppingCart(page, playwright)

    # Skip login and navigate to a pre-filled shopping cart (6 items)
    page.context.add_cookies([login_cookie])
    page.context.add_init_script(cart_fill_script)
    page.goto(url=CART_URL)

    # Remove items from cart one-by-one
    initial_item_count = cart.get_cart_item_count()
    for n in range(initial_item_count):
        cart.remove_first_item_from_cart()
        current_item_count = cart.get_cart_item_count()
        assert current_item_count == initial_item_count - (n + 1)

    # Leave the shopping cart or proceed to checkout
    if next_step == "return":
        cart.return_to_shop_page()
        page.wait_for_url(url=SHOP_URL)

    elif next_step == "proceed":
        cart.proceed_to_checkout_page()
        page.wait_for_url(url=CHECKOUT_URL)
