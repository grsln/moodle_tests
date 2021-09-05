import pytest

from common.constants import LoginConstants
from conftest import logger
from models.auth import AuthData


class TestAuth:
    @pytest.mark.auth
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData(login="gabdrashitov", password="Password1@")
        app.login.auth(data)
        assert app.login.is_auth(), "We are not auth"

    @pytest.mark.auth
    def test_auth_invalid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with invalid data
        3. Check auth result
        """
        logger.info("Start test_auth_invalid_data")
        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    @pytest.mark.auth
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Steps
        1. Open main page
        2. Auth with empty data
        3. Check auth result
        """
        logger.info("Start test_auth_empty_data")
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, field, None)
        app.login.auth(data)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    @pytest.mark.auth
    @pytest.mark.parametrize("password", ["", "password"])
    def test_auth_valid_login(self, app, password):
        """
        Steps
        1. Open main page
        2. Auth with valid login and invalid password
        3. Check auth result
        """
        logger.info("Start test_auth_valid_login")
        app.open_auth_page()
        data = AuthData(login="gabdrashitov", password=password)
        app.login.auth(data)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"
