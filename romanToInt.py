# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:43:03 2020

@author: asaga
"""

import time

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1,'V': 5,'X': 10,'L':50,'C':100, 'D':500, 'M':1000, 'V^':5000, 'X^':10000}
        """
        integer=[]
        
        for r in s:
            integer.append(roman_dict[r])
        
        num = integer[0]
        for i in range(1, len(integer)):
            if integer[i-1] >= integer[i]:
                num += integer[i]
            else:
                num = num + integer[i] - 2*integer[i-1]
        """
        
        number, prev, curr = 0,0,0
        for n in s:
            curr = roman_dict[n]
            number += curr
            
            if prev > 0 and prev < curr:
                number = number - 2 * prev
            prev = curr
        
        return number
        

start = time.time()
X = Solution().romanToInt('LVIII')
print(X)
print( 'Time Taken: {}'.format(time.time()- start))