import re
import pytest
from config.config import ACCESS_KEY


@pytest.allure.testcase("http://test-tracker/api-2")
@pytest.allure.feature("API-2: /{date}/ схема ответа")
@pytest.mark.parametrize("date", ["latest", "2018-12-22"])
def test_api_2(requests, date):
    default_base = "EUR"
    symbols = ["CZK", "TOP", "ETB", "MZN", "XAU", "BOB", "MVR", "SCR", "NIO", "SGD", "ALL", "BDT", "DZD", "IMP", "IRR",
               "SBD", "ANG", "XAG", "SDG", "XAF", "GHS", "ILS", "MKD", "GIP", "USD", "ISK", "SAR", "QAR", "HTG", "SRD",
               "LAK", "PHP", "STD", "NZD", "SHP", "CUP", "INR", "JMD", "CNY", "DJF", "KES", "XDR", "GNF", "TJS", "TZS",
               "BRL", "KMF", "CUC", "VEF", "SEK", "BMD", "GEL", "ZWL", "MOP", "UAH", "XCD", "AWG", "OMR", "MGA", "MRO",
               "PYG", "JOD", "FKP", "AOA", "BTN", "MNT", "SZL", "BGN", "AUD", "RWF", "YER", "SYP", "CVE", "BSD", "BAM",
               "GYD", "HUF", "BZD", "WST", "TND", "BWP", "HNL", "KZT", "KHR", "LYD", "PKR", "UGX", "UYU", "LRD", "MUR",
               "MDL", "RSD", "BYR", "DKK", "VUV", "KPW", "JPY", "CLP", "CRC", "KGS", "PAB", "ZMK", "MYR", "CHF", "RON",
               "KYD", "LKR", "XPF", "FJD", "NPR", "GBP", "JEP", "PGK", "BBD", "TWD", "GMD", "AZN", "KRW", "COP", "LBP",
               "KWD", "IDR", "UZS", "NGN", "GGP", "AFN", "HKD", "SOS", "ZAR", "TMT", "BTC", "LVL", "BND", "TRY", "THB",
               "GTQ", "AED", "SVC", "LSL", "MXN", "MAD", "DOP", "NOK", "HRK", "CDF", "MWK", "EGP", "IQD", "SLL", "RUB",
               "ERN", "XOF", "ARS", "PEN", "TTD", "BYN", "ZMW", "PLN", "AMD", "MMK", "VND", "NAD", "LTL", "CLF", "CAD",
               "BHD", "BIF", "EUR"]

    path = f"{date}?access_key={ACCESS_KEY}"
    response: dict = requests.get(path).json()

    assert response["success"] is True, "should have success == true"
    assert bool(re.match(r"^\d+$", str(response["timestamp"]))), "should have timestamp"
    assert response["base"] == default_base, f"should have base {default_base} by default"
    assert type(response["rates"]) is dict, "rates should have type dict"

    rates: dict = response["rates"]

    assert list(rates.keys()).sort() == symbols.sort(), "should have countries in rates"

    for symbol in rates:
        symbol_type = type(rates[symbol])
        assert (symbol_type is float) or (symbol_type is int), f"{rates[symbol]} should be numeric"
        assert rates[symbol] > 0, f"{rates[symbol]} should be above 0"
