from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from src.tests import config


class MainPage(BasePage):
    _url = "/"
    _links = (By.CSS_SELECTOR, "li a")

    def __init__(self, driver):
        super().__init__(driver)

    def visit_main_page(self):
        self._visit(config.baseurl)

    def is_main_page(self):
        return self.driver.current_url == config.baseurl + self._url

    def get_links_count(self):
        return len(self._find_all(self._links))

    def validate_all_links(self):
        """
        The current method clicks on every page link and matches it with the real page URL.
        Returns an empty dictionary if all hrefs are matching with the real page URLs
        """

        href_vs_actual_url = {}
        links_count = len(self._find_all(self._links))
        for i in range(links_count):
            links = self._find_all(self._links)
            href = links[i].get_attribute("href")
            links[i].click()
            if self.driver.current_url != href:
                href_vs_actual_url.update({href: self.driver.current_url})
            self.driver.back()
        return href_vs_actual_url
