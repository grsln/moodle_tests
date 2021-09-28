import pytest

from conftest import logger
from models.course import CourseData


class TestCoursePage:
    @pytest.mark.course
    def test_create_course(self, app, auth):
        """
        Steps
        1. Open course page
        2. Fill fields with valid data
        3. Save changes
        4. Check changes
        """
        logger.info("Start test_create_course")
        app.open_course_page()
        page = app.course_page
        data = CourseData().random()
        logger.info("Create course")
        page.create_course(data)
        logger.info("Check changes")
        assert page.is_changed(), "Cannot change fields."
