"""
98. Split Array Largest Sum

Time Complexity: O(N log(Sum(N) - Max(N)))
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarrayCount = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarrayCount += 1
                    curSum = n
            return subarrayCount <= k

        l, r = max(nums), sum(nums)
        res = r
        
        while l <= r:
            m = l + ((r - l) // 2)
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
                
        return res\n