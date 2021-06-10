# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:02:24 2020

@author: asaga
"""

import time

class Solution:
    def reverse(self, x: int) -> int:
        sum_ = 0
        neg=True if x <0 else False
        x = abs(x)
        while(x>0):
            sum_ = sum_*10 + x%10
            x = x//10
        if neg:
            sum_*= -1
            
        if(abs(sum_) > (2 ** 31 - 1)):
            return 0
        return sum_
        

s = Solution()

start = time.time()
print(s.reverse(120))
print(time.time()-start)
