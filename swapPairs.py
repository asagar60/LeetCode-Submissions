# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:42:39 2020

@author: asaga 
"""

import time

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def add(self, d):
        
        #add in the beginning of the list
        new_node = ListNode(d, self)
        self = new_node
        
    def add_list(self, items):
        
        x  = ListNode(self.val)
        for i in items:
            new_node = ListNode(i)
            new_node.next = x
            x = new_node
        return x
        
    def print_list(self): 
        this_node = self
        while this_node is not None:
            print(this_node.val, end='->')
            this_node = this_node.next
        print('None')
        
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
         
        if head==None or head.next==None:
            return head
        
        curr, prev, temp = head.next, head, head
        
        while True:
           prev.next = curr.next
           curr.next = prev
           if temp == head:
               head = curr
           else:
               temp.next = curr
                
           if prev.next==None or  prev.next.next==None:
               break
           temp = prev
           prev = prev.next
           curr = prev.next
               
        return head
            
        
        
x = ListNode(7)
x = x.add_list([6,5,4,3,2,1])
x.print_list()


x = None
start = time.time()
X = Solution().swapPairs(x)
print(X.print_list())
print(X)
print( 'Time Taken: {}'.format(time.time()- start))