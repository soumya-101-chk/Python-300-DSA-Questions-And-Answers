"""
34. Non-overlapping Intervals

Time Complexity: O(N log N)
Space Complexity: O(1) or O(N) depending on sort
"""
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        res = 0
        prevEnd = float("-inf")
        
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                
        return res
