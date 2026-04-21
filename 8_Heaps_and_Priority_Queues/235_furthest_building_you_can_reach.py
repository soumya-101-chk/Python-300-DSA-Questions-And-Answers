"""
235. Furthest Building You Can Reach

Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = [] # will store the ladder climbs
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
                
            heapq.heappush(minHeap, diff)
            if len(minHeap) > ladders:
                bricks -= heapq.heappop(minHeap)
            if bricks < 0:
                return i
                
        return len(heights) - 1
