"""
294. Number of 1 Bits

Time Complexity: O(1) space, O(1) time
Space Complexity: O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
