from selenium.webdriver.remote.webelement import WebElement

from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    def city_input(self) -> WebElement:
        return self.find_element(UserPageLocators.CITY)

    def submit_button(self) -> WebElement:
        return self.find_element(UserPageLocators.SUBMIT)

    def save_notification(self) -> WebElement:
        return self.find_element(UserPageLocators.NOTIFICATION)

    def user_menu(self) -> WebElement:
        return self.find_element(UserPageLocators.USER_MENU)

    def profile_settings(self) -> WebElement:
        return self.find_element(UserPageLocators.SETTINGS)

    def edit_profile(self) -> WebElement:
        return self.find_element(UserPageLocators.EDIT_PROFILE)

    def open_profile(self):
        self.click_element(self.user_menu())
        self.click_element(self.profile_settings())
        self.click_element(self.edit_profile())

    def change_fields(self, data):
        self.fill_element(self.city_input(), data.city)
        self.click_element(self.submit_button())

    def is_changed(self):
        return self.save_notification() is not None
