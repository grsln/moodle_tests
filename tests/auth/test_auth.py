class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_auth_page()
        app.login.auth(login="gabdrashitov", password="Password1@")
        assert app.login.is_auth(), "We are not auth"
