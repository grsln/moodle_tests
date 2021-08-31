from faker import Faker

fake = Faker("Ru-ru")


class ProfileData:
    def __init__(self, email=None, city=None, country=None):
        self.email = email
        self.city = city
        self.country = country

    @staticmethod
    def random():
        email = fake.email()
        city = fake.city()
        country = fake.country()
        return ProfileData(email, city, country)
