import requests
import pytest
import datetime


@pytest.allure.testcase("http://test-tracker/api-1")
@pytest.allure.feature("API-1: /{dates}/ latest")
def test_api_1(base):
    url = f"{base['url']}latest?access_key={base['access_key']}"
    now = datetime.datetime.now()
    today = f"{now.year}-{now.month}-{now.day}"

    response: dict = requests.get(url).json()

    assert response["date"] == today, f"should have date equal {today}"
    assert "historical" not in response, "should not have 'historical' key"
