"""
174. Gray Code

Time Complexity: O(2^N)
Space Complexity: O(2^N)
"""
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x + (1 << i) for x in reversed(res)]
        return res
