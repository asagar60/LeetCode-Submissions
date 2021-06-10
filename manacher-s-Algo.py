# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:35:00 2020

@author: asaga
"""

import time

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_updated = []
        s_updated.append('$')
        s_updated.append('#')
        for char in s:    #O(n)
            s_updated.append(char)
            s_updated.append('#')
        s_updated.append('@')
        print(s_updated)
        
        P = [0 for _ in s_updated]
        C ,R = 0,0
        for i in range(1,len(P)-1):
            mirr = 2*C - i
            
            if (i < R):
                P[i] = min(R- i , P[mirr])
            
            while (s_updated[i + (1 + P[i])] == s_updated[i - (1 + P[i])]):
                P[i] += 1
            
            if (i + P[i] > R):
                C = i
                R = i + P[i]
        
        max_P = max(P)
        maxP_Index = P.index(max_P)
        palindrome = s_updated[maxP_Index - (max_P) : maxP_Index + (max_P)]
        palindrome = "".join(palindrome).replace('#',"")
        return palindrome
        
start = time.time()
X = Solution().longestPalindrome("abababa")
print(X)
print( 'Time Taken: {}'.format(time.time()- start))