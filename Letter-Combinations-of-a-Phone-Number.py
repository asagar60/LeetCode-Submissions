# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:10:41 2020

@author: asaga
"""
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

import time

class Solution:
    def letterCombinations(self, digits):
        
        def find_all_combination(num_dict, s, ans, word, index):
            
            if index == len(s):
                ans.append("".join(word))
                return 
            
            for i in range(0, len(num_dict[s[index]])):
                word.append(num_dict[s[index]][i])
                find_all_combination(num_dict, s, ans, word, index+1)
                word.pop()
        
        
        ans = []
        if len(digits) == 0:
            return ans
    
        num_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        find_all_combination(num_dict, digits, ans, [], 0)
        
        return ans
        
        


start = time.time()
X = Solution().letterCombinations("234")
print(X)
print( 'Time Taken: {}'.format(time.time()- start))