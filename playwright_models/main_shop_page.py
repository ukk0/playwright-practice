class ShopPage:
    def __init__(self, page, playwright):
        self.page = page
        self.playwright = playwright
        playwright.selectors.set_test_id_attribute("data-test")

        self.hamburger_menu = page.get_by_role("button", name="Open Menu")
        self.side_menu_wrapper = page.locator("[class='bm-menu-wrap']")
        self.menu_all_items_button = page.get_by_role("link", name="All Items")
        self.menu_about_button = page.get_by_role("link", name="About")
        self.menu_logout_button = page.get_by_role("link", name="Logout")
        self.menu_reset_app_button = page.get_by_role("link", name="Reset App State")
        self.close_menu_button = page.get_by_role("button", name="Close Menu")

        self.shopping_cart_button = page.locator("[class='shopping_cart_container'] [class='shopping_cart_link']")

    def open_side_menu(self):
        self.hamburger_menu.click()
        self.page.wait_for_load_state()

    def close_side_menu(self):
        self.close_menu_button.click()
        self.page.wait_for_load_state()
