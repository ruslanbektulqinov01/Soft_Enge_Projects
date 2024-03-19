class MoveKElementsBackward:
    def __init__(self, array, k):
        self.array = array
        self.k = k

    def move_k_elements_backward(self):
        k_elements = self.array[:self.k]
        remaining_elements = self.array[self.k:]
        return remaining_elements + k_elements


if __name__ == "__main__":
    array = [3, -5, 2, 7, -8, 10]
    k = 2
    mover = MoveKElementsBackward(array, k)
    print(f"Move {k} elements backward:", mover.move_k_elements_backward())
