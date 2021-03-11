class Node:

    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent  # object of type Node

    def __str__(self):
        return self.name + ", " + str(self.parent)


ch = Node("Chyngyz Han", None)
djchi = Node("Jychi", ch)
ugd = Node("Ugedei", ch)
chgt = Node("Chagatai", ch)
tolui = Node("Toloi", ch)

uli = Node("Uluk", djchi)
air = Node("Airas", chgt)

print(uli)
print(air)
