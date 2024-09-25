
# { 1: 1 , 2 : 4 , 3: 9 }

# result = {}

# for index in range(1, 11):
#     result[index] = index * index

# print(result)


result = {
    number: number*number
    for number in range(1, 11)
    if number % 2 == 0
}

print(result)

result = {
    number: number*number
    for number in range(2, 11, 2)
}

print(result)
