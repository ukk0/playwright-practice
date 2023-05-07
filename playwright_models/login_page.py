class LoginPage:
    def __init__(self, page, playwright):
        self.page = page
        self.playwright = playwright
        playwright.selectors.set_test_id_attribute("data-test")

        self.user_name_input = page.get_by_test_id("username")
        self.user_password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
        self.login_error_message = page.get_by_test_id("error")

    def login_user(self, username: str = "standard_user", password: str = "secret_sauce"):
        self.user_name_input.fill(username)
        self.user_password_input.fill(password)
        self.login_button.click()
