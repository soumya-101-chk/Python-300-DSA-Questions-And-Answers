"""
64. Double a Number Represented as a Linked List

Time Complexity: O(N)
Space Complexity: O(1)
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev, curr = None, node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
            
        reversed_head = reverse(head)
        curr = reversed_head
        carry = 0
        prev = None
        
        while curr:
            val = curr.val * 2 + carry
            curr.val = val % 10
            carry = val // 10
            prev = curr
            curr = curr.next
            
        if carry:
            prev.next = ListNode(carry)
            
        return reverse(reversed_head)
