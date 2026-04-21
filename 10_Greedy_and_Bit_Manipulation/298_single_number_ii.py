"""
298. Single Number II

Time Complexity: O(N)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
            
        return ones
