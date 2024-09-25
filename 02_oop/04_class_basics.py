class Product:
    def __init__(self, title, price, dicount):
        self.title = title
        self.price = price
        self.discount = dicount

    def __str__(self):
        return f"Product with the title {self.title}"

    def __repr__(self):
        return f"{self.title}, {self.price} , {self.discount}"


product = Product("Mac book", 99999, 30)
product2 = Product("Mouse", 999, 40)


print(str(product))
print(repr(product))
