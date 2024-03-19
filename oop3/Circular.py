class CircularCounter:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def count_elements_equal_to_k(self):
        remaining = self.n % self.k
        if remaining == 0:
            return self.k
        else:
            return remaining


if __name__ == "__main__":
    N = 4
    K = 3
    counter = CircularCounter(N, K)
    remaining_k = counter.count_elements_equal_to_k()
    print(f"For N={N} and K={K}, the {remaining_k}-th person remains.")
