# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:45:46 2020

@author: asaga
"""

"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

"""


import time


"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        sign , result = 1,0
        if divisor * dividend < 0:
            sign = -1
        if abs(dividend) >= abs(divisor):
            result = sign * (1 + self.divide(abs(dividend) - abs(divisor), abs(divisor)))
        
        if result > 0:
            return min((2 << 31)-1, result )
        
        return max(-2 << 32, result)
"""

"""
using bit operations

3 * 1 = 3^0
3*2 = 3 ^ 1
3*2^2 = 3 ^ 4
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            
        #base case
        if dividend <= -1 << 31 :
            if divisor == 1:
                return (-1<<31)
            elif divisor == -1:
                return (1<<31)-1
        
        if (dividend >=0 ) ==  (divisor >=0):
            factor = 1
        else:
            factor = -1
            
        result = 0
        
        dividend, divisor = abs(dividend),abs(divisor)
        
        while (dividend - divisor >= 0):
            x = 0
            while (dividend - (divisor << 1 << x)) >=0:
                x+=1
            
            result += 1 << x
            dividend = dividend - (divisor << x)
        
        return factor * result
        
        
    
start = time.time()
X = Solution().divide(-2147483648,2)
print(X)
print( 'Time Taken: {}'.format(time.time()- start))