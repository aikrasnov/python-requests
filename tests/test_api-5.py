from src.requests import get
import pytest


@pytest.allure.testcase("http://test-tracker/api-5")
@pytest.allure.feature("API-5: /{date}/ данные не по всем странам из списка")
def test_api_5(base):
    country_with_data = "AED"
    country_without_data = "ZWL"
    date = "2011-01-22"

    url = f"{base['url']}{date}?access_key={base['access_key']}&symbols={country_with_data},{country_without_data}"
    response: dict = get(url).json()

    assert response["success"] is True, "should have success == true"
    assert list(response["rates"].keys()) == [country_with_data], \
        f"should have only {country_with_data}, not {country_without_data}"
