from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from locators.course_page_locators import CoursePageLocators
from models.course import CourseData
from pages.base_page import BasePage


class CoursePage(BasePage):
    def __init__(self, app):
        super(CoursePage, self).__init__(app)
        self.fullname = None

    def fullname_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.FULLNAME_INPUT)

    def shortname_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.SHORTNAME_INPUT)

    def open_course_format_section(self):
        self.click_element(self.find_element(CoursePageLocators.COURSE_FORMAT_DATA))

    def open_appearance_section(self):
        self.click_element(self.find_element(CoursePageLocators.APPEARANCE_DATA))

    def open_file_section(self):
        self.click_element(self.find_element(CoursePageLocators.FILE_DATA))

    def open_role_rename_section(self):
        self.click_element(self.find_element(CoursePageLocators.ROLE_RENAME_DATA))

    def end_day_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_DAY)

    def end_month_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_MONTH)

    def end_year_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_YEAR)

    def end_hour_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_HOUR)

    def end_minute_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.END_MINUTE)

    def course_description_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_DESCRIPTION)

    def section_number_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.SECTION_NUMBER)

    def course_language_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_LANGUAGE)

    def max_file_size_select(self) -> WebElement:
        return self.find_element(CoursePageLocators.MAX_FILE_SIZE)

    def manager_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.MANAGER_NAME)

    def teacher_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.TEACHER_NAME)

    def student_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.STUDENT_NAME)

    def save_and_show_button(self):
        return self.find_element(CoursePageLocators.SAVE_AND_SHOW_BUTTON)

    def select_end_day(self, value):
        self.set_value_select(self.end_day_select(), value)

    def select_end_month(self, value):
        self.set_value_select(self.end_month_select(), value)

    def select_end_year(self, value):
        self.set_value_select(self.end_year_select(), value)

    def select_end_hour(self, value):
        self.set_value_select(self.end_hour_select(), value)

    def select_end_minute(self, value):
        self.set_value_select(self.end_minute_select(), value)

    def input_course_description(self, text):
        self.fill_element(self.course_description_input(), text)

    def select_section_number(self, value):
        self.set_value_select(self.section_number_select(), value)

    def select_course_language(self, value):
        self.set_value_select(self.course_language_select(), value)

    def select_max_file_size(self, value):
        self.set_value_select(self.max_file_size_select(), value)

    def input_manager_name(self, name):
        self.fill_element(self.manager_name_input(), name)

    def input_teacher_name(self, name):
        self.fill_element(self.teacher_name_input(), name)

    def input_student_name(self, name):
        self.fill_element(self.student_name_input(), name)

    def save_and_display_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.SAVE_AND_DISPLAY_BUTTON)

    def create_course(self, data: CourseData):
        self.fullname = data.fullname
        self.fill_element(self.fullname_input(), data.fullname)
        self.fill_element(self.shortname_input(), data.shortname)
        self.select_end_day(data.end_day)
        self.select_end_month(data.end_month)
        self.select_end_year(data.end_year)
        self.select_end_hour(data.end_hour)
        self.select_end_minute(data.end_minute)
        self.input_course_description(data.course_description)
        self.open_course_format_section()
        self.select_section_number(data.section_number)
        self.open_appearance_section()
        self.select_course_language(data.course_language)
        self.open_file_section()
        self.select_max_file_size(data.max_file_size)
        self.open_role_rename_section()
        self.input_manager_name(data.manager_name)
        self.input_teacher_name(data.teacher_name)
        self.input_student_name(data.student_name)
        self.click_element(self.save_and_display_button())

    def save_notification(self) -> WebElement:
        return self.find_element(CoursePageLocators.NOTIFICATION)

    def is_changed(self):
        return self.save_notification() is not None

    def go_to_manage_courses(self) -> WebElement:
        return self.click_element(
            self.find_element(CoursePageLocators.MANAGE_COURSES_BUTTON)
        )

    def delete_course(self):
        return self.click_element(
            self.find_elements(CoursePageLocators.DELETE_COURSE_BUTTON)[1]
        )

    def confirm_delete(self) -> WebElement:
        return self.click_element(
            self.find_element(CoursePageLocators.CONFIRM_DELETE_BUTTON)
        )

    def delete_created_course(self):
        self.app.open_course_manage_page()
        self.find_course_by_full_name(self.fullname)
        self.delete_course()
        self.confirm_delete()

    def is_full_course_name_error(self) -> bool:
        element = self.find_elements(CoursePageLocators.FULLNAME_ERROR)
        if len(element) > 0:
            return True
        return False

    def is_short_course_name_error(self) -> bool:
        element = self.find_elements(CoursePageLocators.SHORTNAME_ERROR)
        if len(element) > 0:
            return True
        return False

    def is_course_name_error(self):
        if self.is_short_course_name_error() or self.is_full_course_name_error():
            return True
        return False

    def find_course_by_full_name(self, course_name) -> WebElement:
        return self.find_element((By.XPATH, f"//a[text()='{course_name}']"))

    def find_delete_confirmation(self) -> str:
        return self.find_elements(CoursePageLocators.COURSE_DELETE_CONFIRMATION)[1].text

    def quit(self):
        self.click_element(self.find_element(CoursePageLocators.USER_MENU))
        self.click_element(self.find_element(CoursePageLocators.EXIT))
