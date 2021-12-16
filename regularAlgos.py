from collections import Counter;

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

print(addStrings("11", "123"))

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