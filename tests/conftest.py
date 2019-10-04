import pytest
from base.webdriverfactory import WebDriverFactory

# Main Configuration function where browsers will be called and killed
@pytest.yield_fixture(scope="class")
def baseSetUp(browser, request):

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


# Gets the type of browser required from the user
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

