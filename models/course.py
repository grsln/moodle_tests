import datetime
import random

from faker import Faker

from common.constants import CourseConstants

fake = Faker("Ru-ru")


class CourseData:
    def __init__(
        self,
        fullname=None,
        shortname=None,
        end_day=None,
        end_month=None,
        end_year=None,
        end_hour=None,
        end_minute=None,
        course_description=None,
        section_number=None,
        course_language=None,
        max_file_size=None,
        manager_name=None,
        teacher_name=None,
        student_name=None,
    ):
        self.fullname = fullname
        self.shortname = shortname
        self.end_day = end_day
        self.end_month = end_month
        self.end_year = end_year
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.course_description = course_description
        self.section_number = section_number
        self.course_language = course_language
        self.max_file_size = max_file_size
        self.manager_name = manager_name
        self.teacher_name = teacher_name
        self.student_name = student_name

    @staticmethod
    def random():
        fullname = fake.job() + str(datetime.datetime.now())
        shortname = fake.word() + str(datetime.datetime.now())
        end_day = str(random.randint(1, 28))
        end_month = str(random.randint(1, 12))
        end_year = str(
            random.randint(CourseConstants.CURRENT_YEAR, CourseConstants.LAST_YEAR)
        )
        end_hour = str(random.randint(0, 23))
        end_minute = str(random.randint(0, 59))
        course_description = fake.text(max_nb_chars=200)
        section_number = str(random.randint(0, CourseConstants.SECTION_NUMBER))
        course_language = CourseConstants.COURSE_LANGUAGE
        max_file_size = str(random.choice(CourseConstants.FILE_SIZES_VALUES))
        manager_name = fake.word()
        teacher_name = fake.word()
        student_name = fake.word()
        return CourseData(
            fullname,
            shortname,
            end_day,
            end_month,
            end_year,
            end_hour,
            end_minute,
            course_description,
            section_number,
            course_language,
            max_file_size,
            manager_name,
            teacher_name,
            student_name,
        )
