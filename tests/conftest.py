import pytest
import os
import shutil
from pathlib import Path
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session", autouse=True)
def create_and_protect_output_dir():
    # Define your directory name
    target_dir = os.path.abspath("my_test_outputs")
    
    # Force create it if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        
    yield  # This is where your tests run
    
    # Teardown safety check: Force create it again if a hook deleted it
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        
# def pytest_configure(config):
#     """Manages the test-results folder safely to prevent deletion conflicts."""
    
#     # 1. Look for the directory assigned via --html
#     htmlpath = config.getoption("--html")
    
#     if htmlpath:
#         report_dir = Path(htmlpath).parent
        
#         # 2. Manually wipe out previous results right here (Full Overwrite)
#         if report_dir.exists():
#             shutil.rmtree(report_dir)
            
#         # 3. Recreate it fresh
#         report_dir.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session")
def API_Setup(playwright: Playwright) -> APIRequestContext:
    request_context = playwright.request.new_context(
        base_url = "https://jsonplaceholder.typicode.com",
        extra_http_headers = {
            "Accept" : "application/json"
        }
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def weather_api(playwright: Playwright) -> APIRequestContext:
    context = playwright.request.new_context(base_url = "https://api.open-meteo.com")
    yield context
    context.dispose()

@pytest.fixture(scope="session", autouse=True)
def stop_playwright_cleanup(pytestconfig):
    """Forces pytest-playwright not to purge the output directory mid-run."""
    # This disables the internal flag that makes the folder vanish
    pytestconfig.option.no_summary_clean = True

