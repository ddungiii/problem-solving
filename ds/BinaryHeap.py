class BinaryHeap:
    def __init__(self):
        """
        Index of items starts with 1.
        """
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2

        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]

            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        left, right = idx * 2, idx * 2 + 1
        smallest = idx

        if left < len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right < len(self) and self.items[right] < self.items[right]:
            smallest = right

        if smallest != idx:
            self.items[smallest], self.items[idx] = (
                self.items[idx],
                self.items[smallest],
            )

            self._percolate_down(smallest)

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted


def test_binaryHeap():
    binary_heap = BinaryHeap()
    assert len(binary_heap) == 0

    binary_heap.insert(3)
    binary_heap.insert(2)
    binary_heap.insert(1)
    assert len(binary_heap) == 3

    assert binary_heap.extract() == 1
    assert len(binary_heap) == 2
    assert binary_heap.extract() == 2
    assert len(binary_heap) == 1
    assert binary_heap.extract() == 3
    assert len(binary_heap) == 0
