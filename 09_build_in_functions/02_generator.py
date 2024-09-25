
# numbers = []

# for i in range(0, 1000):
#     numbers.append(i)

# print(numbers)

# def get_number():
#     for i in range(0, 1000):
#         yield i  # 0, 1


# gen = get_number()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))  # 5


# enerator comprehension.
number_genrator = (i for i in range(10))

try:
    number = next(number_genrator)
    while (number is not None):
        print(number)
        number = next(number_genrator)
except StopIteration:
    print("No new Number to print")

# for number in number_genrator:
#     print(number)
