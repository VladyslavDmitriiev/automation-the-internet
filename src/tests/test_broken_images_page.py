from src.pages.broken_images_page import BrokenImagesPage


def test_broken_images_page(driver):
    broken_images_page = BrokenImagesPage(driver)
    broken_images_page.visit_broken_images_page()
    assert broken_images_page.is_broken_images_page()
    assert broken_images_page.are_no_broken_images()