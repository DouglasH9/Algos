
from collections import defaultdict, deque
from ctypes import sizeof
import random
from re import search
from types import new_class
from typing import Optional

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

"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

def num_islands(grid: list[list[str]]) -> int:
    # if there's no grid, return 0
    if not grid:
        return 0
    # define the size of "map" as m(len of outer list) by n(len of inner lists)
    m, n = len(grid), len(grid[0])
    # directions for depth first search to look at around each grid square
    directions = [0, 1, 0, -1, 0]

    def depth_first_search(row, col):
        # if the row or column is less than zero or equal to the length or height of the "map," return zero
        if row < 0 or row == m or col < 0 or col == n or grid[row][col] == "0": return 0
        # flip visited square to zero
        grid[row][col] = "0"
        # recursive call to find all the surrounding 1's if 1 is found. Loop through the values in DIR to look at what's around the grid square and return 1 when done.
        for i in range(4):
            depth_first_search(row + directions[i], col + directions[i+1])
        return 1

    answer = 0
    # loop through all the grid squares, calling on DFS each time, and add 1 each time an island is found
    for row in range(m):
        for col in range(n):
            answer += depth_first_search(row, col)
    return answer

# print(num_islands([
#     ["1","1","0","0","1"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]))

"""
Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

def single_number(nums: list[int]) -> int:
    # set up stack to store values to check
    lonely_num_stack = [];
    # take care of base cases where nums is empty or only contains one element
    if len(nums) < 1:
        return 0
    elif len(nums) == 1:
        return nums[0]
    for num in nums:
        # iterate over nums and add num to lonely stack if not already in
        if num not in lonely_num_stack:
            lonely_num_stack.append(num)
        # remove num if already in lonely stack
        else:
            lonely_num_stack.remove(num)
    # return whatever value is left over
    return lonely_num_stack.pop()
            

# print(single_number([1,2,1,2,3,4,4]))

# much faster solution with hash table(DON'T FORGET ABOUT HASH TABLES!!!)

def single_number_two(nums: list[int]) -> int:
    # create hash table for nums. Use defaultdict because iterated lists can be added to it. Defaultdicts accept keys without values assigned, regular dicts do not.
    lonely_hash = defaultdict(int)
    # iterate over nums and add them as keys to hash table, add one to their value every time they are encountered in the list
    for num in nums:
        lonely_hash[num] += 1

    # iterate over hash table and check for key that has value of 1, and return it
    for num in lonely_hash:
        if lonely_hash[num] == 1:
            return num

# print(single_number_two([1,1,9,4,3,4,3]))

"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Recursion

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def swap_pairs_of_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    first_node = head
    second_node = head.next

    first_node.next = swap_pairs_of_nodes(second_node.next)
    second_node.next = first_node

    return second_node


head = ListNode(2, None)
head.next = ListNode(3, None)
head.next.next = ListNode(4, None)
head.next.next.next= ListNode(5, None)

print(swap_pairs_of_nodes(head))