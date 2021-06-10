# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:19:20 2020

@author: asaga
"""
"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""



import time

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:     
        
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
        
        """
        A = len(haystack)
        B = len(needle)
        
        if B == 0:
            return -1
        
        for i in range(0, A-B+1):
            if haystack[i:i+B] == needle:
                return i
        return 0
            
        

start = time.time()
X = Solution().strStr(haystack = "hello", needle = "ll")
print(X)
print( 'Time Taken: {}'.format(time.time()- start))