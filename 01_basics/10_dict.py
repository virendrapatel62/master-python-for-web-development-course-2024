student_ages = {
    "virendra": 24,
    "vivek": 48,
    "adiya": 24
}

student_ages["virendra"] = 25
student_ages["harsh"] = 10

print(student_ages["virendra"])
print(student_ages)
print(type(student_ages))

# print(student_ages.clear())
# print(student_ages.items())

print(student_ages.get('sandeep'))  # None

student_ages.update({"cm": 34})

print(student_ages)


# create a list of students with name with ages

students = [
    {
        "name": "Virendra", 'age': 24, "marks": [23, 3, 46,]
    },
    {
        "name": "Vivek", 'age': 28,  "marks": [345, 5, 54546,]
    },
    {
        "name": "Aditya", 'age': 37
    }
]
print(students)


print(students[0].get("marks")[0])
