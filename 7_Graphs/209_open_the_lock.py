"""
209. Open the Lock

Time Complexity: O(10^4)
Space Complexity: O(10^4)
"""
from typing import List
import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
            
        q = collections.deque([("0000", 0)]) # lock, turns
        visit = set(deadends)
        visit.add("0000")
        
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turns + 1))
                    
        return -1
