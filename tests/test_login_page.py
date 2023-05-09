import pytest

from playwright_models.login_page import LoginPage

LOGIN_URL = "https://www.saucedemo.com/"
SHOP_URL = "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize("username", ["standard_user", "locked_out_user", "not_registered_user"])
def test_successful_and_unsuccessful_login(page, playwright, username: str):
    login = LoginPage(page, playwright)

    # Navigate to login page
    page.goto(url=LOGIN_URL)

    # Try to log in user
    login.login_user(username=username, password="secret_sauce")
    if username == "locked_out_user":
        assert login.login_error_message.is_visible()
        assert login.login_error_message.inner_text() == "Epic sadface: Sorry, this user has been locked out."
    elif username == "not_registered_user":
        assert login.login_error_message.is_visible()
        assert login.login_error_message.inner_text() == "Epic sadface: Username and password do not match any user " \
                                                         "in this service"
    else:
        page.wait_for_url(url=SHOP_URL)


def test_username_and_password_required(page, playwright, username: str = "standard_user"):
    login = LoginPage(page, playwright)

    # Navigate to login page
    page.goto(url=LOGIN_URL)

    # Try to log in without providing username
    login.login_button.click()
    assert login.login_error_message.is_visible()
    assert login.login_error_message.inner_text() == "Epic sadface: Username is required"

    # Provide username and try without password
    login.user_name_input.fill(username)
    login.login_button.click()
    assert login.login_error_message.is_visible()
    assert login.login_error_message.inner_text() == "Epic sadface: Password is required"
