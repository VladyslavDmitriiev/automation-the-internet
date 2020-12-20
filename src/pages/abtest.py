from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.tests import config


class AbTest(BasePage):
    _url = "/abtest"
    _page_header = (By.CSS_SELECTOR, ".example h3")
    _page_paragraph = (By.CSS_SELECTOR, ".example p")

    def __init__(self, driver):
        self.driver = driver

    def visit_abtest_page(self):
        self._visit(self._url)

    def is_abtest_page(self):
        return self.driver.current_url == config.baseurl + self._url

    def text_page_header(self):
        return self._find(self._page_header).text if self._is_displayed(self._page_header, 3) else "No element"

    def text_page_paragraph(self):
        return self._find(self._page_paragraph).text if self._is_displayed(self._page_paragraph) else "No element"