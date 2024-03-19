class MoveKElementsForward:
    def __init__(self, array, k):
        self.array = array
        self.k = k

    def move_k_elements_forward(self):
        k_elements = self.array[-self.k:]
        remaining_elements = self.array[:-self.k]
        return k_elements + remaining_elements


if __name__ == "__main__":
    array = [3, -5, 2, 7, -8, 10, 20, 30]
    k = 3
    mover = MoveKElementsForward(array, k)
    print(f"Move {k} elements forward:", mover.move_k_elements_forward())
