import pytest

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
        page.open_profile()


class TestLongFirstname:
    @pytest.mark.profile
    @pytest.mark.parametrize(
        "firstname", [(99 * "a", 99), (100 * "a", 100), (101 * "a", 100)]
    )
    def test_long_firstname(self, app, user_page, firstname):
        """
        Firstname field has attribute maxlength=100
        Steps
        1. Type long firstname in firstname field
        2. Check changes
        """
        logger.info("Start test_long_firstname")
        text, result = firstname
        logger.info("Change field firstname")
        field_text = app.user_page.change_firstname(text)
        logger.info("Check changes")
        assert len(field_text) == result, "Assigned long firstname."
