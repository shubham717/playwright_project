from pages.bookmyshow.home_page import BMSHomePage
from playwright.sync_api import Page, expect

def test_bms_navigation(page, config):
    bms_home = BMSHomePage(page)

    url = config["environments"]["bookmyshow"]["base_url"]
    bms_home.navigate(url)

    bms_home.click_movies_tab()
    assert "Movies" in bms_home.get_title()
