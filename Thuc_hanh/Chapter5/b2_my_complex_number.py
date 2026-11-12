from math import hypot


class MyComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {abs(self.imaginary)}i"
        return f"{self.real} + {self.imaginary}i"

    def input(self):
        self.real = float(input("Real part: "))
        self.imaginary = float(input("Imaginary part: "))

    def my_addition(self, other):
        return MyComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary,
        )

    def my_subtract(self, other):
        return MyComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary,
        )

    def my_multi(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return MyComplexNumber(real, imaginary)

    def my_division(self, other):
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ZeroDivisionError("cannot divide by zero")

        real = (
            self.real * other.real + self.imaginary * other.imaginary
        ) / denominator
        imaginary = (
            self.imaginary * other.real - self.real * other.imaginary
        ) / denominator
        return MyComplexNumber(real, imaginary)

    def magnitude(self):
        return hypot(self.real, self.imaginary)

    def compare(self, other):
        if self.magnitude() < other.magnitude():
            return -1
        if self.magnitude() > other.magnitude():
            return 1
        return 0

    def __add__(self, other):
        if not isinstance(other, MyComplexNumber):
            return NotImplemented
        return self.my_addition(other)

    def __sub__(self, other):
        if not isinstance(other, MyComplexNumber):
            return NotImplemented
        return self.my_subtract(other)

    def __mul__(self, other):
        if not isinstance(other, MyComplexNumber):
            return NotImplemented
        return self.my_multi(other)

    def __truediv__(self, other):
        if not isinstance(other, MyComplexNumber):
            return NotImplemented
        return self.my_division(other)

    def __eq__(self, other):
        if not isinstance(other, MyComplexNumber):
            return NotImplemented
        return self.real == other.real and self.imaginary == other.imaginary

    def __lt__(self, other):
        if not isinstance(other, MyComplexNumber):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def __gt__(self, other):
        if not isinstance(other, MyComplexNumber):
            return NotImplemented
        return self.magnitude() > other.magnitude()


if __name__ == "__main__":
    first = MyComplexNumber(10, 2)
    second = MyComplexNumber(3, -1)
    print(first + second)
    print(first - second)
    print(first * second)
    print(first / second)
    print(first.magnitude())
    print(first.compare(second))
