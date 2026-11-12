class Student:
    def __init__(self, name, number):
        if not isinstance(number, int) or isinstance(number, bool) or number < 5:
            raise ValueError("number must be at least 5")

        self.name = name
        self.number = number
        self.score = [0] * number

    def getName(self):
        return self.name

    def getScore(self, i):
        return self.score[i]

    def inputScore(self):
        for i in range(self.number):
            self.score[i] = float(input(f"Score for exam {i + 1}: "))

    def getAverage(self):
        return sum(self.score) / self.number

    def getHighScore(self):
        return max(self.score)

    def hasScholarship(self):
        return self.getAverage() > 8.0 and min(self.score) >= 4

    def __str__(self):
        return f"Student: {self.name}, scores: {self.score}"


if __name__ == "__main__":
    student = Student("An", 5)
    student.score = [9, 8, 8.5, 9.5, 8]
    print(student)
    print(student.getAverage())
    print(student.getHighScore())
    print(student.hasScholarship())
