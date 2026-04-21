"""
217. Longest Cycle in a Graph

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visit = set()
        res = -1
        
        for i in range(n):
            if i not in visit:
                node_dist = {}
                dist = 0
                curr = i
                while curr != -1 and curr not in visit:
                    visit.add(curr)
                    node_dist[curr] = dist
                    dist += 1
                    curr = edges[curr]
                if curr != -1 and curr in node_dist:
                    res = max(res, dist - node_dist[curr])
                    
        return res
