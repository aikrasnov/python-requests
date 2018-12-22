import requests
import pytest


@pytest.allure.testcase("http://test-tracker/api-4")
@pytest.allure.feature("API-4: /{date}/ symbols")
@pytest.mark.parametrize("date", ["latest", "2011-01-22", "2005-04-01"])
@pytest.mark.parametrize("symbols", [["AED", "ZWL"], ["USD"], ["EUR"], ["USD", "EUR", "RUB"]])
def test_api_4(base, date, symbols):
    url = f"{base['url']}{date}?access_key={base['access_key']}&symbols={','.join(symbols)}"
    print(url)
    response: dict = requests.get(url).json()["rates"]

    assert list(response.keys()) == symbols, f"should have countries only from get-param {symbols}"
