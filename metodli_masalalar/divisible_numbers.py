class DivisibleNumbers:
    def __init__(self, k):
        self.k = k

    def find_first_divisible(self, n):
        for i in range(1, n + 1):
            if i % self.k == 0:
                return i


if __name__ == "__main__":
    k_value = 3
    n_value = 20
    div_obj = DivisibleNumbers(k_value)
    print(f"Berilgan {k_value} soniga qoldiqsiz bo'linadigan birinchi {n_value} ta son: {div_obj.find_first_divisible(n_value)}")
