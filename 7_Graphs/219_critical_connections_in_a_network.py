"""
219. Critical Connections in a Network (Tarjan's)

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""
from typing import List
import collections

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = collections.defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        discovery_time = [-1] * n
        lowest_time = [-1] * n
        res = []
        self.time = 0
        
        def dfs(node, parent):
            discovery_time[node] = lowest_time[node] = self.time
            self.time += 1
            
            for nei in adj[node]:
                if nei == parent:
                    continue
                if discovery_time[nei] == -1:
                    dfs(nei, node)
                    lowest_time[node] = min(lowest_time[node], lowest_time[nei])
                    if lowest_time[nei] > discovery_time[node]:
                        res.append([node, nei])
                else:
                    lowest_time[node] = min(lowest_time[node], discovery_time[nei])
                    
        dfs(0, -1)
        return res
