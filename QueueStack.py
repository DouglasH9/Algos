
from collections import deque
from ctypes import sizeof
import random
from types import new_class

"""
Queue and Stack algos with Python



Sliding window average algorithm. Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
"""

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

# cool_slide = SlidingWindowDoubleEndedQueue(5)
# print(cool_slide.next(2))
# print(cool_slide.next(3))
# print(cool_slide.next(8))
# print(cool_slide.next(9))
# print(cool_slide.next(10))
# print(cool_slide.next(3))

"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Rooms is 2d array input
"""

def walls_and_gates(rooms: list[list[int]]) -> list[list[int]]:
    # return if there's no rooms to search
    if not rooms:
        return
    # define the rows and columns
    row, column = len(rooms), len(rooms[0])
    # iterate over all the rooms
    for i in range(row):
        for j in range(column):
            # if the room is 0 (a gate) add it to the queue
            if rooms[i][j] == 0:
                queue = deque([])
                # look at all the adjacent rooms and append it's coordinate and distance from gate as a tuple
                queue.append((i+1, j, 1)); queue.append((i-1, j, 1))
                queue.append((i, j+1, 1)); queue.append((i, j-1, 1))
                # create set to store visited rooms
                visited = set()
                # while there's things in the queue...
                while queue:
                    # pop off the left value of queue and store values from tuple in x, y, val
                    x, y, val = queue.popleft()
                    
                    if x < 0 or x >= row or y < 0 or y >= column or rooms[x][y] in [0,-1] or (x,y) in visited:
                        continue
                    visited.add((x,y))
                    rooms[x][y] = min(rooms[x][y], val)
                    queue.append((x+1, y, val+1)); queue.append((x-1, y, val+1))
                    queue.append((x, y+1, val+1)); queue.append((x, y-1, val+1))
    return rooms

# print(walls_and_gates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))


