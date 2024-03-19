class ArrayOperations:
    def __init__(self, n):
        self.n = n

    def reverse_array(self):
        array = [i for i in range(1, self.n + 1)]
        reversed_array = array[::-1]
        return reversed_array


if __name__ == "__main__":
    n = 10
    reverse = ArrayOperations(n)
    reversed_array = reverse.reverse_array()
    print("Reversed array:", reversed_array)
