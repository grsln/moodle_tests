from locators.auth import LoginPageLocators


class LoginPage:
    def __init__(self, app):
        self.app = app

    def auth(self, login: str, password: str):
        sign_in = self.app.driver.find_element(*LoginPageLocators.SIGN_IN)
        sign_in.click()
        username_input = self.app.driver.find_element(*LoginPageLocators.USERNAME)
        username_input.send_keys(login)
        password_input = self.app.driver.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        login_button = self.app.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
