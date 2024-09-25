def add_numbers(a, b):
    return a + b

add_numbers = lambda a, b : a+b

result = add_numbers(10, 12)

# def clc_average(list = []):
#     result = sum(list) / len(list)
#     return result

clc_average = lambda list: sum(list) / len(list)

print(result)

print(clc_average([1, 2, 3, 4, 5]))
