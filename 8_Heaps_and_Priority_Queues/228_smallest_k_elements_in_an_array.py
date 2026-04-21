"""
228. Smallest K Elements in an Array

Time Complexity: O(N log K)
Space Complexity: O(K)
"""
from typing import List
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        maxHeap = []
        for num in arr:
            heapq.heappush(maxHeap, -num)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [-num for num in maxHeap]
