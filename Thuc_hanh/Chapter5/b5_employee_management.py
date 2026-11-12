import re
from datetime import date


class Employee:
    Employee_count = 0
    Employee_type = None

    def __init__(self, ID, FullName, BirthDay, Phone, Email):
        if not self.isValidName(FullName):
            raise ValueError("FullName is not valid")
        if not self.isValidBirthDay(BirthDay):
            raise ValueError("BirthDay must be a valid date in YYYY-MM-DD format")
        if not self.isValidPhone(Phone):
            raise ValueError("Phone must contain 7 to 15 digits")
        if not self.isValidEmail(Email):
            raise ValueError("Email is not valid")

        self.__ID = ID
        self.__FullName = FullName
        self.__BirthDay = BirthDay
        self.__Phone = Phone
        self.__Email = Email
        Employee.Employee_count += 1

    @staticmethod
    def isValidName(name):
        if not isinstance(name, str):
            return False
        allowed_punctuation = " -'."
        return bool(name.strip()) and all(
            character.isalpha() or character in allowed_punctuation
            for character in name
        )

    @staticmethod
    def isValidBirthDay(birthday):
        if not isinstance(birthday, str):
            return False
        try:
            birth_date = date.fromisoformat(birthday)
        except ValueError:
            return False
        return birth_date <= date.today()

    @staticmethod
    def isValidPhone(phone):
        if not isinstance(phone, str):
            return False
        return re.fullmatch(r"\+?[0-9]{7,15}", phone) is not None

    @staticmethod
    def isValidEmail(email):
        if not isinstance(email, str):
            return False
        return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) is not None

    def getID(self):
        return self.__ID

    def getFullName(self):
        return self.__FullName

    def getBirthDay(self):
        return self.__BirthDay

    def getPhone(self):
        return self.__Phone

    def getEmail(self):
        return self.__Email

    def showMe(self):
        return (
            f"ID: {self.getID()}\n"
            f"Name: {self.getFullName()}\n"
            f"Birthday: {self.getBirthDay()}\n"
            f"Phone: {self.getPhone()}\n"
            f"Email: {self.getEmail()}\n"
            f"Employee type: {self.Employee_type}"
        )

    def ShowInfo(self):
        print(self.showMe())


class Experience(Employee):
    Employee_type = 0

    def __init__(
        self, ID, FullName, BirthDay, Phone, Email, ExpInYear, ProSkill
    ):
        super().__init__(ID, FullName, BirthDay, Phone, Email)
        self.__ExpInYear = ExpInYear
        self.__ProSkill = ProSkill

    def showMe(self):
        return (
            f"{super().showMe()}\n"
            f"Experience years: {self.__ExpInYear}\n"
            f"Professional skill: {self.__ProSkill}"
        )


class Fresher(Employee):
    Employee_type = 1

    def __init__(
        self,
        ID,
        FullName,
        BirthDay,
        Phone,
        Email,
        Graduation_date,
        Graduation_rank,
        Education,
    ):
        super().__init__(ID, FullName, BirthDay, Phone, Email)
        self.__Graduation_date = Graduation_date
        self.__Graduation_rank = Graduation_rank
        self.__Education = Education

    def showMe(self):
        return (
            f"{super().showMe()}\n"
            f"Graduation date: {self.__Graduation_date}\n"
            f"Graduation rank: {self.__Graduation_rank}\n"
            f"Education: {self.__Education}"
        )


class Intern(Employee):
    Employee_type = 2

    def __init__(
        self,
        ID,
        FullName,
        BirthDay,
        Phone,
        Email,
        Majors,
        Semester,
        University_name,
    ):
        super().__init__(ID, FullName, BirthDay, Phone, Email)
        self.__Majors = Majors
        self.__Semester = Semester
        self.__University_name = University_name

    def showMe(self):
        return (
            f"{super().showMe()}\n"
            f"Major: {self.__Majors}\n"
            f"Semester: {self.__Semester}\n"
            f"University: {self.__University_name}"
        )


class EmployeeManagement:
    def __init__(self):
        self.__employees = []

    def addEmployee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("employee must be an Employee")
        self.__employees.append(employee)
        return employee

    def addExperience(
        self, ID, FullName, BirthDay, Phone, Email, ExpInYear, ProSkill
    ):
        employee = Experience(
            ID, FullName, BirthDay, Phone, Email, ExpInYear, ProSkill
        )
        return self.addEmployee(employee)

    def addFresher(
        self,
        ID,
        FullName,
        BirthDay,
        Phone,
        Email,
        Graduation_date,
        Graduation_rank,
        Education,
    ):
        employee = Fresher(
            ID,
            FullName,
            BirthDay,
            Phone,
            Email,
            Graduation_date,
            Graduation_rank,
            Education,
        )
        return self.addEmployee(employee)

    def addIntern(
        self,
        ID,
        FullName,
        BirthDay,
        Phone,
        Email,
        Majors,
        Semester,
        University_name,
    ):
        employee = Intern(
            ID,
            FullName,
            BirthDay,
            Phone,
            Email,
            Majors,
            Semester,
            University_name,
        )
        return self.addEmployee(employee)

    def findInterns(self):
        return [
            employee for employee in self.__employees if isinstance(employee, Intern)
        ]

    def findExperiences(self):
        return [
            employee
            for employee in self.__employees
            if isinstance(employee, Experience)
        ]

    def findFreshers(self):
        return [
            employee for employee in self.__employees if isinstance(employee, Fresher)
        ]


if __name__ == "__main__":
    management = EmployeeManagement()
    management.addExperience(
        "E01", "An Nguyen", "2000-05-10", "+84123456789", "an@example.com", 5, "Python"
    )
    management.addFresher(
        "F01", "Binh Tran", "2002-08-20", "0123456789", "binh@example.com",
        "2025-06-01", "Good", "ABC University",
    )
    management.addIntern(
        "I01", "Chi Le", "2004-01-15", "0987654321", "chi@example.com",
        "Computer Science", 2, "XYZ University",
    )

    assert len(management.findInterns()) == 1
    assert len(management.findExperiences()) == 1
    assert len(management.findFreshers()) == 1
    management.findInterns()[0].ShowInfo()
