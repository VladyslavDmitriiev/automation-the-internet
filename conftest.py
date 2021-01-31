import os
import pytest
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from src.tests import config


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--baseurl", action="store", default="https://the-internet.herokuapp.com", help="base URL for the app")


@pytest.fixture(scope="function")
def driver(request):
    driver = None
    browser_name = request.config.getoption("--browser_name")
    config.baseurl = request.config.getoption("--baseurl")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        print(f"\nStart {browser_name} browser\n")
        print(f"THE BASE URL: {config.baseurl}")
    
    # elif browser_name == "firefox":
    #     profile = webdriver.FirefoxProfile()
    #     profile.accept_untrusted_certs = True
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
    #     print(f"\nStart {browser_name} browser\n")
    
    yield driver

    # TODO: Check if screenshots folder is created.
    # TODO: Group screenshots by runs.
    screenshot_time = datetime.now().strftime("%d.%m.%Y_%H:%M:%S")
    screenshot_path = "src/tests/screenshots"
    screenshot_new_run_path = screenshot_path + "/" + config.new_run_time_dir
    if not os.path.exists(screenshot_path):
        os.mkdir(screenshot_path)
    if not os.path.exists(screenshot_new_run_path):
        os.mkdir(screenshot_new_run_path)

    if config.failed_tests != request.node.session.testsfailed:
        config.failed_tests += 1
        driver.save_screenshot(f"{screenshot_new_run_path}/{screenshot_time}_{request.node.name}.png")
    print(f"Test status code: {request.node.session.testsfailed}")

    print("\nQuit browser\n")
    driver.quit()