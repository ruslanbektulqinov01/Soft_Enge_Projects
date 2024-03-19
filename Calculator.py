class Calculator:
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation

    @property
    def operate(self):
        if self.operation == "+":
            return self.x + self.y
        elif self.operation == "-":
            return self.x - self.y
        elif self.operation == "*":
            return self.x * self.y
        else:
            if self.y != 0:
                return self.x / self.y
            else:
                return "Invalid Operation"


class SuperCalculator(Calculator):
    def __init__(self, x, y, operation):
        super().__init__(x, y, operation)

    def pow(self):
        return self.x ** self.y

    def sqrt(self):
        return self.x ** 0.5


# print(Calculator(int(input("Enter the first number: ")), int(input("Enter the first number: ")),
#                  input("Enter the operation: ")).operate)

print(SuperCalculator(int(input("Enter the first number: ")), int(input("Enter the first number: ")),
                      input("Enter the operation: ")).pow())
