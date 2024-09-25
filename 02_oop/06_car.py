class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

    def __str__(self) -> str:
        return f"{self.brand} {self.model} released on {self.year}"


toyota = Car("Toyota", 'Corolla', 2020)
print(toyota)

toyota.start()
toyota.stop()


car2 = Car("A", "A1", 2023)
car2.start()
car2.stop()
