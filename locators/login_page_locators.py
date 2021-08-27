from selenium.webdriver.common.by import By

from common.constants import LoginConstants


class LoginPageLocators:
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "loginbtn")
    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN_LINK = (By.PARTIAL_LINK_TEXT, LoginConstants.LOGIN_URL)
    LOGIN_ERROR = (By.ID, "loginerrormessage")
    MODAL_BODY = (By.ID, "modal-body")
    LOGOUT_BUTTON = (By.XPATH, "//form[@action='" + LoginConstants.LOGOUT_URL + "']")
