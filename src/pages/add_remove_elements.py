from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from src.tests import config

class AddRemoveElementsPage(BasePage):
    _url = "/add_remove_elements/"
    _add_element_button = (By.XPATH, "//*[@id='content']/div/button")
    _delete_button = (By.CSS_SELECTOR, ".added-manually")

    def __init__(self, driver):
        self.driver = driver

    def visit_add_remove_elements_page(self):
        self._visit(self._url)

    def is_add_remove_elements_page(self):
        return self.driver.current_url == config.baseurl + self._url

    def is_add_element_button(self):
        return self._is_displayed(self._add_element_button, timeout=5)

    def add_element(self, count=1):
        while count > 0:
            self._find(self._add_element_button).click()
            count -= 1

    def count_delete_buttons(self):
        elements = 0
        if self._is_all_elements_located(self._delete_button, timeout=3):
            elements = self._find_all(self._delete_button)
        return len(elements) if elements != 0 else elements

    def delete_elements(self, count=-1):
        if count == -1:
            elements = 1
            while elements:
                elements = self._find_all(self._delete_button)
                elements[-1].click()
                elements = self._find_all(self._delete_button)
        else:
            while count:
                elements = self._find_all(self._delete_button)
                elements[-1].click()
                count -= 1