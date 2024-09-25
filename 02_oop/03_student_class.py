class Student():
    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} {self.grades}'

    def get_average(self):
        return sum(self.grades) / len(self.grades)


student = Student("virendra", 'patel', 24, [67, 76, 68, 99, 78])


average = student.get_average()
print("*****************************")
print(f"Average Grades : {average}")
print("*****************************")
