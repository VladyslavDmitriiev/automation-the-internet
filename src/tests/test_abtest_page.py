from src.pages.abtest import AbTest


def test_abtest_page(driver):
    abtest_page = AbTest(driver)
    abtest_page.visit_abtest_page()
    assert abtest_page.is_abtest_page()
    assert abtest_page.text_page_header() == "A/B Test Control" or "A/B Test Variation 1"
    assert abtest_page.text_page_paragraph() == "Also known as split testing. This is a way in which businesses are " +\
        "able to simultaneously test and learn different versions of a page to see which text and/or functionality " +\
        "works best towards a desired outcome (e.g. a user action such as a click-through)."
