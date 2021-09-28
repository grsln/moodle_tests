import pytest
from selenium.common.exceptions import ElementClickInterceptedException

from conftest import logger
from models.profile import ProfileData


class TestUserPage:
    @pytest.mark.profile
    def test_change_field(self, app, auth):
        """
        Steps
        1. Open profile page
        2. Change fields with valid data
        3. Save changes
        4. Check changes
        """
        logger.info("Start test_change_field")
        app.open_user_page()
        page = app.user_page
        data = ProfileData().random()
        logger.info("Change and save fields")
        page.change_fields(data)
        logger.info("Check changes")
        assert page.is_changed(), "Cannot change fields."

    @pytest.mark.profile
    @pytest.mark.parametrize("field", ["firstname", "lastname", "email"])
    def test_required_fields_empty(self, app, auth, field):
        """
        Steps
        1. Open profile page
        2. Change required field with empty data
        3. Save changes
        4. Check changes
        """
        logger.info("Start test_required_fields_empty")
        app.open_user_page()
        page = app.user_page
        data = ProfileData().random()
        setattr(data, field, None)
        logger.info("Change and save fields")
        page.change_fields(data)
        logger.info("Check changes")
        assert page.is_error_required_field(), "No error message for required field."

    @pytest.mark.profile
    def test_long_firstname(self, app, auth):
        """
        Steps
        1. Open profile page
        2. Type long firstname in firstname field
        3. Check changes
        """
        logger.info("Start test_long_firstname")
        app.open_user_page()
        page = app.user_page
        logger.info("Change field firstname")
        firstnames = map(page.change_firstname, [99 * "a", 100 * "a", 101 * "a"])
        len_firstnames = list(map(len, firstnames))
        logger.info("Check changes")
        assert len_firstnames == [99, 100, 100], "Assigned long firstname."

    @pytest.mark.skip
    @pytest.mark.profile
    def test_usermenu(self, app, auth):
        """
        Steps
        1. Open profile page
        2. Change firstname with long string
        3. Save change
        4. Open user menu
        5. Check that menu not clickable
        """
        logger.info("Start test_long_firstname")
        app.open_user_page()
        page = app.user_page
        logger.info("Change field firstname")
        data = ProfileData().random()
        setattr(data, "firstname", 100 * "a")
        page.change_fields(data)
        logger.info("Check changes")
        with pytest.raises(ElementClickInterceptedException):
            page.open_profile()
