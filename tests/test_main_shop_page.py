import pytest

from playwright_models.main_shop_page import ShopPage

LOGIN_URL = "https://www.saucedemo.com/"
ABOUT_URL = "https://saucelabs.com/"
SHOP_URL = "https://www.saucedemo.com/inventory.html"


def test_check_side_menu_items(page, playwright, login_cookie):
    shop = ShopPage(page, playwright)

    # Skip login and navigate to shop page
    page.context.add_cookies([login_cookie])
    page.goto(url=SHOP_URL)

    # Open the side menu and assert expected options
    shop.open_side_menu()
    assert shop.side_menu_wrapper.is_visible()
    assert shop.menu_all_items_button.is_visible()
    assert shop.menu_about_button.is_visible()
    assert shop.menu_logout_button.is_visible()
    assert shop.menu_reset_app_button.is_visible()

    # Close the side menu and assert it is closed
    shop.close_side_menu()
    assert not shop.side_menu_wrapper.is_visible()


@pytest.mark.parametrize("menu_option", ["All Items", "About", "Logout"])
def test_side_menu_functionality(page, playwright, menu_option, login_cookie):
    shop = ShopPage(page, playwright)

    # Skip login and navigate to shop page
    page.context.add_cookies([login_cookie])
    page.goto(url=SHOP_URL)

    # Open the side menu and try the options
    if menu_option == "All Items":
        shop.open_shopping_cart()
        shop.open_side_menu()
        shop.menu_all_items_button.click()
        page.wait_for_url(url=SHOP_URL)

    elif menu_option == "About":
        shop.open_side_menu()
        shop.menu_about_button.click()
        page.wait_for_url(url=ABOUT_URL)

    elif menu_option == "Logout":
        shop.open_side_menu()
        shop.menu_logout_button.click()
        page.wait_for_url(url=LOGIN_URL)


def test_item_filtering_options(page, playwright, login_cookie):
    shop = ShopPage(page, playwright)

    # Skip login and navigate to shop page
    page.context.add_cookies([login_cookie])
    page.goto(url=SHOP_URL)

    # Use inventory filters and check that the ordering is correct
    # Filter Z-A
    shop.use_inventory_filter(filter_option="za")
    all_items = shop.inventory_items.all_inner_texts()
    assert all_items == sorted(all_items, reverse=True)

    # Filter A-Z
    shop.use_inventory_filter(filter_option="az")
    all_items = shop.inventory_items.all_inner_texts()
    assert all_items == sorted(all_items)

    # Filter the highest price to the lowest
    shop.use_inventory_filter(filter_option="hilo")
    all_prices = [float(price[1:]) for price in shop.inventory_prices.all_inner_texts()]
    assert all_prices == sorted(all_prices, reverse=True)

    # Filter the lowest price to the highest
    shop.use_inventory_filter(filter_option="lohi")
    all_prices = [float(price[1:]) for price in shop.inventory_prices.all_inner_texts()]
    assert all_prices == sorted(all_prices)


def test_adding_items_to_cart(page, playwright, login_cookie):
    shop = ShopPage(page, playwright)

    # Skip login and navigate to shop page
    page.context.add_cookies([login_cookie])
    page.goto(url=SHOP_URL)

    # Add first three available items to shopping cart and assert correct amount of items is displayed
    shop.add_items_to_cart(amount_of_items=3)
    assert shop.cart_item_count() == 3

    # Remove two items from shopping cart and assert correct amount of items remain
    shop.remove_items_from_cart(amount_of_items=2)
    assert shop.cart_item_count() == 1
