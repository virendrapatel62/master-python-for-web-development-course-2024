
class Student:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class School:
    def __init__(self) -> None:
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self):
        # return (student for student in self.students)
        return iter(self.students)


school = School()
school.add_student(Student("Virendra"))
school.add_student(Student("Harsh"))
school.add_student(Student("Rishabh"))
school.add_student(Student("Aditya"))
school.add_student(Student("Vivek"))

for student in school:
    print(student)


print(iter([1, 2]))
