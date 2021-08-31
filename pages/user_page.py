from selenium.webdriver.remote.webelement import WebElement

from locators.user_page_locators import UserPageLocators
from models.profile import ProfileData
from pages.base_page import BasePage


class UserPage(BasePage):
    def firstname_input(self) -> WebElement:
        return self.find_element(UserPageLocators.FIRSTNAME)

    def lastname_input(self) -> WebElement:
        return self.find_element(UserPageLocators.LASTNAME)

    def email_input(self) -> WebElement:
        return self.find_element(UserPageLocators.EMAIL)

    def mail_display_input(self) -> WebElement:
        return self.find_element(UserPageLocators.MAIL_DISPLAY)

    def moodlenet_profile(self) -> WebElement:
        return self.find_element(UserPageLocators.MOODLENET_PROFILE)

    def city_input(self) -> WebElement:
        return self.find_element(UserPageLocators.CITY)

    def country_input(self) -> WebElement:
        return self.find_element(UserPageLocators.COUNTRY)

    def timezone_input(self) -> WebElement:
        return self.find_element(UserPageLocators.TIMEZONE)

    def file_input(self) -> WebElement:
        return self.find_element(UserPageLocators.FILEMANAGER_CONTAINER)

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

    def change_fields(self, data: ProfileData):
        fields = {
            'city': self.city_input,
            'email': self.email_input}
        for key in fields.keys():
            self.fill_element(fields[key](), getattr(data, key))
        self.set_value_select(self.country_input(), data.country)
        self.click_element(self.submit_button())

    def is_changed(self):
        return self.save_notification() is not None
