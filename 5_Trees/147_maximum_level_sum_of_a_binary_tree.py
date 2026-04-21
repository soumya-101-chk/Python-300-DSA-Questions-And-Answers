"""
147. Maximum Level Sum of a Binary Tree

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        res_level = 0
        level = 1
        q = collections.deque([root])
        
        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            if level_sum > max_sum:
                max_sum = level_sum
                res_level = level
            level += 1
            
        return res_level\n