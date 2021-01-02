from src.pages.add_remove_elements import AddRemoveElements

def test_add_remove_elements_page(driver):
    add_remove_elements_page = AddRemoveElements(driver)
    add_remove_elements_page.visit_add_remove_elements_page()
    assert add_remove_elements_page.is_add_remove_elements_page()
    assert add_remove_elements_page.is_add_element_button()
    elements_count = 50
    add_remove_elements_page.add_element(elements_count)
    assert add_remove_elements_page.count_delete_buttons() == elements_count
    add_remove_elements_page.delete_elements()
    assert add_remove_elements_page.count_delete_buttons() == 0