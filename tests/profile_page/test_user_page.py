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
        page = app.user_page
        page.open_profile()
        data = ProfileData().random()
        page.change_fields(data)
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
        logger.info("Start test_firstname_with_invalid_data")
        page = app.user_page
        page.open_profile()
        data = ProfileData().random()
        setattr(data, field, None)
        page.change_fields(data)
        assert page.is_error_required_field(), "No error message for required field."
