
numbers = [2, 3, 4, 5, 6, 7, 8]
# create another list by multiplying 10
# [20, 30, 40, 50, 60 70, 80]

result = [number*10 for number in numbers]
doubleList = [number * 2 for number in numbers]

# result = []
# for number in numbers:
#     result.append(number * 10)

print(result)
print(doubleList)


numbers_set = {1, 2, 3, 5}

double_number_set = {number * 2 for number in numbers}

print(double_number_set)
