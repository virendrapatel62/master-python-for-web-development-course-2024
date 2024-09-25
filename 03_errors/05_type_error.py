"""
Create a Python program that simulates a school class.
The program should have a School class that can add students.
When a student object is passed to the add_student method,
the method should check the type of the object.
If the object is not of type Student,
a TypeError should be raised with a descriptive message.
"""


class Student:
    def __init__(self, name) -> None:
        self.name = name


class HighSchoolStudent(Student):
    pass


class School:
    def __init__(self, name) -> None:
        self.name = name

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("student must be of type Student")

        print("Admission successfull...")
        print(f"Student Name is {student.name}")


school = School('MKHHS')
virendra = Student("Virendra")
harsh = HighSchoolStudent("Harsh")

# school.add_student(90)
school.add_student(harsh)
