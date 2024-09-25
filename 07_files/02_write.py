# file = open("data.txt", 'w')
# file.write("Somthing in the file")
# file.close()


file_name = input("Enter File name : ")
content = input("write something to the file : ")

file = open(file_name, 'w')
file.write(content)
file.close()
