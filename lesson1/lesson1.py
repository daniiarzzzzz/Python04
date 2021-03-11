class Human:
    class_name = 'Homo sapiens'

    def __init__(self, name, gender, race, height, weight):
        self.name = name
        self.gender = gender
        self.race = race
        self.height = height
        self.weight = weight


human1 = Human(height=20, name='Daniiar', weight=61, race='Mongol', gender='male')
human2 = Human(height=17, name='Aman', weight=66, race='Mongol', gender='male')


# print(human1.class_name, human1.name, human1.height, human1.weight, human1.race, human1.gender)
# print(human1.class_name, human2.name, human2.height, human2.weight, human2.race, human2.gender)


def infinite_loop():
    while 1:
        print("1")


# infinite_loop()
