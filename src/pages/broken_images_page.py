from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from src.tests import config


class BrokenImagesPage(BasePage):
    _url = "/broken_images"
    _images = (By.CSS_SELECTOR, "img")

    def __init__(self, driver):
        super().__init__(driver)

    def visit_broken_images_page(self):
        self._visit(self._url)

    def is_broken_images_page(self):
        return self.driver.current_url == config.baseurl + self._url

    def are_no_broken_images(self):
        images = self._find_all(self._images)
        images_size = [image.get_attribute("naturalWidth") for image in images]
        for i in images_size:
            if int(i) == 0:
                return False
        return True