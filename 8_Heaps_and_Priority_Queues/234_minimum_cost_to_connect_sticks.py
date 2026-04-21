"""
234. Minimum Cost to Connect Sticks

Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            cur = first + second
            cost += cur
            heapq.heappush(sticks, cur)
            
        return cost
