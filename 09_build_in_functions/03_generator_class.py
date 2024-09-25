class EvenNumberGenrator:
    def __init__(self) -> None:
        self.next_even = 0

    def __next__(self):
        number = self.next_even
        self.next_even += 2
        return number


even_number_generator = EvenNumberGenrator()


for i in range(20):
    print(next(even_number_generator))


# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
# print(next(even_number_generator))
