from faker import Faker

fake = Faker("Ru-ru")


class ProfileData:
    def __init__(self, city=None):
        self.city = city

    @staticmethod
    def random():
        city = fake.city()
        return ProfileData(city)
