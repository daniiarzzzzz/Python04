# Data structures

class Queue:

    def __init__(self, arr):
        self.arr = arr

    def add(self, elem):
        self.arr.append(elem)

    def remove(self):
        self.arr.pop(0)

    def __str__(self):
        return str(self.arr)


q = Queue([1, 2, 3, 4])
print(q)
q.add(5)
q.remove()
print(f"q is  :{q}")


