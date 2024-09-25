class School:
    def __init__(self) -> None:
        pass

    def add_student(self, name):
        raise NotImplementedError("This method is in progress")


school = School()

try:
    school.add_student("Virendra")
except NotImplementedError:
    print("We are on it..")
    print("come again later")
