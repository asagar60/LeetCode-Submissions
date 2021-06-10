# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:57:08 2020

@author: asaga
"""

"""
Longest Substring Without Repeating Characters
"""

import time

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        
        """
        best_len = 0
        substring = []
        for sub in s:
            if sub not in substring:
                substring.append(sub)

            else:
                idx = substring.index(sub)
                substring = substring[idx+1:]
                substring.append(sub)
                
            
            if len(substring) > best_len:
                best_len = len(substring)
        return best_len
        
        """
        
        dicts = {}
        best_len = 0
        start = 0
        
        for i , value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start =  sums
            nums = i - start + 1 
            if nums > best_len:
                best_len = nums
            dicts[value] = i
        return best_len



start = time.time()
X = Solution().lengthOfLongestSubstring("pwwkew")
print(X)
print( 'Time Taken: {}'.format(time.time()- start))
