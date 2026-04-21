"""
168. Generate Binary Strings without Consecutive 1s

Time Complexity: O(2^N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        
        def dfs(i, path):
            if i == n:
                res.append("".join(path))
                return
            
            # Can always place 0
            path.append("0")
            dfs(i + 1, path)
            path.pop()
            
            # Can place 1 if last is not 1
            if not path or path[-1] != "1":
                path.append("1")
                dfs(i + 1, path)
                path.pop()
                
        dfs(0, [])
        return res
