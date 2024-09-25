
age = 17

if age >= 18:
    print('You can vote')

# friends = ['sandeep', 'pranav', 'vivek', 'aditya', 'rishabh']

# user_input = input("Enter you friend's name : ")

# if user_input in friends:
#     print("Invite to party")
# else:
#     print("Do not invite, he/she is not your friend")


friends = ["aditya", 'vivek', 'pranav']
family = ['sandeep', 'priya', 'swapnil']

name = input("Enter a name : ")

if name in friends:
    print("He is your friend")
elif name in family:
    print("He is your family")
else:
    print("He is neither your family member nor friend")


print("End...")
