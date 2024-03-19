class SquaredSum:
    def __init__(self, n):
        self.n = n

    def calculate_squared_sum(self):
        result = 0
        for i in range(1, self.n + 1):
            result += i * i
        return result


if __name__ == "__main__":
    n_value = 5
    squared_obj = SquaredSum(n_value)
    print("1·1+2·2+3·3+...+n·n yig’indisi:", squared_obj.calculate_squared_sum())
