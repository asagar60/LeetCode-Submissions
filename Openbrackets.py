# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:26:01 2020

@author: asaga
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

import time

class Solution:
    def isValid(self, s):
        p_dict = {"]":"[",")":"(","}":"{"}
        p_stack = []
        
        for _s in s:

            if _s not in p_dict.keys():
                p_stack.append(_s)
            
            elif len(p_stack)==0 or p_stack.pop()!=p_dict[_s]:
                return False
            
        return len(p_stack)==0
        
        

start = time.time()
X = Solution().isValid("{[]}")
print(X)
print( 'Time Taken: {}'.format(time.time()- start))