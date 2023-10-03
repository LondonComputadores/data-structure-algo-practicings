import collections
import unittest


class Queue:

    def __init__(self):
        self._data = collections.deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        if self._data:
            return self._data.popleft()


class QueueTest(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def test_simple(self):
        self.queue.enqueue(11)
        self.queue.enqueue(22)

        self.assertEqual(11, self.queue.dequeue())
        self.assertEqual(22, self.queue.dequeue())

    def test_empty_queue(self):
        self.assertIsNone(self.queue.dequeue())


if __name__ == '__main__':
    unittest.main()