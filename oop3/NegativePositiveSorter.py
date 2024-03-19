class NegativePositiveSorter:
    def __init__(self, array):
        self.array = array

    def sort_negative_positive(self):
        negatives = [num for num in self.array if num < 0]
        positives = [num for num in self.array if num >= 0]
        return negatives + positives


if __name__ == "__main__":
    array = [3, -5, 2, 7, -8, 10]
    sorter = NegativePositiveSorter(array)
    print("Sorted negative-positive:", sorter.sort_negative_positive())
