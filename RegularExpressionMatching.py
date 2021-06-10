# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:25:00 2020

@author: asaga
"""
"""

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""

import time

class Solution:
    
    """
    def isMatch(self, s: str, p: str) -> bool:
        
        i,j =0,0
        len_track = j
        
        while(i< len(s)):
            if p[j] is None:
                return False
            
            if p[j] == '.':
                prev = "#"
                j = j+1
                i = i+1
                len_track = j
            
            elif p[j] == '*':
                
                if s[i] == prev or prev == '#':
                    print(s[i], p[j], prev, i,j)
                    i = i+1
                elif i > j and s[i]==p[j+1] or p[j] == '.':
                    print(s[i], p[j+1], i,j)
                    i = i+1
                    j = j+2
            elif p[j] == s[i]:
                 print(s[i], p[j], i,j)
                 prev = p[j]
                 i = i+1
                 j = j+1
                 len_track = j
                 
            else:
                return False
        
        return True
            
    """
    
    def isMatch(self, s: str, p: str) -> bool:
        
        i,j =0,0
        prev = None
        
        while (i < len(s)):
            
            if prev==None and p[j]=='*':
                return False
            
            if s[i] == p[j]:
                print(s[i], p[j], prev, i,j)
                i+=1
                j+=1
                prev = s[i]
                
            elif p[j] == '*':
                if prev == s[i] or prev == '#':
                    print(s[i], p[j], prev, i,j)
                    i = i+1
                else:
                    print(s[i], p[j], prev, i,j)
                    j = j+1
            elif p[j] == '.':
                print(s[i], p[j], prev, i,j)
                prev = "#"
                i = i+1
                j = j+1
                continue
            else:
                return False
        return True
                

start = time.time()
X = Solution().isMatch("aab","c*a*b")
print(X)
print( 'Time Taken: {}'.format(time.time()- start))