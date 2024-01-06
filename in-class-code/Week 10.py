class Empty(Exception):
    pass


class Item:
    """ Item in Heap """

    def __init__(self, key, value):
        self.key = key
        self.val = value

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return str((self.key, self.val))


class MinHeap:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def _parent(self, k):
        if not(k >= 0 and type(k) == int):
            raise ValueError("k must be a positive integer")

        return (k - 1) // 2

    def _left(self, k):
        if not(k >= 0 and type(k) == int):
            raise ValueError("k must be a positive integer")

        return 2*k + 1

    def _right(self, k):
        if not(k >= 0 and type(k) == int):
            raise ValueError("k must be a positive integer")

        return 2*k + 2

    def _has_left(self, k):
        if not(k >= 0 and type(k) == int):
            raise ValueError("k must be a positive integer")

        return self._left(k) < len(self._data)

    def _has_right(self, k):
        if not(k >= 0 and type(k) == int):
            raise ValueError("k must be a positive integer")

        return self._right(k) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, k):
        parent = self._parent(k)

        if k > 0 and self._data[k] < self._data[parent]:
            self._swap(k, parent)
            self._sift_up(parent)

    def add(self, new_item: Item):
        for i in range(len(self._data)):
            if self._data[i] == new_item:
                cue = input("The key already exists. Do you want to update the value? (y/n) ")
                if cue.lower() == 'y':
                    self._data[i] = new_item
                    self._sift_up(i)
                return

        self._data.append(new_item)
        self._sift_up(len(self._data) - 1)

    def get_min(self):
        if not self.is_empty():
            return self._data[0]

    def _sift_down(self, size, k=0):
        while True:
            left = self._left(k)
            right = self._right(k)
            smallest = k

            if left < size and self._data[left] < self._data[smallest]:
                smallest = left
            if right < size and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest != k:
                self._swap(smallest, k)
                k = smallest
            else:
                break

    def remove_min(self):
        if not self.is_empty():
            min_item = self._data[0]
            self._data[0] = self._data[-1]
            del self._data[-1]
            self._sift_down(len(self), 0)
            return min_item

    def max_heap_sort(self):
        for i in range(len(self) - 1, -1, -1):
            self._swap(0, i)
            self._sift_down(i, 0)

    def __str__(self):
        str_data = [str(item) for item in self._data]
        return ', '.join(str_data)


class Median:
    def __init__(self):
        self.smaller = MinHeap()
        self.larger = MinHeap()

    def add_val(self, val):
        if len(self.smaller) == 0 or val < -self.smaller.get_min():
            self.smaller.add(-val)
        else:
            self.larger.add(val)

        if len(self.smaller) > len(self.larger) + 1:
            num = self.smaller.remove_min()
            self.larger.add(-num)
        if len(self.larger) > len(self.smaller):
            num = self.larger.remove_min()
            self.smaller.add(-num)

    def find_median(self):
        if len(self.larger) == len(self.smaller):
            return (-self.smaller.remove_min() + self.larger.remove_min()) / 2
        else:
            return -self.smaller.remove_min()


def maximize_capital(expense: list, revenue: list, name: list, initial_cap, number_of_prj):
    if not len(expense) == len(revenue) == len(name):
        raise Exception()

    projects = MinHeap()
    aux = MinHeap()
    res = []

    for i in range(len(name)):
        profit = revenue[i] - expense[i]
        prj = Item(-profit, (expense[i], name[i]))
        projects.add(prj)

    while len(res) < number_of_prj:
        item = projects.remove_min()
        p, (e, n) = -item.key, item.val
        if initial_cap >= e:
            res.append(n)
            initial_cap += p
            while aux:
                projects.add(aux.remove_min())
        else:
            aux.add(item)

    return res, initial_cap


name = ['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6', 'TC7', 'TC8', 'TC9']
expense = [2, 1, 9, 5, 4, 13, 41, 39, 15]
revenue = [5, 5, 13, 10, 10, 36, 90, 79, 37]
initial_cap = 3

print(maximize_capital(expense, revenue, name, 3, 4))
