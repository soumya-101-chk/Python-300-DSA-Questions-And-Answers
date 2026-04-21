"""
179. Partition to K Equal Sum Subsets

Time Complexity: O(k * 2^N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
            
        target = sum(nums) // k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        
        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
                
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                if j > 0 and not used[j - 1] and nums[j] == nums[j - 1]:
                    continue
                    
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
                
            return False
            
        return backtrack(0, k, 0)
