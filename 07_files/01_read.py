# file = open("data.txt", 'r')
# content = file.read()
# file.close()
# print(content)


with open("data.txt", 'r') as file:
    content = file.read()
    print(content)
