class ArrayOperations:
    def __init__(self, array):
        self.array = array

    def sum_elements(self):
        return sum(self.array)

    def product_elements(self):
        result = 1
        for num in self.array:
            result *= num
        return result

    def max_element(self):
        return max(self.array)

    def min_element(self):
        return min(self.array)

    def move_negatives_first(self):
        negatives = [num for num in self.array if num < 0]
        positives = [num for num in self.array if num >= 0]
        return negatives + positives

    @staticmethod
    def execute_operations(array):
        array_ops = ArrayOperations(array)
        print("Sum of elements:", array_ops.sum_elements())
        print("Product of elements:", array_ops.product_elements())
        print("Max element:", array_ops.max_element())
        print("Min element:", array_ops.min_element())
        print("Negatives first:", array_ops.move_negatives_first())


if __name__ == "__main__":
    array = [3, -5, 2, 7, -8, 10]
    ArrayOperations.execute_operations(array)
