# find all the prime number from 1-20

# 4 -> 2 , 3 False
# 5 -> 2 , 3, 4, Prime

for number in range(2, 21):
    for index in range(2, number):
        remainder = number % index
        if remainder == 0:
            print(f"{number} is Not Prime Number")
            break
    else:
        print(f"{number} is Prime Number")
