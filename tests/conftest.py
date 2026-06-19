<<<<<<< Updated upstream
=======
import pytest
from playwright.sync_api import Playwright, APIRequestContext

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

>>>>>>> Stashed changes
