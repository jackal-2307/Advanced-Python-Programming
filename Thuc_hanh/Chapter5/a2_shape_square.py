class Shape:
    def getarea(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def getarea(self):
        return self.length * self.length


if __name__ == "__main__":
    print(Shape().getarea())
    print(Square(4).getarea())
