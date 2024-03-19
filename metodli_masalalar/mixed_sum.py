class MixedSum:
    def __init__(self, n):
        self.n = n

    def calculate_mixed_sum(self):
        result = 0
        for i in range(1, self.n + 1):
            result += i * (self.n - i + 1)
        return result


if __name__ == "__main__":
    n_value = 5
    mixed_obj = MixedSum(n_value)
    print("1·n+2·(n ‒1)+3·(n ‒2)+...+n·1 yig’ini:", mixed_obj.calculate_mixed_sum())
