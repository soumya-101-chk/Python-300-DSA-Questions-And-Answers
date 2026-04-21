"""
160. Combination Sum II

Time Complexity: O(2^N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target < 0:
                return
                
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                
        backtrack([], 0, target)
        return res
