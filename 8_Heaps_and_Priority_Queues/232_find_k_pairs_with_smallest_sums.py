"""
232. Find K Pairs with Smallest Sums

Time Complexity: O(K log K)
Space Complexity: O(K)
"""
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2:
            return res
            
        minHeap = []
        visit = set([(0, 0)])
        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        
        while minHeap and len(res) < k:
            val, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            
            if i + 1 < len(nums1) and (i + 1, j) not in visit:
                visit.add((i + 1, j))
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                
            if j + 1 < len(nums2) and (i, j + 1) not in visit:
                visit.add((i, j + 1))
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return res
