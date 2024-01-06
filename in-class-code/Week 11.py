class Full(Exception):
    pass


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class SepChainHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def add(self, key, val):
        index = self.hash(key)
        head = self.table[index]

        while head:
            if head.data[0] == key:
                head.data = (key, val)
                return
            head = head.next

        self.table[index] = Node(data=(key, val), next=self.table[index])

    def __getitem__(self, key):
        index = self.hash(key)
        node = self.table[index]

        while node:
            if node.data[0] == key:
                return node
            node = node.next

        raise KeyError(f'{key} not found.')

    def delete(self, key):
        index = self.hash(key)
        node = self.table[index]
        prev = None

        while node:
            if node.data[0] == key:
                if not prev:
                    self.table[index] = None
                else:
                    prev.next = node.next
                return

            prev = node
            node = node.next

        raise KeyError(f'{key} not found.')

    def __repr__(self):
        res = 'Separate Chaining Hash:\n'

        for i in range(self.size):
            node = self.table[i]
            res += f'{i}: '
            while node:
                res += str(node) + ' ~ '
                node = node.next
            res += '\n'

        return res


class LinProbHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def add(self, key, val):
        index = self.hash(key)
        k = index

        while self.table[index]:
            index = self.hash(index+1)
            if index+1 == k:
                raise Full('Hash is full.')

        self.table[index] = (key, val)

    def __getitem__(self, key):
        index = self.hash(key)

        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index]
            index = self.hash(index + 1)

        raise KeyError(f'{key} not found.')

    def delete(self, key):
        index = self.hash(key)

        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] = None
                next_index = self.hash(index + 1)

                # while self.table[next_index]:
                #     if self.hash(self.table[next_index][0]) != next_index:
                #         self.table[index] = self.table[next_index]
                #         index = next_index
                #         next_index = self.hash(next_index + 1)
                #     else:
                #         self.table[index] = None
                #         break

                while self.table[next_index]:
                    k, v = self.table[next_index]
                    self.table[next_index] = None
                    self.add(k, v)
                    next_index = (next_index + 1) % self.size

                return

            index = self.hash(index + 1)

        raise KeyError(f'{key} not found.')

    def __repr__(self):
        str_data = [str(item) for item in self.table]
        return ', '.join(str_data)


table = LinProbHash(8)

for key, val in [(6, 's'), (3, 'd'), (11, 'a'), (19, 'p'), (8, 'd'), (14, 'q'), (21, 'j')]:
    table.add(key, val)
print(table)

print(table[11])

table.delete(11)
print(table)

table.delete(3)
print(table)

for key, val in [(16, 'l'), (0, 'o'), (9, 'a')]:
    table.add(key, val)
print(table)

table.delete(8)
print(table)



