def generate_bill(item_name, unit_price, quantity):
    total_cost = unit_price * quantity
    return (f"Bill For {item_name} : {unit_price} x {quantity} = {total_cost}")


message = generate_bill("Mac Book", 99999, 10)
print(message)


def generate_bill(item_name, unit_price, quantity):
    total_cost = unit_price * quantity
    return total_cost


cost = generate_bill("Mac Book", 99999, quantity=10)
print(cost)
# generate_bill("Keyboard", 2300, 9)


def print_table(number):  # number parameter
    for index in range(1, 11):
        print(f"{number} x {index} = {number*index}")


# print_table(10)  # 10 is argument
# print_table(14)  # 10 is argument


def get_even_numbers(count):
    numbers = []
    for index in range(0, count * 2 + 1, 2):
        numbers.append(index)
    return numbers


def get_even_numbers(count):
    return [number for number in range(0, count * 2 + 1, 2)]


even_numbers = get_even_numbers(20)
print(even_numbers)


def get_user_name():
    return {}


print(get_user_name())
