from models.profile import ProfileData


class TestUserPage:
    def test_change_field(self, app, auth):
        """
        Steps
        1. Open profile page
        2. Change field
        3. Save changes
        4. Check changes
        """
        page = app.user_page
        page.open_profile()
        data = ProfileData().random()
        page.change_fields(data)
        assert page.is_changed(), "Cannot change fields."
