#Using list as a quesue
stock_price_queue = []
stock_price_queue.insert(0, 131)
stock_price_queue.insert(0,132)
stock_price_queue.insert(0, 133)

stock_price_queue.pop()

#Using collections.deque as a queue
from collections import deque
q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(10)
q

q.pop()

from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
