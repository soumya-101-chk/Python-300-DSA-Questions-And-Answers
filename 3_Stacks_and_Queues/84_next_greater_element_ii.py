"""
84. Next Greater Element II

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = [] # indices
        
        for i in range(n * 2):
            idx = i % n
            while stack and nums[idx] > nums[stack[-1]]:
                res[stack.pop()] = nums[idx]
            if i < n:
                stack.append(idx)
                
        return res\n