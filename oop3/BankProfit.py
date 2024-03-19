class BankProfitCalculator:
    def __init__(self, a_array, b_array):
        self.a_array = a_array
        self.b_array = b_array

    def calculate_bank_profit(self):
        total_profit = sum(a * b / 100 for a, b in zip(self.a_array, self.b_array))
        return total_profit


if __name__ == "__main__":
    a_array = [1000, 2000, 1500]
    b_array = [5, 3, 4]
    calculator = BankProfitCalculator(a_array, b_array)
    total_profit = calculator.calculate_bank_profit()
    print("Bank's total profit in a year:", total_profit)
