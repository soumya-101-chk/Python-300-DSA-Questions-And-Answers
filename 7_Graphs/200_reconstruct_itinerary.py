"""
200. Reconstruct Itinerary (Hierholzer's)

Time Complexity: O(E log E)
Space Complexity: O(E)
"""
from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort(key=lambda i: i[1])
        for u, v in tickets:
            adj[u].append(v)
            
        res = []
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop(0)
                dfs(dest)
            res.append(src)
            
        dfs("JFK")
        return res[::-1]
