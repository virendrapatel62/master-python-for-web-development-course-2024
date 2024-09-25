class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self) -> str:
        return f"{self.name} with age {self.age}"

    def get_average_grades(self):
        return sum(self.grades) / len(self.grades)


virendra = Student("Virendra", 24, [77, 89, 79])
harsh = Student("Harsh", 25, [87, 78, 79])

avg = virendra.get_average_grades()


print(avg)


print(virendra)
print(harsh)
