# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:24:15 2020

@author: asaga
"""

import time
import datetime

"""
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
  
"""

def validMountainArray(A):
    
    N = len(A)
    i =0
    while i+1 < N and  A[i]<A[i+1]:
        i += 1
    
    if i==0 or i == N-1:
        return False
    
    while i+1 < N and A[i] > A[i+1]:
        i+=1
    
    return i == N-1
        
        


start = datetime.datetime.now()
arr = [2,1] #false
print('Output {}'.format(validMountainArray(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))

print()
start = datetime.datetime.now()
arr = [3,5,5] #false
print('Output {}'.format(validMountainArray(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))

print()
start = datetime.datetime.now()
arr = [0,3,2,1] #true
print('Output {}'.format(validMountainArray(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))


print()
start = datetime.datetime.now()
arr = [0,1,2,3,4,5,6,7,8,9]#false
print('Output {}'.format(validMountainArray(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))


[9,8,7,6,5,4,3,2,1,0]

print()
start = datetime.datetime.now()
arr = [9,8,7,6,5,4,3,2,1,0]#false
print('Output {}'.format(validMountainArray(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))