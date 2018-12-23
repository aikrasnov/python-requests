from config.config import ACCESS_KEY
import pytest


@pytest.allure.testcase("http://test-tracker/api-9")
@pytest.allure.feature("API-9: /{date}/ запрос c инвалидным base")
@pytest.mark.parametrize("date", ["latest", "2014-06-15"])
@pytest.mark.parametrize("api_base", ["123", "foo", "'select", "["])
def test_api_9(requests, date, api_base):
    path = f"{date}?access_key={ACCESS_KEY}&base={api_base}"
    response: dict = requests.get(path).json()

    assert response["success"] is False, "should have success == false"
    assert type(response["error"] is dict), "should have error in response"
    assert response["error"]["code"] == 201, "should have error code 201"
    assert response["error"]["type"] == "invalid_base_currency", "should have error message"
