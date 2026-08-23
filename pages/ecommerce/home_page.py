from playwright.sync_api import Page, expect
import os
import pytest

class Homepage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/")

    def verify_title(self):
        expect(self.page).to_have_title("Practice Software Testing - Toolshop - v5.0")

    def sorting(self):
        # self.page.wait_for_selector("")
        dropdown = self.page.locator('[data-test="sort"]')
        dropdown.select_option(value="price,desc")

    def wait_for_a_bit(self):
        self.page.wait_for_timeout(5000)

    def drag_price(self):
        source = self.page.get_by_role("slider", name="ngx-slider-max")
        target = self.page

    def test_duplicate_tab_same_context(self):
        current_url = self.page.url
        context = self.page.context
        new_page = context.new_page()
        new_page.goto(current_url)
        new_page.wait_for_load_state("networkidle")

    def minimum_price(self):
        price_locator = self.page.locator('//span[@data-test="product-price"]')
        price_locator.first.wait_for(state="visible")
        raw_prices = price_locator.all_text_contents()
        float_prices = [float(price.replace('$', '').strip()) for price in raw_prices]
        min_price = min(float_prices)



