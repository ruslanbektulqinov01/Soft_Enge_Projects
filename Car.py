class Car:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.model}, {self.color}, {self.year}, {self.price}"


car1 = Car("Ford", "white", 2019, 200000)

print(car1)
