import requests
import pytest


# @pytest.mark.parametrize("text", ["foobar", "бесплатно", "без регистрации", "中文"])
@pytest.allure.testcase("http://test-tracker/api-1")
@pytest.allure.feature("API-1: /latest/")
def test_api_1(base):
    url = f"{base['url']}latest?access_key={base['access_key']}"
    response = requests.get(url).json()

    print(response)

    assert response["success"] is True, "should have success == true"
    assert response["timestamp"]

