from src.requests import get
import pytest


@pytest.allure.testcase("http://test-tracker/api-6")
@pytest.allure.feature("API-6: /{date}/ запрос без access_key")
@pytest.mark.parametrize("date", ["latest", "2018-10-30"])
def test_api_6(base, date):
    url = f"{base['url']}{date}"
    response: dict = get(url).json()

    assert response["success"] is False, "should have success == false"
    assert type(response["error"] is dict), "should have error in response"
    assert response["error"]["code"] == 101, "should have error code 101"
    assert response["error"]["type"] == "missing_access_key", "should have error message"
    assert response["error"]["info"] == "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]", \
        "should have additional info in response"
