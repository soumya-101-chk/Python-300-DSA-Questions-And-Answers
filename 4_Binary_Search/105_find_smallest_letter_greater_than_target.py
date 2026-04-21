"""
105. Find Smallest Letter Greater Than Target

Time Complexity: O(log N)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        res = letters[0]
        
        while l <= r:
            m = (l + r) // 2
            if letters[m] > target:
                res = letters[m]
                r = m - 1
            else:
                l = m + 1
                
        return res\n