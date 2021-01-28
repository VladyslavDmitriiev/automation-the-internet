from src.pages.login_page import LoginPage
from src.pages.secure_zone import SecureZonePage

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.visit_login_page()
    assert login_page.is_login_page()
    login_page.perform_login(("tomsmith", "SuperSecretPassword!"))

    secure_zone_page = SecureZonePage(login_page.driver)
    secure_zone_page.is_secure_zone_page()
    assert secure_zone_page.is_success_message()
    assert secure_zone_page.success_message_content() == "You logged into a secure area!\n×"
    assert secure_zone_page.is_logout_button()
    secure_zone_page.perform_logout()

    login_page = LoginPage(secure_zone_page.driver)
    login_page.is_login_page()
    login_page.is_success_message()
    assert login_page.success_message_content() == "You logged out of the secure area!\n×"
    # input("Debug time...\n")