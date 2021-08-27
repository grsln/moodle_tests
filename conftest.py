import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless.lower() == "true":
        chrome_options.add_argument("--headless")
    fixture = Application(
        webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
        base_url,
    )
    yield fixture
    fixture.quit()


@pytest.fixture
def auth(request, app):
    app.open_auth_page()
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    data = AuthData(login=username, password=password)
    app.login.auth(data)


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
