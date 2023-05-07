import pytest
from playwright_models.login_page import LoginPage


@pytest.mark.parametrize("username", ["standard_user", "locked_out_user"])
def test_successful_and_unsuccessful_login(page, playwright, username: str):
    login = LoginPage(page, playwright)

    page.goto(url="https://www.saucedemo.com/")
    login.login_user(username=username, password="secret_sauce")
    if username == "locked_out_user":
        assert login.login_error_message.is_visible()
    else:
        page.expect_navigation(url="https://www.saucedemo.com/inventory.html")
