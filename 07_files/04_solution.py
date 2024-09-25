import json
file = None
students = list()

try:
    with open('student_data.json', 'r+') as file:
        data = file.read()
        try:
            students = json.loads(data)
        except json.decoder.JSONDecodeError:
            students = []
except FileNotFoundError:
    with open('student_data.json', 'w') as file:
        pass


with open('student_data.json', 'w') as file:
    name = input("Enter Student Name : ")
    age = int(input("Enter Student Age : "))
    student = {
        "name": name, "age": age
    }
    students.append(student)
    print(students)
    json_content = json.dumps(students)
    file.truncate(0)
    file.seek(0)
    file.write(json_content)

    print("Json written successfully")
