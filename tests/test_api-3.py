import pytest
from config.config import ACCESS_KEY


@pytest.allure.testcase("http://test-tracker/api-3")
@pytest.allure.feature("API-3: /{date}/ конкретные даты")
@pytest.mark.parametrize("date", ["2000-05-13", "2018-12-21", "2018-12-22"])
def test_api_3(requests, date):
    path = f"{date}?access_key={ACCESS_KEY}"
    response: dict = requests.get(path).json()

    assert response["success"] is True, "should have success == true"
    assert response["date"] == date, f"should have date equal {date}"
    assert response["historical"] is True, "should have 'historical' key"
