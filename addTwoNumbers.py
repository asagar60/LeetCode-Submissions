# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:57:58 2020

@author: asaga
"""
"""

Problem :

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

import time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        n = 0
        temp , k = l1, l1
        while (l1 or l2 or n > 0):
            if l1 and l2:
                n = n + l1.val + l2.val   
                l2 = l2.next
            elif l1:
                n = n + l1.val
            elif l2:
                n = n + l2.val
                l2 = l2.next
                
            if l1:
                l1.val = n%10
                k=l1
                l1 = l1.next 
            else:
                k.next = ListNode(n%10)
                k = k.next
            
            n =int(n/10)
        return temp
            