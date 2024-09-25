# Let's create our own function. The building blocks are:
# def
# the name
# brackets
# colon
# any code you want, but it must be indented if you want it to run as part of the function.

def say_hello():
    print('Hello User')


# say_hello()


# def greet_the_user():
#     pass

user = None  # global varibale


def greet_the_user():
    # local variable, can not acces outside of the function
    user = input("Enter Your Name : ")
    print(f"Hello {user}")


def greet_the_user():
    global user
    # this will assign value to global variable
    user = input("Enter Your Name : ")
    print(f"Hello {user}")


print(user)

greet_the_user()

print(user)
