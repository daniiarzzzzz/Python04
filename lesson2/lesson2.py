class Animal:

    def __init__(self, color, size, brain):
        self.color = color
        self.size = size
        self.brain = brain

    def birth(self):
        return "YA RODYLSYA"

    def live(self):
        return "YA JIVU"

    def death(self):
        return "YA UMER"


class Parrot(Animal):

    def __init__(self, color, size, brain, wings, tail, beak):
        super(Parrot, self).__init__(color, size, brain)
        self.wings = wings
        self.tail = tail
        self.beak = beak

    def birth(self):
        return "YA VYLUPILSYA"


class Kakadu(Parrot):

    def __init__(self, color, size, brain, wings, tail, beak, scallop):
        super(Kakadu, self).__init__(color, size, brain, wings, tail, beak)
        self.scallop = scallop

    def live(self):
        return "YA LIVE IN A JUNGLE"

    def death(self):
        return "HEROIC DEATH"


animal = Animal(color='white', size=100, brain=5)
parrot = Parrot(color='black', size=100, brain=5, wings=1000000, tail=10, beak=3)
kakadu = Kakadu(color='black', size=100, brain=5, wings=1000000, tail=10, beak=3, scallop=312)

print(animal.color, animal.size, animal.brain)
print(parrot.color, parrot.size, parrot.brain, parrot.wings)
print(kakadu.birth())
print(parrot.birth())
print(animal.birth())
print()
print(kakadu.live())
print(parrot.live())
print(animal.live())
print()
print(kakadu.death())
print(animal.death())
print(parrot.death())
