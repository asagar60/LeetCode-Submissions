# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:33:00 2020

@author: asaga
"""
import time

class Solution:
    
    """
    #O(n^2)
    def maxArea(self, height) -> int:
        area = []
        
        for i in range(len(height)):
            max_area = 0
            for j in range(i+1, len(height)):
                a = min(height[i], height[j]) * (j - i)
                if  a > max_area:
                    max_area = a
            area.append(max_area)
        return max(area)
     """

    #O(n)       
    def maxArea(self, height) -> int:
        max_area = 0
        i = 0
        j = len(height)-1
         
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area =  area
            
            if height[i] > height[j]:
                j -= 1
            else:
                i+=1
        return max_area
    
start = time.time()
X = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(X)
print( 'Time Taken: {}'.format(time.time()- start))