"""
233. Top K Frequent Words

Time Complexity: O(N log K)
Space Complexity: O(N)
"""
from typing import List
import collections
import heapq

class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        minHeap = []
        
        for word, count in counts.items():
            heapq.heappush(minHeap, Element(count, word))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap).word)
            
        return res[::-1]
