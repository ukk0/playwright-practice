import pytest
from playwright_models.login_page import LoginPage

URL = "https://www.saucedemo.com/"


@pytest.mark.parametrize("username", ["standard_user", "locked_out_user"])
def test_successful_and_unsuccessful_login(page, playwright, username):
    login = LoginPage(page, playwright)

    page.goto(url=URL)
    login.login_user(username=username, password="secret_sauce")
    if username == "locked_out_user":
        assert login.login_error_message.is_visible()
    else:
        page.expect_navigation(url="https://www.saucedemo.com/inventory.html")
