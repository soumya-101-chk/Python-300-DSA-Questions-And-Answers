"""
24. Find All Duplicates in an Array

Time Complexity: O(N)
Space Complexity: O(1) beyond output
"""
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                res.append(n)
            else:
                nums[n - 1] = -nums[n - 1]
        return res
