import pytest

from playwright.sync_api import APIRequestContext, Playwright


def test_get_single_post(API_Setup: APIRequestContext)->None:
    response = API_Setup.get("/posts/1")
    assert response.ok, f"Request failed with status {response.status}"
    assert response.status == 200
    response_body = response.json()
    assert response_body["id"] == 1
    assert response_body["userId"] == 1
    assert "title" in response_body
    assert "body" in response_body
