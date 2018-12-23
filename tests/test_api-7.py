from src.requests import get
import pytest


@pytest.allure.testcase("http://test-tracker/api-7")
@pytest.allure.feature("API-7: /{date}/ запрос c невалидным access_key")
@pytest.mark.parametrize("date", ["latest", "2008-09-29"])
@pytest.mark.parametrize("invalid_access_key", ["'select", "`", "foobar", "{"])
def test_api_7(base, date, invalid_access_key):
    url = f"{base['url']}{date}?access_key={invalid_access_key}"
    response: dict = get(url).json()

    assert response["success"] is False, "should have success == false"
    assert type(response["error"] is dict), "should have error in response"
    assert response["error"]["code"] == 101, "should have error code 101"
    assert response["error"]["type"] == "invalid_access_key", "should have error message"
    assert response["error"]["info"] == "You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]", \
        "should have additional info in response"
