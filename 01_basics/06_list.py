
even_numbers = [0, 2, 4, 6, 8]
# [0 ,1, 2, 3, 4]
# [1, 2, 4, 6, 8]

print("Even Numbers : ", even_numbers)
print("Even Numbers : ", len(even_numbers))
print("First Numbe : ", even_numbers[0])
print("second Numbe : ", even_numbers[1])
print("third Numbe : ", even_numbers[2])


students = ["Virendra", 'Somil', "Pranav"]
print(len(students), students)
print(students[2])

students[1] = "Vivek"
students.append("Aditya")

print(students)

students.remove("Virendra")
print(students)

removed_student = students.pop()
print(removed_student)
print(students)

students.reverse()
print(students)

student_marks = [
    ["Virendra", 99],
    ["Vivek", 45],
    ["Pranav", 33],
    ["Aditya", 89],
    ["Rishabh", 90],
]

print(student_marks[2][0])
print(student_marks[2][1])
