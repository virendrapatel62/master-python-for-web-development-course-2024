numbers = {5, 3, 10, 0, 0, 0, 10, 10, "Virendra", "Virendra"}
# Un-Ordered List
# Unique , you can not add duplicate items
# you can manipulate set

numbers.add("Aditya")
numbers.remove(0)

print(numbers)

# numbers.pop()
numbers.remove(5)

print(numbers)
print(type(numbers))


print({1, 4,  2, 3, 5, 9}.difference({2, 3, 4, 10, 12}))
print({1, 4,  2, 3, 5, 9}.intersection({2, 3, 4, 10, 12}))
