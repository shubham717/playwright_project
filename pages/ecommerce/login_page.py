from playwright.sync_api import Page

class Basepage:
    def __init__(self, page:Page):
        self.page = page
        self.base_url = "https://practicesoftwaretesting.com"

    def navigate_to(self, endpoint: str = ""):
        self.page.goto(f"{self.base_url}{endpoint}")
        