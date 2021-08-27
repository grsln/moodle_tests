from selenium.webdriver.common.by import By

from common.constants import ProfileConstants


class UserPageLocators:
    USER_MENU = (By.CLASS_NAME, "usermenu")
    SETTINGS = (By.ID, "actionmenuaction-5")
    EDIT_PROFILE = (By.XPATH, f'//a[contains(@href,"{ProfileConstants.EDIT_PROFILE}")]')
    CITY = (By.ID, "id_city")
    SUBMIT = (By.ID, "id_submitbutton")
    NOTIFICATION = (By.ID, "user-notifications")
    EMAIL = (By.ID, "id_email")
