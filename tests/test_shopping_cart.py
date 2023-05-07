from playwright_models.shopping_cart_page import ShoppingCart


def test_remove_shopping_cart_items_and_leave(page, playwright, login_cookie, cart_fill_script):
    cart = ShoppingCart(page, playwright)

    # Skip login and navigate to a pre-filled shopping cart (6 items)
    page.context.add_cookies([login_cookie])
    page.context.add_init_script(cart_fill_script)
    page.goto(url="https://www.saucedemo.com/cart.html")

    # Remove items from cart one-by-one
    initial_item_count = cart.get_cart_item_count()
    for n in range(initial_item_count):
        cart.remove_first_item_from_cart()
        current_item_count = cart.get_cart_item_count()
        assert current_item_count == initial_item_count - (n + 1)

    # Leave the shopping cart
    cart.return_to_shop_page()
    page.expect_navigation(url="https://www.saucedemo.com/inventory.html")
