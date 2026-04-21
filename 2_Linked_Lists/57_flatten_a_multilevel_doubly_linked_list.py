"""
57. Flatten a Multilevel Doubly Linked List

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import Optional

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        dummy = Node(0, None, head, None)
        self.dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next
        
    def dfs(self, prev, curr):
        if not curr:
            return prev
            
        curr.prev = prev
        prev.next = curr
        
        tempNext = curr.next
        tail = self.dfs(curr, curr.child)
        curr.child = None
        
        return self.dfs(tail, tempNext)
