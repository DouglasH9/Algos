from collections import deque

# Binary Searches...
# ====================================================
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid +1
    return None

# my_list = [1,3,5,7,9]

# print binary_search(my_list, 3)
# print binary_search(my_list, -1)

# =========================================Selection Sort=================================================

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# print selectionSort([5,3,6,2,10])

# =======================================Recursive Factorial=======================================

def recursive_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)

# print recursive_factorial(5)

# =====================================Recursive Sum================================================

def recursive_sum(arr):
    if arr == []:
        return "empty array"
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])

# print recursive_sum([])

# ============================Recursive Counting of an array================================

def recursive_count(arr):
    if len(arr) == 0:
        return "nothing in the array"
    elif len(arr) == 1:
        return 1
    else:
        return 1 + recursive_count(arr[1:])

# print recursive_count([3,4,5,5,4,3,3,2])

# =============================Recursive Max Number==========================================

def recursive_max_number(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = recursive_max_number(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# print recursive_max_number([4,5,8,12,23,3,5])

# ============================Recursive Binary Search=========================================

def recursive_bin_search(arr, low, high, num):
    if high >= 1:
        mid = 1 + (high+low)//2
        if arr[mid] == num:
            return mid
        elif num > high:
            return -1
        elif arr[mid] > num:
            return recursive_bin_search(arr, low, mid-1, num)
        else:
            return recursive_bin_search(arr, mid+1, high, num)
    else:
        return -1

# arr1 = [2,3,4,5,6,7,8,9,10,11,12]


# print recursive_bin_search(arr1, 0, len(arr1)-1, 13)

# =======================================Quicksort=============================================

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)

# print quicksort([3,4,6,32,1,34,100,56,20, 78])


# ==========================Valid Parens Algo=======================================================

def valid_parens(str):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for char in str:
        if char in open_par:
            stack.append(char)
        elif stack and char == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []

# print(valid_parens("()()("))

# =========================================graphs and breadth first search================================
# creates a graph of friends and breadth first searches for a specific type of friend

# creating a graph of friends
my_graph = {}
my_graph["me"] = ["jim","joe", "andy", "tony"]
my_graph["jim"] = ["joe","andy"]
my_graph["andy"] = ["jim", "joe"]
my_graph["joe"] = ["andy"]
my_graph["tony"] = ["scott", "drew"]
my_graph["scott"] = []
my_graph["drew"] = []

# silly function to define if person is one we're looking for. will make it so that it finds first person with name ending in "t"

def person_with_t(name):
    return name[-1] == "t"

# creating a breadth first search algorithm
def breadth_first_search(name):
    search_queue = deque()
    search_queue += my_graph[name]
    searched_names = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched_names:
            if person_with_t(person):
                print (f"{person} has a T at the end of their name!")
                return True
            else:
                search_queue += my_graph[person]
                searched_names.append(person)
    return False

# print(breadth_first_search("me"))

# =========================Dijkstra's Algorithm===========================================
# Takes in a weighted graph and returns the least costly path from A to B

d_graph = {}

d_graph["start"] = {}
d_graph["start"]["a"] = 6
d_graph["start"]["b"] = 2
d_graph["a"] = {}
d_graph["a"]["fin"] = 1
d_graph["b"] = {}
d_graph["b"]["a"] = 3
d_graph["b"]["fin"] = 5
d_graph["fin"] = {}

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None