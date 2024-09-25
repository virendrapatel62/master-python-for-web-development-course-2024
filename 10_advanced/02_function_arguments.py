

def update_name(local_student, name):
    print(id(local_student))
    local_student['name'] = name


student = {
    "name": 'Virendra', "age": 24
}

print(id(student))
update_name(student, "harsh")
print(student)
