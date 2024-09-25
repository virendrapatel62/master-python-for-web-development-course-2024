import random
import json

print(random.randint(0, 100))
print(random.randbytes(100))


print(json.dumps({"name": "virendra", "age": 24}))
print(json.dumps([4, 5, 6, 6]))

numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)
