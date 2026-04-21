"""
128. Binary Tree Zigzag Level Order Traversal

Time Complexity: O(N)
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
            
        even_level = False
        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if even_level:
                res.append(val[::-1])
            else:
                res.append(val)
            even_level = not even_level
            
        return res\n