from config.config import ACCESS_KEY
import pytest
import datetime


@pytest.allure.testcase("http://test-tracker/api-1")
@pytest.allure.feature("API-1: /{dates}/ latest")
def test_api_1(requests):
    path = f"latest?access_key={ACCESS_KEY}"
    now = datetime.datetime.now()
    today = f"{now.year}-{now.month}-{now.day}"

    response: dict = requests.get(path).json()

    assert response["success"] is True, "should have success == true"
    assert response["date"] == today, f"should have date equal {today}"
    assert "historical" not in response, "should not have 'historical' key"
