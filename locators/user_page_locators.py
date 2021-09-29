from selenium.webdriver.common.by import By

from common.constants import ProfileConstants


class UserPageLocators:
    USER_MENU = (By.CLASS_NAME, "usermenu")
    SETTINGS = (By.ID, "actionmenuaction-5")
    EDIT_PROFILE = (By.XPATH, f'//a[contains(@href,"{ProfileConstants.EDIT_PROFILE}")]')
    CITY = (By.ID, "id_city")
    SUBMIT_BUTTON = (By.ID, "id_submitbutton")
    NOTIFICATION = (By.ID, "user-notifications")
    EMAIL = (By.ID, "id_email")
    FIRSTNAME_INPUT = (By.ID, "id_firstname")
    LASTNAME_INPUT = (By.ID, "id_lastname")
    MAIL_DISPLAY_SELECT = (By.ID, "id_maildisplay")
    MOODLENET_INPUT = (By.ID, "id_moodlenetprofile")
    COUNTRY_SELECT = (By.ID, "id_country")
    TIMEZONE_SELECT = (By.ID, "id_timezone")
    DESCRIPTION_INPUT = (By.ID, "id_description_editoreditable")
    FILEMANAGER_CONTAINER = (By.CLASS_NAME, "filemanager-container")
    AVATAR_TAB = (By.ID, "id_moodle")
    AVATAR_INPUT = (By.ID, "id_imagefile")
    ADD_AVATAR_LINK = (By.XPATH, '//a[contains(@title,"Добавить...")]')
    AVATAR_FILE_INPUT = (By.XPATH, '//input[contains(@name,"repo_upload_file")]')
    UPLOAD_FILE_BUTTON = (By.XPATH, '//button[contains(text(), "Загрузить этот файл")]')
    OPENED_DIALOGS = (
        By.XPATH,
        '//div[@class="moodle-dialogue-base"][@aria-hidden="false"]',
    )
    LOAD_IMG = (By.CLASS_NAME, "realpreview")
    ERROR_DIV = (By.XPATH, '//div[contains(@id,"id_error")]')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="id_cancel"]')
