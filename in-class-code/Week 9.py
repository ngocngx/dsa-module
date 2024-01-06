class Empty(Exception):
    pass

class Queue:
    """FIFO Queue implementation using a Python list as underlying storage."""

    def __init__(self):
        """ Create an empty queue """
        self._data = []
        self._size = 0

    def __repr__(self):
        """ Return string representation of the queue """
        return str(self._data)

    def __len__(self):
        """ Return the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty """
        return self._size == 0

    def enqueue(self, value):
        """ Add an element to the back of queue """
        self._data.append(value)
        self._size += 1

    def dequeue(self):
        """ Remove and return the first element of the queue.
        Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty('Queue is empty')
        self._size -= 1
        return self._data.pop(0)

    def first(self):
        """ Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def add_left(self, parent: Node, child: Node):
        parent.left = child

    def add_right(self, parent: Node, child: Node):
        parent.right = child

    def breadfirst(self):
        queue = Queue()
        queue.enqueue(self.root)

        while queue:
            p = queue.dequeue()
            print(p, end=' ')
            if p.left:
                queue.enqueue(p.left)
            if p.right:
                queue.enqueue(p.right)

    def in_order(self, root, queue: Queue):
        if not root:
            return
        self.in_order(root.left, queue)
        queue.enqueue(root.value)
        self.in_order(root.right, queue)

    def calculate(self):
        queue = Queue()
        self.in_order(self.root, queue)
        return queue

    def func(self):
        return self._func(self.root)

    def _func(self, root):
        if not root:
            return

        # if root.value == '+':
        #     return self._func(root.left) + self._func(root.right)
        # elif root.value == '-':
        #     return self._func(root.left) - self._func(root.right)
        # elif root.value == '*':
        #     return self._func(root.left) * self._func(root.right)
        # elif root.value == '/':
        #     return self._func(root.left) / self._func(root.right)
        # else:
        #     return root.value

        # if type(root.value) is int:
        #     return root.value
        try:
            return eval(str(self._func(root.left)) + root.value + str(self._func(root.right)))
        except:
            return root.value


a = Node('+')
b = Node('*')
c = Node(6)
d = Node(3)
e = Node('-')
h = Node(7)
k = Node(4)

binary_tree = BinaryTree(a)
binary_tree.add_left(a, b)
binary_tree.add_right(a, c)
binary_tree.add_left(b, d)
binary_tree.add_right(b, e)
binary_tree.add_left(e, h)
binary_tree.add_right(e, k)

# func = binary_tree.calculate()
# math = ''
# while func:
#     char = func.dequeue()
#     math += char
#
# print(math)
print(binary_tree.func())