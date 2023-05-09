import pytest

from playwright_models.login_page import LoginPage

LOGIN_URL = "https://www.saucedemo.com/"
SHOP_URL = "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize("username", ["standard_user", "locked_out_user"])
def test_successful_and_unsuccessful_login(page, playwright, username: str):
    login = LoginPage(page, playwright)

    page.goto(url=LOGIN_URL)
    login.login_user(username=username, password="secret_sauce")
    if username == "locked_out_user":
        assert login.login_error_message.is_visible()
    else:
        page.wait_for_url(url=SHOP_URL)
