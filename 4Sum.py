# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:39:39 2020

@author: asaga
"""

"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

import time

class Solution:
    def fourSum(self, nums, target):
        
        len_nums = len(nums)
        nums.sort()
        pairs=  []
        
        print(nums)
        
        prev_i = None
        for i in range(len_nums):
            if nums[i] == prev_i:
                continue
            prev_i = nums[i]
            prev_j = None
            for j in range(i+1, len_nums):
                if nums[j] == prev_j:
                    continue
                prev_j = nums[j]
                l = j+1
                r = len_nums -1
                while(l<r):
                    target_sum = nums[i]+ nums[j] + nums[l]+ nums[r]
                    if target_sum > target:
                        r = r-1
                    elif target_sum < target:
                        l = l+1
                    else:
                        pairs.append([nums[i], nums[j], nums[l], nums[r]])
                        prev_l = nums[l]
                        prev_r = nums[r]
                        while l < len_nums and nums[l]==prev_l  :
                            l = l+1
                        while  r > l and nums[r]==prev_r :
                            r = r-1                  
        return pairs
    

start = time.time()
X = Solution().fourSum(
[-3,-2,-1,0,0,1,2,3],
0)
print(X)
print( 'Time Taken: {}'.format(time.time()- start))

