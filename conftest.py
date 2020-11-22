import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    driver = None
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        print(f"\nStart {browser_name} browser\n")
    
    # elif browser_name == "firefox":
    #     profile = webdriver.FirefoxProfile()
    #     profile.accept_untrusted_certs = True
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
    #     print(f"\nStart {browser_name} browser\n")
    
    yield driver
    print("\nQuit browser\n")
    driver.quit()