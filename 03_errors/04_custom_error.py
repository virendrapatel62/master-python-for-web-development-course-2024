class AdmissionClosed(Exception):
    def __init__(self, message, count):
        super().__init__(message)
        self.count = count


class School:
    count = 0

    def __init__(self) -> None:
        pass

    def add_student(self, name):

        if School.count == 5:
            raise AdmissionClosed("We are full", School.count)

        School.count += 1
        print("Student Added")


school = School()

school.add_student('A')
school.add_student('A')
school.add_student('A')
school.add_student('B')
school.add_student('C')

# school.add_student('Vierndra')

try:
    school.add_student('Vierndra')
except AdmissionClosed as e:
    print(e.count, str(e))
