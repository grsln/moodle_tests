from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGN_IN = (By.LINK_TEXT, "Вход")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    ACCOUNT_NAME = (By.CLASS_NAME, "usertext")
