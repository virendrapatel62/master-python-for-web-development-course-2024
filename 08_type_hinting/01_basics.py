import datetime


def getTime() -> datetime.datetime:
    return datetime.datetime.now()


time = getTime()
print(time)


def sum(a: int, b: int) -> int:
    return a + b


ans = sum(122, 32)

print(ans)


class Student:
    def __init__(self) -> None:
        pass

    def run():
        print("Running studnet")


class School:

    def __init__(self) -> None:
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def get_all_students(self) -> list[Student]:
        return self.students


school = School()
school.add_student(Student())
school.add_student(Student())
print(school.get_all_students())
