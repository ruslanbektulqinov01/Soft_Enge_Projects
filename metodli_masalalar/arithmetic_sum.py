class ArithmeticSum:
    def __init__(self, n):
        self.n = n

    def calculate_sum(self):
        return self.n * (self.n + 1) // 2

    def calculate_product(self):
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        return result


if __name__ == "__main__":
    n_value = 5
    arithmetic_obj = ArithmeticSum(n_value)
    print("1+2+3+...+n yig’indi:", arithmetic_obj.calculate_sum())
    print("1*2*3*...+n ko'paytma", arithmetic_obj.calculate_product())
