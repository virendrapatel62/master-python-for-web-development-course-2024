import json

students = [
    {"name": 'Virendra', 'age': 24}
]

# file = open('students.json', 'w')
# file.write(json.dumps(students))
# file.close()


file = open('students.json', 'r')
json_content = file.read()
data = json.loads(json_content)
file.close()

print(data[0].get('name'))
