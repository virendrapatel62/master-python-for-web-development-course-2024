'''
file reading
csv to dict
dict to json 
json write file
'''

import csv
import json

print("Welcome to csv to json covertor: Enter file names without extensions")
csv_file_name = f"{input('Enter csv file name:')}.csv"
json_file_name = f"{input("Enter Json file name: ")}.json"
students = []

with open(csv_file_name ,'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for student in reader:
        students.append(student)

with open(json_file_name ,'w') as json_file:
    json.dump(students , fp=json_file , indent=4 ) 
    print("Written to the file..")