# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 00:44:40 2020

@author: asaga
"""

"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

import time

class Solution:
    
    """
    #works if sorted
    def twoSum(self, nums, target):
        
        i,j,_sum=0,len(nums)-1,0
        while(i<j):
            _sum = nums[i] + nums[j]
            if _sum == target:
                return [nums[i], nums[j]]
            elif _sum > target:
                j = j - 1
            else:
                i = i+1

    """
        
    def twoSum(self, nums, target):
        
        prevMap = {}
        
        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return
        
start = time.time()
X = Solution().twoSum([2,3,3,4],6)
print(X)
print( 'Time Taken: {}'.format(time.time()- start))