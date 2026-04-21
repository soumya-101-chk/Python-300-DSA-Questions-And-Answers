"""
220. Closest Node to Given Two Nodes

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List
import collections

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(src):
            dist = {src: 0}
            q = collections.deque([src])
            while q:
                node = q.popleft()
                nei = edges[node]
                if nei != -1 and nei not in dist:
                    dist[nei] = dist[node] + 1
                    q.append(nei)
            return dist
            
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        
        res = -1
        min_dist = float("inf")
        
        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                curr_dist = max(dist1[i], dist2[i])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    res = i
                    
        return res
