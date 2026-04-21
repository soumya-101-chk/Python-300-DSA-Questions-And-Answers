"""
231. IPO

Time Complexity: O(N log N + K log N)
Space Complexity: O(N)
"""
from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        minCapital.sort()
        
        maxProfit = []
        i = 0
        
        for _ in range(k):
            while i < len(minCapital) and minCapital[i][0] <= w:
                heapq.heappush(maxProfit, -minCapital[i][1])
                i += 1
                
            if not maxProfit:
                break
                
            w += -heapq.heappop(maxProfit)
            
        return w
