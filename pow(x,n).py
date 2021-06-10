# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 08:53:45 2020

@author: asaga
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n==0:
            return 1
        if n ==1:
            return x
        if n==2:
            return x*x
        
        if n<0:
            x = 1/x
        
        if abs(n)%2==0:
            result = result * self.myPow(x, abs(n//2))**2
        else:
            result = result * self.myPow(x, abs(n//2)) * self.myPow(x, abs(n//2 +1))

        
        return result
    
s = Solution()
print(s.myPow(2.00,-2147483648))
print(s.myPow(0.00001,2147483647))
print(s.myPow(2, -2))
