import pytest
from application import Application


@pytest.fixture(scope="session")  # Run all tests in one session
def app(request):                 # Fixture for Selenium Web driver
    global fixture
    browser = request.config.getoption("--browser")
    project = request.config.getoption("--project")
    fixture = Application(browser, project)

    def fin():
        fixture.destroy()         # function for destroy Selenium fixture
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):     # hooks for browsers, by default = Chrome
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--project", action="store", default="99papers")


def pytest_report_header(config):  # invitation in console before test run is "On"
    if config.getoption("verbose") > 0:
        return ["Lucky - Labs Automation tests is start"]