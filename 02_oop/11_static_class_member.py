class FeelFreeToCodeCourse:
    author_name = 'Virendra'

    def __init__(self, title, description, price, duration) -> None:
        self.title = title
        self.description = description
        self.price = price
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.title} at {self.price} of {self.duration} hr"

    def display_result(self) -> str:
        print(f"{self.title} at {self.price} of {self.duration} hr")

    @classmethod
    def get_discounted_price(cls, price, percent):
        print(cls, price, percent, cls.author_name)
        return 99


javascript = FeelFreeToCodeCourse("Javscript", "Complete Js Course", 999, 10)
python = FeelFreeToCodeCourse("python", "Complete Python Course", 1999, 15)


javascript.display_result()
python.display_result()

value = FeelFreeToCodeCourse.get_discounted_price(javascript.price, 10)
print(value)


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


c = Calculator()

print(c.add(12, 12))
