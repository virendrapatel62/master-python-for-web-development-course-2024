from typing import List
import json
file_name = 'todos.json'

class DataWriterAndReader:
    def __init__(self) -> None:
        pass

    @classmethod
    def read_from_file(cls) -> List[str]:
        print(f"reading from the file")
        data = []
        with open(file_name) as todos_file:
            content =todos_file.read()
            data = json.loads(content)
        return data

    @classmethod
    def write_to_file(cls , todos : List[str] ):
        with open(file_name , 'w') as todos_file:
            json.dump(todos , fp=todos_file , indent=4)
    

class Database:
    def __init__(self) -> None:
        self.todos = DataWriterAndReader.read_from_file()

    def add_todo(self, content):
        self.todos.append(content)
        DataWriterAndReader.write_to_file(self.todos)
    
    def remove_todo(self , index):
        print(f"Removing todo : {index}")
        self.todos = self.todos[: index] + self.todos[index + 1: ]
        DataWriterAndReader.write_to_file(self.todos)

class Controller:
    def __init__(self) -> None:
        self.db = Database()

    def add_todo(self):
        print("Lets Add todo")
        todo = input("Enter your todo message : ")
        self.db.add_todo(todo)

    def remove_todo(self):
        print("Lets Remove todo")
        index = int(input("Enter the todo number: ") )- 1
        self.db.remove_todo(index)

    def show_all(self):
        print("Lets Show All Todos")
        print(self.db.todos)

intial_options = """
Press 1 : Add Todos
Press 2 : Remove Todo
Press 3 : Show All Todos
Press 9 : exit

Waiting for input : 
"""
controller = Controller()

while True:
    option = int(input(intial_options))
    if option is 1:
        controller.add_todo()
    elif option is 2:
        controller.remove_todo()
    elif option is 3:
        controller.show_all()
    elif option is 9:
        print("Thank you !!")
        break;
    


