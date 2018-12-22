from config.config import BASE_URL, ACCESS_KEY
import pytest


@pytest.fixture(scope="session")
def base():
    return {
        "url": BASE_URL,
        "access_key": ACCESS_KEY
    }

