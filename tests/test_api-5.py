from config.config import ACCESS_KEY
import pytest


@pytest.allure.testcase("http://test-tracker/api-5")
@pytest.allure.feature("API-5: /{date}/ данные не по всем странам из списка")
def test_api_5(requests):
    country_with_data = "AED"
    country_without_data = "ZWL"
    date = "2011-01-22"

    path = f"{date}?access_key={ACCESS_KEY}&symbols={country_with_data},{country_without_data}"
    response: dict = requests.get(path).json()

    assert response["success"] is True, "should have success == true"
    assert list(response["rates"].keys()) == [country_with_data], \
        f"should have only {country_with_data}, not {country_without_data}"
