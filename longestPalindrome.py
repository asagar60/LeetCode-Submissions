# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 06:51:58 2020

@author: asaga
"""
import time

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.checkPalindrome(s,i,i)
            len2 = self.checkPalindrome(s, i,i+1)
            
            l = max(len1, len2)
            if l > end - start:
                start, end = i - int((l -1)/2), i+int(l/2)
        return s[start:end+1]
        
        
    def checkPalindrome(self, s, i, j):
        left = i
        right = j
        while left >= 0 and right < len(s) and s[left]==s[right] :
            left -= 1
            right += 1
        return right - left -1
        
start = time.time()
X = Solution().longestPalindrome("a")
print(X)
print( 'Time Taken: {}'.format(time.time()- start))