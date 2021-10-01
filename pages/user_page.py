from os.path import abspath, dirname

from selenium.webdriver.remote.webelement import WebElement

from locators.user_page_locators import UserPageLocators
from models.profile import ProfileData
from pages.base_page import BasePage


class UserPage(BasePage):
    def firstname_input(self) -> WebElement:
        return self.find_element(UserPageLocators.FIRSTNAME_INPUT)

    def lastname_input(self) -> WebElement:
        return self.find_element(UserPageLocators.LASTNAME_INPUT)

    def email_input(self) -> WebElement:
        return self.find_element(UserPageLocators.EMAIL)

    def mail_display_input(self) -> WebElement:
        return self.find_element(UserPageLocators.MAIL_DISPLAY_SELECT)

    def moodlenet_profile(self) -> WebElement:
        return self.find_element(UserPageLocators.MOODLENET_INPUT)

    def city_input(self) -> WebElement:
        return self.find_element(UserPageLocators.CITY)

    def country_input(self) -> WebElement:
        return self.find_element(UserPageLocators.COUNTRY_SELECT)

    def timezone_input(self) -> WebElement:
        return self.find_element(UserPageLocators.TIMEZONE_SELECT)

    def file_input(self) -> WebElement:
        return self.find_element(UserPageLocators.FILEMANAGER_CONTAINER)

    def avatar_tab(self) -> WebElement:
        return self.find_element(UserPageLocators.AVATAR_TAB)

    def add_avatar_link(self) -> WebElement:
        return self.find_element(UserPageLocators.ADD_AVATAR_LINK)

    def avatar_file_input(self) -> WebElement:
        return self.find_element(UserPageLocators.AVATAR_FILE_INPUT)

    def upload_file_button(self) -> WebElement:
        return self.find_element(UserPageLocators.UPLOAD_FILE_BUTTON)

    def avatar_input(self) -> WebElement:
        return self.find_element(UserPageLocators.AVATAR_INPUT)

    def is_opened_dialogs(self) -> bool:
        elements = self.find_elements(UserPageLocators.OPENED_DIALOGS)
        if len(elements) > 0:
            return True
        return False

    def load_img(self) -> WebElement:
        return self.find_element(UserPageLocators.LOAD_IMG)

    def submit_button(self) -> WebElement:
        return self.find_element(UserPageLocators.SUBMIT_BUTTON)

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
            "firstname": self.firstname_input,
            "lastname": self.lastname_input,
            "city": self.city_input,
            "email": self.email_input,
        }
        for key in fields.keys():
            self.fill_element(fields[key](), getattr(data, key))

        self.set_value_select(self.country_input(), data.country_code)

        self.click_element(self.avatar_tab())
        self.click_element(self.add_avatar_link())
        self.avatar_file_input().send_keys(
            f"{self.get_tests_path()}/common/images/robot.jpeg"
        )
        self.click_element(self.upload_file_button())
        if self.is_opened_dialogs():
            self.find_element(UserPageLocators.LOAD_IMG)

        self.click_element(self.submit_button())

    def is_changed(self):
        return self.save_notification() is not None

    def is_error_required_field(self):
        elements = self.find_elements(UserPageLocators.ERROR_DIV)
        if len(elements) > 0:
            return True
        return False

    def firstname_length(self):
        element = self.firstname_input()
        return len(element.get_attribute("value"))

    def change_firstname(self, text):
        firstname_element = self.firstname_input()
        self.fill_element(firstname_element, text)
        return firstname_element.get_attribute("value")

    def cancel_button(self):
        return self.find_element(UserPageLocators.CANCEL_BUTTON)

    def cancel_edit(self):
        self.click_element(self.cancel_button())

    @staticmethod
    def get_tests_path():
        return dirname(dirname(abspath(__file__)))
