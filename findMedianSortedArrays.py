# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:59:35 2020

@author: asaga
"""

"""

4. Median of Two Sorted Arrays - Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


"""

len_x, len_y = len(nums1), len(nums2)
        
        if len_x > len_y:
            nums1, nums2 = nums2, nums1
            len_x, len_y = len_y, len_x 
        
        low, high = 0, len_x
        
        while(low <=high):
            partition_X = int((low + high) / 2)
            partition_Y = int((len_x + len_y + 1)/2)  - partition_X
            maxLeftX = max(nums1[:partition_X]) if partition_X != 0 else float("-inf")
            minRightY = min(nums2[partition_Y:]) if partition_Y != len_y else float("inf")
            maxLeftY = max(nums2[:partition_Y]) if partition_Y != 0 else float("-inf")
            minRightX = min(nums1[partition_X:]) if partition_X != len_x else float("inf")
            if maxLeftX <= minRightY and maxLeftY <= minRightX :
                if (len_x + len_y)%2==0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partition_X - 1
            else:
                low = partition_X + 1
"""

import time

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        len_x, len_y = len(nums1), len(nums2)
        
        if len_x > len_y:
            nums1, nums2 = nums2, nums1
            len_x, len_y = len_y, len_x 
        
        low, high = 0, len_x
        
        while(low <=high):
            partition_X = int((low + high) / 2)
            partition_Y = int((len_x + len_y + 1)/2)  - partition_X
            maxLeftX = nums1[partition_X-1] if partition_X != 0 else float("-inf")
            minRightY = nums2[partition_Y] if partition_Y != len_y else float("inf")
            maxLeftY = nums2[partition_Y-1] if partition_Y != 0 else float("-inf")
            minRightX = nums1[partition_X] if partition_X != len_x else float("inf")
            if maxLeftX <= minRightY and maxLeftY <= minRightX :
                if (len_x + len_y)%2==0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partition_X - 1
            else:
                low = partition_X + 1
        


start = time.time()
X = Solution().findMedianSortedArrays([1, 3, 8, 9, 15],[7, 11, 18, 19, 21, 25])
print(X)
print( 'Time Taken: {}'.format(time.time()- start))