class Stack:

    def __init__(self, arr):
        self.arr = arr

    def add(self, elem):
        self.arr.append(elem)

    def remove(self):
        self.arr.pop()

    def __str__(self):
        return str(self.arr)


stack = Stack([])
stack.add("a")
stack.add("i")
stack.add("r")
stack.add("a")
stack.add("s")
print(stack)
stack.remove()
stack.remove()
print(stack)
stack.add("A")
stack.add("S")
stack.add("$")
print(stack)
