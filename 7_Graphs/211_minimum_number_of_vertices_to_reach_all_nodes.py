"""
211. Minimum Number of Vertices to Reach All Nodes

Time Complexity: O(V + E)
Space Complexity: O(V)
"""
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
            
        res = []
        for i in range(n):
            if indegree[i] == 0:
                res.append(i)
                
        return res
