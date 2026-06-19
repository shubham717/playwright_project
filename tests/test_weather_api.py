import pytest
from playwright.sync_api import Playwright, APIRequestContext

def test_weather_api_pune(weather_api) -> None:
    params = {
        "latitude": 18.5196,
        "longitude": 73.8554,
        "hourly": "temperature_2m",
        "timezone": "auto"
    }
    response = weather_api.get("/v1/forecast", params=params)

    assert response.ok, f"API Request failed with status code: {response.status}"

    response_body = response.json()
 

    assert "hourly" in response_body, "Response missing 'hourly' data object."

    assert "temperature_2m" in response_body, "Response missing 'temperature_2m' data object."

