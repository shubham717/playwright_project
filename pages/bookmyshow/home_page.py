from pages.basepage import Basepage

class BMSHomePage(Basepage):
    def __init(self, page):
        super().__init(page)

        self.movies_tab = "a:has-text('Movies')"
        self.search_icon = "div#super-container svg"

    def click_movies_tab(self):
        self.click_element(self.movies_tab)

