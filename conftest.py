import logging

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application

logger = logging.getLogger("moodle")


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    if headless.lower() == "true":
        chrome_options.add_argument("--headless")
    fixture = Application(
        webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
        base_url,
    )
    yield fixture
    fixture.quit()


def auth_fixture(request, app):
    app.open_auth_page()
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    data = AuthData(login=username, password=password)
    app.login.auth(data)


@pytest.fixture
def auth(request, app):
    auth_fixture(request, app)


@pytest.fixture(scope="class")
def user_page(request, app):
    auth_fixture(request, app)
    app.open_user_page()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "app" in item.fixturenames:
                web_driver = item.funcargs["app"]
            else:
                logger.error("Fail to take screen-shot")
                return
            logger.info("Screen-shot done")
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            logger.error("Fail to take screen-shot: {}".format(e))


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="gabdrashitov",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Password1@",
        help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter headless true or false",
    ),
