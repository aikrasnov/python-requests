from config.config import BASE_URL, ACCESS_KEY
import pytest
import sys

# hack to see output (curl) with xdist https://github.com/pytest-dev/pytest-xdist/issues/354
sys.stdout = sys.stderr


@pytest.fixture(scope="session")
def base():
    return {
        "url": BASE_URL,
        "access_key": ACCESS_KEY
    }
