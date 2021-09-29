from selenium.webdriver.common.by import By


class CoursePageLocators:
    FULLNAME_INPUT = (By.ID, "id_fullname")
    SHORTNAME_INPUT = (By.ID, "id_shortname")
    SAVE_AND_DISPLAY_BUTTON = (By.ID, "id_saveanddisplay")
    NOTIFICATION = (By.ID, "user-notifications")
