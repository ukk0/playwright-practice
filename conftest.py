import pytest


@pytest.fixture
def login_cookie():
    cookie = {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/"
    }
    return cookie
