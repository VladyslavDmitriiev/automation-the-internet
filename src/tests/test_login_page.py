from pages.login_page import LoginPage

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page._visit(login_page._url)
    login_page._perform_login(("tomsmith", "SuperSecretPassword!"))

    input("Debug time...\n")