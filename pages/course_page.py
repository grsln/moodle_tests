from selenium.webdriver.remote.webelement import WebElement

from locators.course_page_locators import CoursePageLocators
from models.course import CourseData
from pages.base_page import BasePage


class CoursePage(BasePage):
    def fullname_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.FULLNAME_INPUT)

    def shortname_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.SHORTNAME_INPUT)

    def save_and_display_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.SAVE_AND_DISPLAY_BUTTON)

    def create_course(self, data: CourseData):
        self.fill_element(self.fullname_input(), data.fullname)
        self.fill_element(self.shortname_input(), data.shortname)
        self.click_element(self.save_and_display_button())

    def save_notification(self) -> WebElement:
        return self.find_element(CoursePageLocators.NOTIFICATION)

    def is_changed(self):
        return self.save_notification() is not None
