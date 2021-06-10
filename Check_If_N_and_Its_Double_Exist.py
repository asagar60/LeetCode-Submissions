# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:19:45 2020

@author: asaga
"""

import time
import datetime

"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
"""
        
#approach 1
"""
def checkIfExist(arr):
    found = False
    
    i = 0
    j = i+1
    while(True):
        if i == len(arr):
            found = False
            break
        if arr[i] == 2 * arr[j] and i != j:
            found = True
            break
        elif j == len(arr) - 1:
            j = 0
            i += 1
        else:
            j +=1
    
    return found ,(i,j)
"""    
    
#approach 2 - use sets
def checkIfExist(arr):
    found = False
        
    arr_set = set()
    for num in arr:
        if num/2 in arr_set or num*2 in arr_set:
            return True
        arr_set.add(num)
    return False


start = datetime.datetime.now()
arr = [10,2,5,3] #true
print('Output {}'.format(checkIfExist(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))

print()
start = datetime.datetime.now()
arr = [7,1,14,11] #true
print('Output {}'.format(checkIfExist(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))

print()
start = datetime.datetime.now()
arr = [3,1,7,11] #false
print('Output {}'.format(checkIfExist(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))

print()
start = datetime.datetime.now()
arr = [-2,0,10,-19,4,6,-8]#false
print('Output {}'.format(checkIfExist(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))



print()
start = datetime.datetime.now()
arr = [0,0]#true
print('Output {}'.format(checkIfExist(arr)))
end = datetime.datetime.now()
delta = (end-start).total_seconds() * 1000
print("Time Taken {}ms".format(delta))