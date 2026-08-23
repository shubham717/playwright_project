import pytest
import os
from playwright.sync_api import Playwright, APIRequestContext
from pages.login_page import LoginPage
from dotenv import load_dotenv
from pages.ecommerce.home_page import Homepage

load_dotenv()

# def test_demo(page):
#     email = os.getenv("TEST_USER_EMAIL")
#     password = os.getenv("TEST_USER_PASSWORD")
    
#     login_pg = LoginPage(page)
#     login_pg.navigate()
#     login_pg.login(email, password)
#     login_pg.page.wait_for_timeout(6000)
    
def test_scenarios(page):
    home_pg = Homepage(page)
    home_pg.navigate()
    home_pg.verify_title()
    home_pg.sorting()
    home_pg.wait_for_a_bit()
    home_pg.test_duplicate_tab_same_context()
    home_pg.wait_for_a_bit()
    home_pg.test_duplicate_tab_same_context()
