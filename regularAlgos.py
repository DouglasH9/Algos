from collections import Counter;
from math import e, log
# from typing import ValuesView;

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord("0") if p1 >= 0 else 0 
            x2 = ord(num2[p2]) - ord("0") if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1
            
        if carry:
            res.append(carry)
            
        return "".join(str(x) for x in res[::-1])

# print(addStrings("11", "123"))

# =========================================First Unique Character in a string===================================

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1

# print(firstUniqChar("ddouglasherman"))

# =========================================Merge 2 sorted arrays============================================
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # make copy of the first m elements of nums1
        nums1_copy = nums1[:m]
        
        # pointers for nums1_copy and nums2
        p1 = 0
        p2 = 0
        
        # compare elements nums1_copy and nums2 and write the smallest to nums1
        for p in range(n+m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
        # make sure p1 and p2 aren't over the boundaries of their arrays
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

# Alternate solution that uses less memory by starting from the end and doesn't create copy of nums1

def merge_two_sorted_alt(nums1, m, nums2, n):

    # set p1 and p2 to point to the ends of their arrays
    p1 = m - 1
    p2 = n - 1
    
    # move p backwards through the array, each time writing the smallest value pointed at by p1 or p2
    # this solution is better
    for p in range(n + m -1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

# ================================================Finding the Sqrt of a number===============================================
"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

"""

# Pocket calculator algorithm

def mySqrt1(x):
    if x < 2:
        return x
    
    left = int(e**(0.5 * log(x)))
    right = left +1
    return left if right * right > x else right

# print(mySqrt1(4))

# Binary search approach

def mySqrt2(x):
    if x < 2: 
        return x
    
    left, right = 2, x//2

    while left <= right:
        pivot = left + (right - left) // 2
        num = pivot * pivot
        if num > x:
            right = pivot - 1
        elif num < x:
            left = pivot + 1
        else:
            return pivot
    return right

# print(mySqrt1(102))

# Newton's approach

def mySqrt2(x):
    if x < 2:
        return x
    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + x / x0) / 2
    return int(x1)

# ====================================================Roman Numeral to Integer===================================================
"""
Given a roman numeral, convert it to an integer
"""
# starting at beginning and looping to end approach...

# create map of roman numerals and their values 
romans = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

def romanToInt(romanNum):
    total = 0
    i = 0
    while i < len(romanNum):
        # subtraction case where a lower value appears before a higher value...
        if i + 1 < len(romanNum) and romans[romanNum[i]] < romans[romanNum[i + 1]]:
            total += romans[romanNum[i+1]] - romans[romanNum[i]]
            # increase i by 2 to skip over both evaluated nums
            i += 2
        else:
            total += romans[romanNum[i]]
            i += 1
    return total

# print(romanToInt("MCDXXIII"))

# back to front approach (slightly more efficient, looks better in interviews)...

def romanToInt2(romanNum):
    total = romans.get(romanNum[-1])
    for i in reversed(range(len(romanNum) - 1)):
        if romans[romanNum[i]] < romans[romanNum[i + 1]]:
            total -= romans[romanNum[i]]
        else: 
            total += romans[romanNum[i]]
    return total

# print (romanToInt2("MCDXXIII"))

# ===================================================Remove Duplicates from an array==========================================

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums):
    if (len(nums) == 0):
        return 0
    i = 0
    while (i < len(nums)-1):
        if (nums[i] == nums[i+1]):
            del nums[i]
        else:
            i += 1
    print(nums)
    return nums
        

# removeDuplicates([1,2,2,3,4,5,5,5,5,5,6,6,7])



# ================================================Binary Tree Craziness===========================================
# Define structure of BinTreeNode
class BinTreeNode(object):
    # initialize the attributes
    def __init__(self, data, song):
        self.data = data
        self.song = song
        self.left = None
        self.right = None
    # method to insert new nodes into Binary Tree
    def insertToBinTree(self, data, song):
        # if current node contains data...
        if self.data:
            # if the data for the node to be inserted is less than current node...
            if data < self.data:
                # insert node as left child if left is equal to None
                if self.left is None:
                    self.left = BinTreeNode(data, song)
                # else run insertToBinTree on next left child node
                else:
                    self.left.insertToBinTree(data, song)
            # if data of node to insert is greater than current node...
            elif data > self.data:
                if self.right is None:
                    self.right = BinTreeNode(data, song)
                else:
                    self.right.insertToBinTree(data, song)
        else:
            self.data = data

    def printBinTree(self):
        if self.left:
            self.left.printBinTree()
        print(self.data, self.song),
        if self.right:
            self.right.printBinTree()

# Create Instance of Node, and call it root to start tree
root = BinTreeNode(1, "PDA")
root.insertToBinTree(2, "The Weekenders")
root.insertToBinTree(3, "Sedona")
root.insertToBinTree(10, "Ju$t")
root.insertToBinTree(12, "Shadow")
root.insertToBinTree(8, "NightCall")
root.printBinTree()






