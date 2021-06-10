# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 06:30:59 2020

@author: asaga
"""
import time

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        dict_nums = dict()
        for i in nums:
            dict_nums[i] = dict_nums.get(i,0) + 1
        print(dict_nums.keys())
        """
        
        if len(nums) == 0:
            return []
        not_in_list = list(set(range(1, len(nums)+1)) - set(nums))
        return not_in_list
        

start = time.time()
X = Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(X)
print( 'Time Taken: {}'.format(time.time()- start))

