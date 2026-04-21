"""
65. Split Linked List in Parts

Time Complexity: O(N)
Space Complexity: O(K) for output array
"""
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1
            
        base_len, remainder = length // k, length % k
        
        res = []
        curr = head
        for i in range(k):
            res.append(curr)
            part_len = base_len + (1 if remainder > 0 else 0)
            remainder -= 1
            
            for j in range(part_len - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt
                
        return res
