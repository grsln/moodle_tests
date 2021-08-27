from selenium.webdriver.remote.webelement import WebElement

from locators.login_page_locators import LoginPageLocators
from models.auth import AuthData
from pages.base_page import BasePage


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def is_confirm(self):
        elements = self.find_elements(LoginPageLocators.LOGOUT_BUTTON)
        if len(elements) > 0:
            return True
        return False

    def email_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def logout_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGOUT_BUTTON)

    def auth_login_error(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text

    def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.is_confirm():
            self.click_element(self.logout_button())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())
