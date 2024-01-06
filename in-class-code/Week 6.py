class Empty(Exception):
    pass


class Queue:
    def __init__(self):
        self._data = []
        self._size = 0

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        self._data.append(value)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        self._size -= 1
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]


def get_time(line: Queue(), k: int):
    time = 0

    while line:
        current = line.dequeue() - 1
        time += 1

        if current:
            line.enqueue(current)
        else:
            if k == 0:
                break
        k = (k - 1) % len(line)
       

    return time

# tickets = Queue()
# k = 0
# for i in [3, 2, 3, 4, 1, 2]:
#     tickets.enqueue(i)
# print(tickets, get_time(tickets, k))

# tickets = Queue()
# k = 2
# for i in [2, 3, 2]:
#     tickets.enqueue(i)
# print(tickets, get_time(tickets, k))


tickets = Queue()
k = 0
for i in [5,1,1,1]:
    tickets.enqueue(i)
print(get_time(tickets, k))

tickets = Queue()
k = 2
for i in [2, 3, 2, 4]:
    tickets.enqueue(i)
print(get_time(tickets, k))