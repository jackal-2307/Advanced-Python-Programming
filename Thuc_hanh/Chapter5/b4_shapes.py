from math import pi


class Shape:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def findarea(self):
        pass

    def findperimeter(self):
        pass

    def __str__(self):
        return self.name


class Circle(Shape):
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def findarea(self):
        return pi * self.radius**2

    def findperimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def findarea(self):
        return self.width * self.height

    def findperimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, color, name, length):
        super().__init__(color, name, length, length)

    def findarea(self):
        return self.width**2

    def findperimeter(self):
        return 4 * self.width


if __name__ == "__main__":
    circle = Circle("blue", "Circle", 3)
    rectangle = Rectangle("red", "Rectangle", 4, 5)
    square = Square("green", "Square", 4)
    for shape in (circle, rectangle, square):
        print(shape, shape.findarea(), shape.findperimeter())
