from playwright.sync_api import Page, expect

def test_open_bookmyshow(page: Page):

    page.goto("https://in.bookmyshow.com/")
    page.wait_for_timeout(3000)

