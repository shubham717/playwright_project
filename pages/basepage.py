from playwright.sync_api import Page, expect

class Basepage:
    def __init(self, page:Page):
        self.page = page

    def navigate(self, url:str):
        self.page.goto(url)

    def click_element(self, selector:str):
        self.page.locator(selector).click

    def fill_text(self) ->str:
        return self.page.title()
