import pytest
from playwright_models.main_shop_page import ShopPage


def test_check_side_menu_items(page, playwright, login_cookie):
    shop = ShopPage(page, playwright)

    # Skip login and navigate to page
    page.context.add_cookies([login_cookie])
    page.goto(url="https://www.saucedemo.com/inventory.html")

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

    # Skip login and navigate to page
    page.context.add_cookies([login_cookie])
    page.goto(url="https://www.saucedemo.com/inventory.html")

    # Open the side menu and try the options
    if menu_option == "All Items":
        shop.shopping_cart_button.click()
        shop.open_side_menu()
        shop.menu_all_items_button.click()
        page.expect_navigation(url="https://www.saucedemo.com/inventory.html")

    elif menu_option == "About":
        shop.open_side_menu()
        shop.menu_about_button.click()
        page.expect_navigation(url="https://saucelabs.com/")

    elif menu_option == "Logout":
        shop.open_side_menu()
        shop.menu_logout_button.click()
        page.expect_navigation(url="https://www.saucedemo.com/")
