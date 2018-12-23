from config.config import BASE_URL
from src.requests import Requests
import pytest
import sys

# hack to see output (curl) with xdist https://github.com/pytest-dev/pytest-xdist/issues/354
sys.stdout = sys.stderr


# https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def requests(request):
    print_curl = request.config.getoption("--showcurl")

    requester = Requests(print_curl, BASE_URL)
    yield requester

    if request.node.rep_call.failed:
        requester.show_curl()


def pytest_addoption(parser):
    parser.addoption("--showcurl", action='store_true', default=False, help="show curl")



