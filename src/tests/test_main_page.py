from src.pages.main_page import MainPage


def test_main_page(driver):
    main_page = MainPage(driver)
    main_page.visit_main_page()
    assert main_page.is_main_page()
    assert main_page.get_links_count() == 44
    assert main_page.validate_all_links() == {}, "Some href are not matching with the real page URL"

