"""
151. Binary Tree Cameras

Time Complexity: O(N)
Space Complexity: O(H)
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return 1 # covered
                
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0:
                self.res += 1
                return 2 # has camera
            elif left == 2 or right == 2:
                return 1 # covered
            else:
                return 0 # needs camera
                
        return (dfs(root) == 0) + self.res\n