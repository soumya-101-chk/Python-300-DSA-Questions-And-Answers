"""
212. Possible Bipartition

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""
from typing import List
import collections

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
            
        color = {}
        
        for i in range(1, n + 1):
            if i not in color:
                color[i] = 0
                q = collections.deque([i])
                while q:
                    node = q.popleft()
                    for nei in adj[node]:
                        if nei not in color:
                            color[nei] = 1 - color[node]
                            q.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True
