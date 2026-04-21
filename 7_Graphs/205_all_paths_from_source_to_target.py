"""
205. All Paths From Source to Target

Time Complexity: O(2^V * V)
Space Complexity: O(V)
"""
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1
        
        def dfs(node, path):
            if node == target:
                res.append(path.copy())
                return
                
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
                
        dfs(0, [0])
        return res
