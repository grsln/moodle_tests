from pages.login_page import LoginPage
from pages.user_page import UserPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.user_page = UserPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def open_user_page(self):
        self.driver.get(self.url + "/user/editadvanced.php")
