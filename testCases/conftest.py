from selenium import webdriver
import pytest


# This setup method will be common for all test cases
@pytest.fixture()
def setup(browser):              # Here we initialized wedriver with respective browser driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Chrome Browser")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("FireFox Browser")
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(10)  # Define waits for all successive webelement before throwing any Exceptions
    return driver


def pytest_addoption(parser):     #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):              #This will return the browser value to setup method
    return request.config.getoption("--browser")

# pytest HTML Report

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Amazon Add To Cart'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Yogiraj Khade'



