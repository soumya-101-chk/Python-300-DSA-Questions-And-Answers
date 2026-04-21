"""
10. Replace Elements with Greatest Element on Right Side

Time Complexity: O(N)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
            
        return arr
