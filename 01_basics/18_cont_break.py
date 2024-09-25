
'''
itr over all the elements when you find even number
you have to print
Yess we found the even number
you you fint odd number  break the loop
No We found odd number
'''

# numbers = [2, 4, 6, 8, 10, 11, 12, 16, 18]

# for number in numbers:
#     if (number % 2 == 0):
#         print("Yes we found an even number", number)
#         continue

#     print("No we found an odd number", number)
#     break


# print("End Loop")


"""
for i in range(10):
    print(i)
    if (i < 5):
        continue
    else:
        break


for i in range(5):
    print(i)

"""


lectures = ["working",
            'working',
            'working',
            'fault',
            'working',
            'working']

# case 1 : watch the videos which are working
# case 2 : stop watching videos when you find faulty video


for status in lectures:
    if (status == 'fault'):
        break

    print("Watching the video")

for status in lectures:
    if (status == 'fault'):
        continue

    print("Watching the video")
