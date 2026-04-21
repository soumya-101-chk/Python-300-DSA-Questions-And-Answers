"""
109. Longest Increasing Subsequence (Binary Search approach)

Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)
                sub[idx] = x
                
        return len(sub)\n