from faker import Faker

fake = Faker("Ru-ru")


class ProfileData:
    def __init__(
        self,
        firstname=None,
        lastname=None,
        email=None,
        city=None,
        country_code=None,
        avatar=None,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.city = city
        self.country_code = country_code
        self.avatar = avatar

    @staticmethod
    def random():
        firstname = fake.first_name_male()
        lastname = fake.last_name_male()
        email = fake.email()
        city = fake.city()
        country_code = fake.country_code()
        return ProfileData(firstname, lastname, email, city, country_code)
