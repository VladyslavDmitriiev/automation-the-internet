from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    _url = "https://the-internet.herokuapp.com/login"
    _form_username = (By.ID, "username")
    _form_password = (By.ID, "password")
    _button_login = (By.CLASS_NAME, "fa-sign-in")
    _button_logout = (By.NAME, "Logout")
    _all_login_form_fields = (_form_username, _form_password)

    def __init__(self, driver):
        self.driver = driver

    def _perform_login(self, form_inputs):
        field = 0
        for form_input in form_inputs:
            self._type(self._all_login_form_fields[field], form_input)
            field += 1
        self._click(self._button_login)
