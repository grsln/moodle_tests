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
    FIRSTNAME = (By.ID, "id_firstname")
    LASTNAME = (By.ID, "id_lastname")
    MAIL_DISPLAY = (By.ID, "id_maildisplay")
    MOODLENET_PROFILE = (By.ID, "id_moodlenetprofile")
    COUNTRY = (By.ID, "id_country")
    TIMEZONE = (By.ID, "id_timezone")
    DESCRIPTION = (By.ID, "id_description_editoreditable")
    FILEMANAGER_CONTAINER = (By.CLASS_NAME, "filemanager-container")
