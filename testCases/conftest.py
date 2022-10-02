import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching Ie Browser-----------------")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox Browser-----------------")
    else:
        driver = webdriver.Chrome()
        print("launching Chrome Browser-----------------")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### html reports##############

def pytest_configure(config):
    config._metadata['Project Name'] = "Nop commerce"
    config._metadata['module Name'] = "Customers"
    config._metadata['Tester Name'] = "Pravin"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
