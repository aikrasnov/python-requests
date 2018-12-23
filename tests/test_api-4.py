import pytest
from config.config import ACCESS_KEY


@pytest.allure.testcase("http://test-tracker/api-4")
@pytest.allure.feature("API-4: /{date}/ symbols")
@pytest.mark.parametrize("date", ["latest", "2011-01-22", "2005-04-01"])
@pytest.mark.parametrize("symbols", [["AED"], ["USD"], ["EUR"], ["USD", "EUR", "RUB"]])
def test_api_4(requests, date, symbols):
    path = f"{date}?access_key={ACCESS_KEY}&symbols={','.join(symbols)}"
    response: dict = requests.get(path).json()

    assert response["success"] is True, "should have success == true"
    assert list(response["rates"].keys()) == symbols, f"should have countries only from get param {symbols}"
