"""
172. Non-decreasing Subsequences

Time Complexity: O(N * 2^N)
Space Complexity: O(N * 2^N)
"""
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def dfs(i, path):
            if len(path) > 1:
                res.add(tuple(path))
                
            for j in range(i, len(nums)):
                if not path or nums[j] >= path[-1]:
                    path.append(nums[j])
                    dfs(j + 1, path)
                    path.pop()
                    
        dfs(0, [])
        return [list(r) for r in res]
