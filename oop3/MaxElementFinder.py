class MaxElementFinder:
    def __init__(self, array):
        self.array = array

    def find_max_element_index(self):
        max_index = self.array.index(max(self.array)) + 1
        return max_index

    @staticmethod
    def find_max_element_index_print(array):
        max_finder = MaxElementFinder(array)
        print("Max element index:", max_finder.find_max_element_index())


if __name__ == "__main__":
    array = [3, -5, 2, 7, -8, 10]
    MaxElementFinder.find_max_element_index_print(array)

