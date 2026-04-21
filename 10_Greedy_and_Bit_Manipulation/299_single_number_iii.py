"""
299. Single Number III

Time Complexity: O(N)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
            
        # find rightmost 1-bit
        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit = diff_bit << 1
            
        a, b = 0, 0
        for n in nums:
            if diff_bit & n:
                a ^= n
            else:
                b ^= n
                
        return [a, b]
