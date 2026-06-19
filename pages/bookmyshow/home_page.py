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
from pages.basepage import Basepage
from playwright.sync_api import Page

class BMSHomePage(Basepage):
    def __init(self, page):
        super().__init__(page)

        self.movies_tab = "a:has-text('Movies')"
        self.search_icon = "div#super-container svg"

    def click_movies_tab(self):
        self.click_element(self.movies_tab)

