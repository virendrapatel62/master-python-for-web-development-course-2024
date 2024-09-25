class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def speak(self):
        return f"hello from {self.name}"


class Student(Person):
    def __init__(self, name, age, school) -> None:
        super().__init__(name, age)
        self.school = school

    def speak(self):
        return f"hello from {self.name} , i am studing in {self.school}"


# person = Person("Virendra", 24)
# message = person.speak()
# print(message)

# student = Student("Harsh", 25, 'MKHHS')
# message = student.speak()
# print(message)
