class FirstKMultiple:
    @staticmethod
    def find_first_k_multiple(k, n):
        for i in range(1, n + 1):
            if i % k == 0:
                return i


if __name__ == "__main__":
    k_value = 15
    n_value = 20
    print(f"Berilgan {k_value} soniga karrali bo’lgan birinchi {n_value} ta son: "
          f"{FirstKMultiple.find_first_k_multiple(k_value, n_value)}")
