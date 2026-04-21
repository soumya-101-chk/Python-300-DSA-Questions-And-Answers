"""
110. Minimum Speed to Arrive on Time

Time Complexity: O(N log(Max_Speed))
Space Complexity: O(1)
"""
from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
            
        l, r = 1, 10**7
        res = -1
        
        while l <= r:
            m = (l + r) // 2
            time = 0
            for i in range(len(dist) - 1):
                time += math.ceil(dist[i] / m)
            time += dist[-1] / m
            
            if time <= hour:
                res = m
                r = m - 1
            else:
                l = m + 1
                
        return res\n