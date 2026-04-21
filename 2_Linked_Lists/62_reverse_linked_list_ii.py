"""
62. Reverse Linked List II

Time Complexity: O(N)
Space Complexity: O(1)
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        
        # Reach node at position "left"
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
            
        # Reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
            
        # Update pointers
        leftPrev.next.next = cur
        leftPrev.next = prev
        
        return dummy.next
