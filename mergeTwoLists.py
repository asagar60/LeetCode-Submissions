# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:44:28 2020

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
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: 
            print(l2.val)
            return l2
        if not l2 :
            print(l1.val)
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            print(l1.val)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            print(l2.val)
            return l2
    
    
    """
    def mergeTwoLists(self, l1, l2):
        
        if l1==None and l2 ==None:
            print("cond 1")
            return None
        elif l1==None:
            print("cond 2")
            return l2
        elif l2 == None:
            print("cond 3")
            return l1
        
        l3, l3_ptr = None, None 
        
        while(l1 != None or l2 != None):
            
            if l1 == None:
                l3_ptr.next = l2
                break
            elif l2== None:
                l3_ptr.next = l1
                break
            
            elif l1.val < l2.val:
                if l3 == None:
                    l3 = ListNode(l1.val)
                    print(l3.val)
                    l3_ptr = l3
                else:
                    l3_ptr.next = ListNode(l1.val)
                    print(l3_ptr.val)
                    l3_ptr = l3_ptr.next
                l1 = l1.next
            else:
                if l3 == None:
                    l3 = ListNode(l2.val)
                    print(l3.val)
                    l3_ptr = l3
                else:
                    l3_ptr.next = ListNode(l2.val)
                    print(l3_ptr.val)
                    l3_ptr = l3_ptr.next
                l2 = l2.next
        return l3
        
        """

x = ListNode(4)
x = x.add_list([2,1])

y = ListNode(4)
y = y.add_list([3,1])

x.print_list()
y.print_list()

start = time.time()
X = Solution().mergeTwoLists(x,y)
print(X.print_list())

print( 'Time Taken: {}'.format(time.time()- start))