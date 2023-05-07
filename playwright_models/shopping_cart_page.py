class ShoppingCart:
    def __init__(self, page, playwright):
        self.page = page
        self.playwright = playwright
        playwright.selectors.set_test_id_attribute("data-test")

        self.remove_item_button = page.get_by_text(text="Remove")
        self.cart_item_label = page.locator("[class='cart_list'] [class='cart_item_label']")
        self.return_to_shop_page_button = page.get_by_test_id("continue-shopping")
        self.proceed_to_checkout_button = page.get_by_test_id("checkout")

    def remove_first_item_from_cart(self):
        self.remove_item_button.first.click()

    def get_cart_item_count(self):
        count = self.cart_item_label.count()
        return count

    def return_to_shop_page(self):
        self.return_to_shop_page_button.click()
        self.page.wait_for_load_state()

    def proceed_to_checkout_page(self):
        self.proceed_to_checkout_button.click()
        self.page.wait_for_load_state()
