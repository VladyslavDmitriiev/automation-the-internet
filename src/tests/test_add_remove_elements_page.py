from src.pages.add_remove_elements import AddRemoveElementsPage

def test_add_remove_elements_page(driver):
    add_remove_elements_page = AddRemoveElementsPage(driver)
    add_remove_elements_page.visit_add_remove_elements_page()
    assert add_remove_elements_page.is_add_remove_elements_page()
    assert add_remove_elements_page.is_add_element_button()
    add_remove_elements_page.add_element(50)
    assert add_remove_elements_page.count_delete_buttons() == 50
    add_remove_elements_page.delete_elements(25)
    add_remove_elements_page.add_element(5)
    assert add_remove_elements_page.count_delete_buttons() == 30