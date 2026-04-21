"""
155. Binary Tree Vertical Order Traversal

Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from typing import List, Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = collections.defaultdict(list)
        q = collections.deque([(root, 0, 0)]) # node, row, col
        
        while q:
            node, row, col = q.popleft()
            nodes[col].append((row, node.val))
            
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
                
        res = []
        for col in sorted(nodes.keys()):
            # Sort by row first, then by value
            col_nodes = sorted(nodes[col])
            res.append([val for row, val in col_nodes])
            
        return res\n