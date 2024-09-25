def say_hello():
    print("Hello User")


greet = say_hello

def send_email():
    print("Sending Email...")


def place_order(action):
    print('Placing an order')
    action()

def send_notification():
    print('Sending Notification')


place_order(send_email)
place_order(send_notification)



def function_that_returns_function():
    def inner_function():
        print("Message from inner Function")
    
    print("Message From outer function")

    return inner_function



inner = function_that_returns_function()
print("Now going to call inner funcion")
inner()