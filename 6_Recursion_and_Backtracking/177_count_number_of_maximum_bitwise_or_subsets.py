"""
177. Count Number of Maximum Bitwise-OR Subsets

Time Complexity: O(2^N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n
            
        res = 0
        def dfs(i, cur_or):
            nonlocal res
            if i == len(nums):
                if cur_or == max_or:
                    res += 1
                return
                
            dfs(i + 1, cur_or | nums[i])
            dfs(i + 1, cur_or)
            
        dfs(0, 0)
        return res
