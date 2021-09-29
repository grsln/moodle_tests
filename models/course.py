from faker import Faker

fake = Faker("Ru-ru")


class CourseData:
    def __init__(
        self,
        fullname=None,
        shortname=None,
    ):
        self.fullname = fullname
        self.shortname = shortname

    @staticmethod
    def random():
        job = fake.job()
        fullname = job
        shortname = job
        return CourseData(fullname=fullname, shortname=shortname)
