def sum(a, b, c):
    print(f"a : {a} , b : {b} , c : {c}")
    return a + b + c


numbers = [23, 45, 77]
numbers = (23, 45, 77)

# ans = sum(numbers[0], numbers[1], numbers[2])
ans = sum(*numbers)
print(ans)


def login(email, password):
    print(f"email : {email}")
    print(f"password : {password}")


user = {
    "email": 'patelvirendra62@gmail.com',
    'password': '989847584'
}
login(user['email'], user['password'])
login(email=user['email'], password=user['password'])
login(**user)


args = [12, 13, 14, 90]
args2 = {
    "f": "FFF", "g": "GG"
}


def demo(a, v, c, d, f, g):
    print(f"a : {a}, v : {v}, c : {c}, d : {d}, f : {f}, g : {g}")


demo(*args, **args2)
