from src.requests import get
import pytest


@pytest.allure.testcase("http://test-tracker/api-9")
@pytest.allure.feature("API-9: /{date}/ запрос c инвалидным base")
@pytest.mark.parametrize("date", ["latest", "2014-06-15"])
@pytest.mark.parametrize("api_base", ["123", "foo", "'select", "["])
def test_api_9(base, date, api_base):
    url = f"{base['url']}{date}?access_key={base['access_key']}&base={api_base}"
    response: dict = get(url).json()

    assert response["success"] is False, "should have success == false"
    assert type(response["error"] is dict), "should have error in response"
    assert response["error"]["code"] == 201, "should have error code 201"
    assert response["error"]["type"] == "invalid_base_currency", "should have error message"
