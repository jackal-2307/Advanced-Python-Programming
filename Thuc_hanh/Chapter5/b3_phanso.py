from math import gcd


class PHANSO:
    def __init__(self, tu_so=0, mau_so=1):
        if mau_so == 0:
            raise ValueError("mau_so must not be zero")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def input(self):
        self.tu_so = int(input("Numerator: "))
        self.mau_so = int(input("Denominator: "))
        if self.mau_so == 0:
            raise ValueError("mau_so must not be zero")

    def reduce(self):
        divisor = gcd(self.tu_so, self.mau_so)
        self.tu_so //= divisor
        self.mau_so //= divisor
        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so
        return self

    def reciprocal(self):
        if self.tu_so == 0:
            raise ZeroDivisionError("zero has no reciprocal")
        return PHANSO(self.mau_so, self.tu_so)

    def __str__(self):
        reduced = PHANSO(self.tu_so, self.mau_so).reduce()
        return f"{reduced.tu_so}/{reduced.mau_so}"

    def my_addition(self, other):
        numerator = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        denominator = self.mau_so * other.mau_so
        return PHANSO(numerator, denominator).reduce()

    def my_subtract(self, other):
        numerator = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        denominator = self.mau_so * other.mau_so
        return PHANSO(numerator, denominator).reduce()

    def my_multi(self, other):
        return PHANSO(
            self.tu_so * other.tu_so,
            self.mau_so * other.mau_so,
        ).reduce()

    def my_division(self, other):
        if other.tu_so == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return PHANSO(
            self.tu_so * other.mau_so,
            self.mau_so * other.tu_so,
        ).reduce()

    def __add__(self, other):
        if not isinstance(other, PHANSO):
            return NotImplemented
        return self.my_addition(other)

    def __sub__(self, other):
        if not isinstance(other, PHANSO):
            return NotImplemented
        return self.my_subtract(other)

    def __mul__(self, other):
        if not isinstance(other, PHANSO):
            return NotImplemented
        return self.my_multi(other)

    def __truediv__(self, other):
        if not isinstance(other, PHANSO):
            return NotImplemented
        return self.my_division(other)


if __name__ == "__main__":
    first = PHANSO(2, 3)
    second = PHANSO(3, 4)
    print(first + second)
    print(first - second)
    print(first * second)
    print(first / second)
    print(first.reciprocal())
