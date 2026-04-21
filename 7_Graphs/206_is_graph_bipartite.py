"""
206. Is Graph Bipartite?

Time Complexity: O(V + E)
Space Complexity: O(V)
"""
from typing import List
import collections

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {} # node -> 0 or 1
        
        for i in range(len(graph)):
            if i not in color:
                q = collections.deque([i])
                color[i] = 0
                
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = 1 - color[node]
                            q.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True
