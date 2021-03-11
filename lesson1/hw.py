class Fraction:

    def __init__(self, num, denum):
        if denum == 0:
            raise ValueError("Denumenator can't 0")

        self.num = num
        self.denum = denum

    def __add__(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = other.denum + self.num
        return Fraction(num, denum)

    def __sub__(self, other):
        num = self.num * other.denum - other.num * self.denum
        denum = other.denum + self.num
        return Fraction(num, denum)

    def multiply(self, other):
        num = self.num * other.denum
        denum = other.denum * self.num
        return Fraction(num, denum)

    def div(self, other):
        num = self.num * other.num
        denum = other.denum * self.denum
        return Fraction(num, denum)


fraction1 = Fraction(1, 2)  # 1/2
fraction2 = Fraction(2, 3)  # 2/3
# fraction3 = fraction1 - fraction2 + fraction2 - fraction2
#
for i in range(10):
    fraction2 += fraction1

print(fraction2.num, "|", fraction2.denum)
