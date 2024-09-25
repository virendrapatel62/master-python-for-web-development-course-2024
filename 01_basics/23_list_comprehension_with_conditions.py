
numbers = [2, 3, 4, 5, 6, 7, 8]
# create another list by multiplying 10 if number is even
# [20, 30, 40, 50, 60 70, 80]

# result = []
# for number in numbers:
#     if number % 2 == 0:
#         result.append(number * 10)


result = [number*10 for number in numbers if number % 2 == 0]
doubleList = [number * 2 for number in numbers if number % 3 == 0]


print(result)
print(doubleList)


numbers_set = {1, 2, 3, 5}

double_number_set = {number * 2 for number in numbers if number == 2}

print(double_number_set)


names = ['pranav', 'vivek', 'aditya', 'rishabh']
relative = ['harsh', 'pranav', 'vivek']

invitation_list = [name for name in names if (name in relative)]

print(invitation_list)
# invite those who are your relaitve
