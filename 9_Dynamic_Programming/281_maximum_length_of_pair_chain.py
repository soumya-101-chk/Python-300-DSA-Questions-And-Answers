"""
281. Maximum Length of Pair Chain

Time Complexity: O(N log N)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr = float("-inf")
        res = 0
        
        for start, end in pairs:
            if start > curr:
                curr = end
                res += 1
                
        return res
