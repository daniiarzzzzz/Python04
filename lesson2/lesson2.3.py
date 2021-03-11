num = 19 == 19


class Age:

    def __init__(self, age):
        self.age = age

    def __add__(self, other):
        age = self.age + other.age
        return Age(age)

    def __sub__(self, other):
        pass

    def __getitem__(self, key):
        return self.age

    def __eq__(self, other):
        return self.age == other.age

    @staticmethod
    def print_value():
        print("asdf")

    @property
    def get_age(self):
        return self.age * 10


age1 = Age(90)
age2 = Age(90)
age3 = age2
print(age3.get_age)
