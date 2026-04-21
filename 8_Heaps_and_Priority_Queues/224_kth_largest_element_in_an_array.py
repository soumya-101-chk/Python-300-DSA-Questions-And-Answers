"""
224. Kth Largest Element in an Array

Time Complexity: O(N) on average with QuickSelect, O(N log K) with MinHeap
Space Complexity: O(K) for MinHeap
"""
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min Heap Approach
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
