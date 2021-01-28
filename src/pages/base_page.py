from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.tests import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            print(f"Open page: {url}")
            self.driver.get(url)
        else:
            print(f"Open page: {config.baseurl + url}")
            self.driver.get(config.baseurl + url)

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _find_all(self, locator):
        return self.driver.find_elements(*locator)

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator, timeout=0):
        
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.visibility_of_element_located(locator))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _is_all_elements_located(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.presence_of_all_elements_located(locator))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False