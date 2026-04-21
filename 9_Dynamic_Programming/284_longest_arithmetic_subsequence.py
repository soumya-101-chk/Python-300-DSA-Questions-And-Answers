"""
284. Longest Arithmetic Subsequence

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""
from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {} # (index, diff) -> length
        res = 2
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
                res = max(res, dp[(i, diff)])
                
        return res
