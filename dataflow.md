📘 Pytest-Playwright Automation BlueprintFrom Single Scripts to a Scalable Page Object Model FrameworkThis document tracks how our code evolved step-by-step from raw script execution into a highly professional architecture using Page Objects, Environment Isolation (.env), and Global Configurations (conftest.py).🏗️ The Evolution: Where We Started vs. Where We ArePlaintext  Phase 1: Raw Scripting           Phase 2: Page Object Pattern          Phase 3: Scalable Framework
┌─────────────────────────┐       ┌────────────────────────────┐       ┌──────────────────────────────┐
│  • Hardcoded locators   │       │  • Code separated by page  │       │  • Zero-boilerplate tests    │
│  • Duplicated setups    │ ───►  │  • Easily maintainable     │ ───►  │  • Automatic dependencies    │
│  • Mixed logic/elements │       │  • Clearer data flows      │       │  • Secured credentials (.env)│
└─────────────────────────┘       └────────────────────────────┘       └──────────────────────────────┘
📁 Final Optimized Directory LayoutPlaintextpractice-software-testing-automation/
│
├── .env                  # Private configurations (Git-ignored)
├── conftest.py           # Core system engine & shared page fixtures
│
├── pages/                # Blueprint Layer (The Map & Actions)
│   ├── __init__.py
│   └── login_page.py
│
└── tests/                # Verification Layer (The Assertions)
    ├── __init__.py
    └── test_demo.py
🛠️ Step-by-Step Code Configuration1. The Environment Safe (.env)Stores sensitive credentials externally so they never leak onto version control platforms like GitHub.Ini, TOML# .env
TEST_USER_EMAIL=amshubham717@gmail.com
TEST_USER_PASSWORD=banafer@01
2. The Shared Configuration Engine (conftest.py)This file runs automatically before anything else. It strips away repetitive object-creation logic from individual test suites by instantiating components behind the scenes.Python# conftest.py
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from dotenv import load_dotenv

# Run this automatically before any test executes to load environment variables globally
@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

# Automatically creates and handles the lifecycle of the login page object
@pytest.fixture
def login_page(page: Page):
    """
    Takes Playwright's native 'page' fixture (active browser tab),
    injects it directly into the LoginPage blueprint, and yields it to the test.
    """
    login_pg = LoginPage(page)
    return login_pg
3. The Page Object Blueprint (pages/login_page.py)Acts as a dictionary of web elements and an operational remote control for the webpage UI.Python# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        # Attach the live browser context to the instance
        self.page = page
        
        # Centralized Object Repository (Locators Map)
        self.email_input = "[data-test='email']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-submit']"
        self.error_message = "[data-test='login-error']"

    def navigate(self):
        """Commands the active tab to jump directly to the target UI route."""
        self.page.goto("https://practicesoftwaretesting.com/auth/login")

    def login(self, email_str: str, password_str: str):
        """Interacts seamlessly with form components using cached locators."""
        self.page.fill(self.email_input, email_str)
        self.page.fill(self.password_input, password_str)
        self.page.click(self.login_button)
        
    def get_error_text(self):
        """Grabs error feedback strings dynamically if context is needed."""
        return self.page.locator(self.error_message).text_content()
4. The Functional Test File (tests/test_demo.py)Because configuration is abstracted away, your test assertions are perfectly declarative, lightweight, and human-readable.Python# tests/test_demo.py
import os
import pytest

def test_demo(login_page):
    # Fetch clean, un-hardcoded values straight from system environment memory
    email = os.getenv("TEST_USER_EMAIL")
    password = os.getenv("TEST_USER_PASSWORD")
    
    # Execute actions via the injected, ready-to-use fixture
    login_page.navigate()
    login_page.login(email, password)
    
    # Let Playwright smart-wait for confirmation instead of freezing code execution
    login_page.page.wait_for_selector("[data-test='nav-menu']")
🔀 System Execution LifecycleWhen you trigger pytest tests/test_demo.py via your terminal, the complete system loop flows like this:$$\text{Pytest Engine Core} \longrightarrow \text{Loads conftest.py [Bootstraps .env variables]} $$$$\Downarrow$$$$\text{Launches Playwright Engine [Generates active tab context]} \longrightarrow \text{Injects tab into LoginPage()}$$$$\Downarrow$$$$\text{Hands fully pre-built login\_page object directly to test\_demo()} \longrightarrow \text{Executes assertions \& cleans memory}$$