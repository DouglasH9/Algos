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
        elif arr[mid] > num:
            return recursive_bin_search(arr, low, mid-1, num)
        else: 
            return recursive_bin_search(arr, mid+1, high, num)
    else:
        return -1

arr1 = [2,3,4,5,6,7,8,9,10,11,12]


print recursive_bin_search(arr1, 0, len(arr1)-1, 1)
