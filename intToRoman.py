# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:01:15 2020

@author: asaga
"""
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

import time

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1:'I',5:'V',10:'X',50:'L',100:'C', 500:'D', 1000:'M', 5000:'V^', 10000:'X^'}
        roman = []
        """
        x = int(num/1000)
        if x >0:
            roman.append(x * roman_dict[1000])
            num = num %1000
        x = int(num/100)
        if x > 0:
            if x <4:
                roman.append(x * roman_dict[100])
            elif x == 4:
                roman.extend([roman_dict[100], roman_dict[500]])
            elif x == 5:
                roman.append(roman_dict[500])
            elif x == 9:
                roman.extend([roman_dict[100], roman_dict[1000]])
            else:
                roman.extend([roman_dict[500], roman_dict[100]* (x-5)])
                
            num = num%100
        x = int(num/10)
            
        if x > 0:
            if x <4:
                roman.append(x * roman_dict[10])
            elif x == 4:
                roman.extend([roman_dict[10], roman_dict[50]])
            elif x == 5:
                roman.append(roman_dict[50])
            elif x == 9:
                roman.extend([roman_dict[10], roman_dict[100]])
            else:
                roman.extend([roman_dict[50], roman_dict[10]* (x-5)])
                
            num = num % 10
        x = num   
        if x > 0:
            if x <4:
                roman.append(x * roman_dict[1])
            elif x == 4:
                roman.extend([roman_dict[1], roman_dict[5]])
            elif x == 5:
                roman.append(roman_dict[5])
            elif x == 9:
                roman.extend([roman_dict[1], roman_dict[10]])
            else:
                roman.extend([roman_dict[5], roman_dict[1]* (x-5)])
        return "".join(roman)  
    
    
        for k in [1000,100,10,1]:
            x = int(num/k)
            if x > 0:
                if x <4:
                    roman.append(x * roman_dict[k])
                elif x == 4:
                    roman.extend([roman_dict[k], roman_dict[k*5]])
                elif x == 5:
                    roman.append(roman_dict[k*5])
                elif x == 9:
                    roman.extend([roman_dict[k], roman_dict[k*10]])
                else:
                    roman.extend([roman_dict[k*5], roman_dict[k]* (x-5)])
                num = num %k
        return "".join(roman)
    """
        k = 1000
        while(k >=1):
            x = int(num/k)
            if x > 0:
                if x <4:
                    roman.append(x * roman_dict[k])
                elif x == 4:
                    roman.extend([roman_dict[k], roman_dict[k*5]])
                elif x == 5:
                    roman.append(roman_dict[k*5])
                elif x == 9:
                    roman.extend([roman_dict[k], roman_dict[k*10]])
                else:
                    roman.extend([roman_dict[k*5], roman_dict[k]* (x-5)])
                num = num %k
            k = k/10
        return "".join(roman)
    
    
    
start = time.time()
X = Solution().intToRoman(1994)
print(X)
print( 'Time Taken: {}'.format(time.time()- start))