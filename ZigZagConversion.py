# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:55:29 2020

@author: asaga
"""
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I      N
A   L S   I G
Y A   H R
P     I

"""
import time

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string = []
        i = 0
        n = 0
        while(i<len(s)):
            
            if n > 0 and i < len(s):
                substring = ["" for _ in range(n)] + [s[i]] + ["" for _ in range(n+1, numRows)]
                string.append(substring)
                i = i+1
                n -= 1
                
            else:
                substring = ["" for _ in range(n)] + [_s for _s in s[i:min(i+n, len(s))]] + ["" for _ in range(n+1, numRows)]
                [_s for _s in s[i:min(i+numRows, len(s))]] + ["" for _ in range(numRows-len(substring))]
                """
                if len(substring) < numRows:
                    substring.extend(["" for _ in range(numRows-len(substring))])
                """
                string.append(substring)
                i = i+numRows
                n = numRows-2
        new_str = []
        for x in list(zip(*string)):
           new_str += "".join(x)
        return "".join(new_str)
    
        
        

start = time.time()
X = Solution().convert("AB",1)
print(X)
print( 'Time Taken: {}'.format(time.time()- start))
#print(len(X))