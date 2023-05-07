class ShopPage:
    def __init__(self, page, playwright):
        self.page = page
        self.playwright = playwright
        playwright.selectors.set_test_id_attribute("data-test")

        self.hamburger_menu = page.get_by_role("button", name="Open Menu")
        self.side_menu_wrapper = page.locator("[class='bm-menu-wrap']")
        self.menu_all_items_button = page.get_by_role(role="link", name="All Items")
        self.menu_about_button = page.get_by_role(role="link", name="About")
        self.menu_logout_button = page.get_by_role(role="link", name="Logout")
        self.menu_reset_app_button = page.get_by_role(role="link", name="Reset App State")
        self.close_menu_button = page.get_by_role(role="button", name="Close Menu")

        self.inventory_filter = page.get_by_test_id("product_sort_container")
        self.inventory_items = page.locator("[class='inventory_list'] [class='inventory_item_name']")
        self.inventory_prices = page.locator("[class='inventory_list'] [class='inventory_item_price']")
        self.shopping_cart_button = page.locator("[class='shopping_cart_container'] [class='shopping_cart_link']")
        self.add_item_to_cart = page.get_by_text(text="Add to cart")
        self.remove_item_from_cart = page.get_by_text(text="Remove")
        self.shopping_cart_items = page.locator("[class='shopping_cart_link'] [class='shopping_cart_badge']")

    def open_side_menu(self):
        self.hamburger_menu.click()
        self.page.wait_for_load_state()

    def close_side_menu(self):
        self.close_menu_button.click()
        self.page.wait_for_timeout(timeout=500)

    def open_shopping_cart(self):
        self.shopping_cart_button.click()
        self.page.wait_for_load_state()

    def use_inventory_filter(self, filter_option: str):
        self.inventory_filter.click()
        self.inventory_filter.select_option(filter_option)
        self.page.wait_for_load_state()

    def add_items_to_cart(self, amount_of_items: int):
        for i in range(amount_of_items):
            self.add_item_to_cart.nth(i).click()

    def remove_items_from_cart(self, amount_of_items: int):
        for i in range(amount_of_items):
            self.remove_item_from_cart.nth(i).click()

    def cart_item_count(self):
        item_count = self.shopping_cart_items.inner_text()
        return int(item_count)
