"""
167. Rat in a Maze

Time Complexity: O(3^(N^2))
Space Complexity: O(L * X) where L is length of path, X is number of paths
"""
from typing import List

class Solution:
    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        res = []
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return res
            
        def dfs(r, c, path):
            if r < 0 or c < 0 or r >= n or c >= n or m[r][c] == 0:
                return
            if r == n - 1 and c == n - 1:
                res.append(path)
                return
                
            m[r][c] = 0 # mark visited
            dfs(r + 1, c, path + "D")
            dfs(r, c - 1, path + "L")
            dfs(r, c + 1, path + "R")
            dfs(r - 1, c, path + "U")
            m[r][c] = 1 # backtrack
            
        dfs(0, 0, "")
        return sorted(res)
