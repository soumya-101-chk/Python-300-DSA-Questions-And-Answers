"""
230. Minimum Number of Refueling Stops

Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxHeap = []
        stations.append([target, 0])
        res = 0
        prev = 0
        fuel = startFuel
        
        for pos, gas in stations:
            fuel -= (pos - prev)
            while maxHeap and fuel < 0:
                fuel += -heapq.heappop(maxHeap)
                res += 1
            if fuel < 0:
                return -1
            heapq.heappush(maxHeap, -gas)
            prev = pos
            
        return res
