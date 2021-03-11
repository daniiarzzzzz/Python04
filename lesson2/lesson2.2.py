class Tech:

    def __init__(self, energy):
        self.energy = energy


class Phone(Tech):

    def __init__(self, size):
        self.size = size


class TouchScreenWork:

    def touch(self):
        print("TouchScreenWork")


class KeyboardWork:

    def press(self):
        print("KeyboardWork")


class Samsung(Phone):

    def __init__(self, ):
        pass


class S21(TouchScreenWork, Samsung):
    pass


class KeyboardSamsung(KeyboardWork, Samsung):
    pass


k = KeyboardSamsung()
ts = S21()

print(k.press())
print(ts.touch())
