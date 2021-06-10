# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:40:34 2020

@author: asaga
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
        
    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.length - 1:
            return -1
        
        i = 0
        curr = self.head
        
        while i!= index:
            curr = curr.next
            i += 1
        return curr.val
            

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        curr = Node(val)
        self.length += 1
        
        if self.head is None:
            self.head = n
        
        else:
            curr.next  = self.head
            self.head = n
        

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = Node(val)
        self.length += 1
        
        if self.head is None:
            self.head = n
        
        else:
            ptr = self.head
            
            while ptr.next:
                ptr = ptr.next
            ptr.next = curr
        

    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            prev = self.head
            curr  = self.head.next
            
            i = 1
            while i < index:
                prev = curr
                curr = curr.next
                i = i+1
            n = Node(val)
            self.length += 1
            prev.next = curr
            n.next = curr
            
        

    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >=0 and index < self.length:
            self.length -= 1
            if index == 0:
                self.head = self.head.next
            else:
                prev = self.head
                cur = self.head.next

                i = 1
                while i < index:
                    prev = cur
                    cur = cur.next
                    i += 1
                
                prev.next = cur.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)