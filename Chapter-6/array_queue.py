class ArrayQueue:
    """
    First in first out queue implementation using a Python list as underlying storage.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """
        Initialize an empty queue, with 10 spaces.
        """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        """
        Return the number of elements in the queue.
        :return: int
        """
        return self._size

    def __str__(self) -> str:
        """
        Return a representation of the values in the queue.
        :return:
        """
        lst_str = []
        for val in self._data:
            if val:
                lst_str.append(val)
        return '<{}>'.format(', '.join(map(str, lst_str)))

    def is_empty(self) -> bool:
        """
        Return true if the queue is empty.
        :return: bool
        """
        return self._size == 0

    def first(self) -> object:
        """
        Return the first element of the queue, but do not remove it.
        :return: object
        """
        if self.is_empty():
            raise Exception("Empty queue.")
        return self._data[self._front]

    def dequeue(self) -> object:
        """
        Return and remove the first element of the queue.
        :return: object
        """
        if self.is_empty():
            raise Exception("Empty queue.")
        result = self._data[self._front]
        self._data[self._front] = None  # Garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result

    def enqueue(self, e: object):
        """
        Add an element to the back of the queue.
        """
        if self._size == len(self._data):  # Double the length of the queue
            self._resize(2 * len(self._data))
        available = (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1

    def _resize(self, capacity):
        """
        Resize the queue to a new capacity
        """
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def size(self) -> int:
        """
        Return the size of the queue.
        :return: int
        """
        return self._size


if __name__ == '__main__':
    queue = ArrayQueue()
    print(queue.size())  # 0
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue("Twenty-five")
    print(queue)  # <5, 10, 15, 20, Twenty-five>
    print(queue.dequeue())  # 5
    print(queue)  # <10, 15, 20, Twenty-five>
    print(queue.first())  # 10
