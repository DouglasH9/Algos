from collections import deque
from ctypes import sizeof
from types import new_class

"""
Queue and Stack algos with Python
"""

#Sliding window average algorithm. Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Time complexity O(N)
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)

# Time complexity O(1) using a double ended queue a "deque"
class SlidingWindowDoubleEndedQueue:
    def __init__(self, size: int) -> None:
        # sets size of sliding window
        self.size = size
        # initializes the double ended queue used for the sliding window
        self.queue = deque()
        # sum of elements in the sliding window
        self.window_sum = 0
        # counts the number of things seen by the window
        self.count = 0

    def next(self, val: int) -> float:
        # calculate the new sum by shifting the window. 
        self.count += 1
        # append new value to right side of queue
        self.queue.append(val)
        # pop the value of the left side of the queue if the number of things in the queue is bigger than its size else, set it to zero so it won't effect the sum when added
        tail = self.queue.popleft() if self.count > self.size else 0

        # subtract the value of the recently popped tail from the window sum and add the new value
        self.window_sum = self.window_sum - tail + val

        # return the new window_sum divided by either the size of the window (if window is full) or the count (if window isn't full), whichever is smaller
        return self.window_sum / min(self.size, self.count)

cool_slide = SlidingWindowDoubleEndedQueue(5)
 

