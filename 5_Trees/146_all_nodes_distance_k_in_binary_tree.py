"""
146. All Nodes Distance K in Binary Tree

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
            
        graph = collections.defaultdict(list)
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
                
        res = []
        visit = set([target])
        q = collections.deque([(target, 0)])
        
        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            else:
                for nei in graph[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, dist + 1))
                        
        return res\n