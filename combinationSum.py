# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:01:06 2020

@author: asaga
"""

import time

class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        def recursiveSum(_sum, _list, candidates):
            for i in range(0, len(candidates)):
                if _sum + candidates[i] == target:
                    result.append(_list+[candidates[i]])
                    return
                
                if _sum + candidates[i] > target:
                    return
                
                else:
                    recursiveSum(_sum + candidates[i], _list + [candidates[i]], candidates[i:])
        
        recursiveSum(0, [], candidates)
        return result
        

start = time.time()
X = Solution().combinationSum([8,7,4,3],11)
print(X)
print( 'Time Taken: {}'.format(time.time()- start))