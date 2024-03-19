class FibonacciSum:
    @staticmethod
    def calculate_fibonacci_sum(n):
        a, b = 0, 1
        total = 0
        for _ in range(n):
            total += a
            a, b = b, a + b
        return total


if __name__ == "__main__":
    fibonacci_value = 10
    print("Fibonachchi sonlari birinchi", fibonacci_value, "tasining yig’ini:", FibonacciSum.calculate_fibonacci_sum(fibonacci_value))
