"""
285. Last Stone Weight II

Time Complexity: O(N * S) where S is sum of stones
Space Complexity: O(S)
"""
from typing import List
import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)
        dp = {}
        
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                return dp[(i, total)]
                
            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return dp[(i, total)]
            
        return dfs(0, 0)
