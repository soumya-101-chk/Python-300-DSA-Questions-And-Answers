"""
300. Maximum XOR of Two Numbers in an Array

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            found = set([n & mask for n in nums])
            
            temp = max_xor | (1 << i)
            for prefix in found:
                if temp ^ prefix in found:
                    max_xor = temp
                    break
                    
        return max_xor
