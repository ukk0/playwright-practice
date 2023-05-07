class CheckoutPage:
    def __init__(self, page, playwright):
        self.page = page
        self.playwright = playwright
        playwright.selectors.set_test_id_attribute("data-test")

        self.submit_info_button = page.get_by_test_id("continue")
        self.input_first_name = page.get_by_placeholder(text="First Name")
        self.input_last_name = page.get_by_placeholder(text="Last Name")
        self.input_zip_code = page.get_by_placeholder(text="Zip/Postal Code")
        self.error_missing_info = page.get_by_test_id("error")

        self.checkout_item_price = page.locator("[class='cart_item'] [class='inventory_item_price']")
        self.summary_subtotal_label = page.locator("[class='summary_subtotal_label']")
        self.summary_tax_label = page.locator("[class='summary_tax_label']")
        self.summary_total_label = page.locator("[class='summary_info_label summary_total_label']")
        self.finish_payment_button = page.get_by_test_id("finish")
        self.thank_you_page = page.get_by_role(role="heading", name="Thank you for your order!")
        self.return_to_shop_button = page.get_by_test_id("back-to-products")

    def fill_first_name(self, first_name: str):
        self.input_first_name.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.input_last_name.fill(last_name)

    def fill_zip_code(self, zip_code: str):
        self.input_zip_code.fill(zip_code)

    def proceed_to_final_checkout(self):
        self.submit_info_button.click()
        self.page.wait_for_load_state()

    def missing_info_warning(self):
        error_msg = self.error_missing_info.inner_text()
        return error_msg

    def finalize_payment(self):
        self.finish_payment_button.click()
        self.page.wait_for_load_state()

    def return_to_shop(self):
        self.return_to_shop_button.click()
        self.page.wait_for_load_state()
