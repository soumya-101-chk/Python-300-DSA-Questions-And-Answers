"""
88. Koko Eating Bananas

Time Complexity: O(N log M) where M is max pile size
Space Complexity: O(1)
"""
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
                
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
                
        return res\n