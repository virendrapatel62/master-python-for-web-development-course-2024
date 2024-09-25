'''
age = 24
age2 = age
age3 = 24
name = 'virendra'
name2 = 'virendra'
age4 = 25


print(id(name))
print(id(name2))

name = name + " patel"
print(name, id(name))

caps = name.capitalize()

print(caps, id(caps))


# print(id(age))
# print(id(age2))
# print(id(age3))
# print(id(age4))

# print(id(name))
# print(id(name2))


t = (1, 24)

t[1] = 24

print(t)
'''


'''
numbers = [1, 2, 34, 56, 77, 88]
print(numbers)
print(id(numbers))

numbers.append(100)

print(numbers)
print(id(numbers))


student = {
    "name": 'Virendra', 'age': 24
}

print(student)
print(id(student))

student['address'] = 'Jabalpur'
student['name'] = 'harsh'

print(student)
print(id(student))
'''


class Student:
    def __init__(self, name) -> None:
        self.name = name

    def run():
        print("Running studnet")

    def __str__(self) -> str:
        return self.name


s1 = Student("Virendra")


print(s1)
print(id(s1))

s1.name = 'harsh'

print(id(s1))
