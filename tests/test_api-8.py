from config.config import ACCESS_KEY
import pytest


@pytest.allure.testcase("http://test-tracker/api-8")
@pytest.allure.feature("API-8: /{date}/ запрос c не дефолтным base")
@pytest.mark.parametrize("date", ["latest", "2004-03-19"])
@pytest.mark.parametrize("api_base", ["BAM", "MDL", "XOF"])
def test_api_8(requests, date, api_base):
    path = f"{date}?access_key={ACCESS_KEY}&base={api_base}"
    response: dict = requests.get(path).json()

    assert response["success"] is False, "should have success == false"
    assert type(response["error"] is dict), "should have error in response"
    assert response["error"]["code"] == 105, "should have error code 105"
    assert response["error"]["type"] == "base_currency_access_restricted", "should have error message"
