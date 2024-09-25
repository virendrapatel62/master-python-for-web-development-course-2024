student = {
    "name": 'Virendra',
    "age": 24,
    "address": 'Jabalpur MP',
    "device": 'Mac book pro',
    "phone": "5894589468"
}

for key in student.keys():
    print(f"{key} : {student.get(key)}")

for key, value in student.items():
    print(f"{key} : {value}")
