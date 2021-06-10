# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:52:49 2020

@author: asaga
"""

import time

class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        print(candidates)
        def recursiveSum(_sum, _list, candidates):
            for i in range(0, len(candidates)):
                if i > 0 and candidates[i]==candidates[i-1]:
                    continue
                if _sum + candidates[i] == target:
                    result.append(_list+[candidates[i]])
                    return
                
                if _sum + candidates[i] > target:
                    return
                
                else:
                    recursiveSum(_sum + candidates[i], _list + [candidates[i]], candidates[i+1:])
        
        recursiveSum(0, [], candidates)
        return result
        

start = time.time()
X = Solution().combinationSum2([10,1,2,2,2,7,6,1,5],8)
print(X)
print( 'Time Taken: {}'.format(time.time()- start))