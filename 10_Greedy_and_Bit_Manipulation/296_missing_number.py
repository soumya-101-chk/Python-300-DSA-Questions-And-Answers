"""
296. Missing Number

Time Complexity: O(N)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
