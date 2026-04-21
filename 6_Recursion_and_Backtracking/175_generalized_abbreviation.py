"""
175. Generalized Abbreviation

Time Complexity: O(N * 2^N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        
        def dfs(i, cur, count):
            if i == len(word):
                if count > 0:
                    cur += str(count)
                res.append(cur)
                return
                
            # Abbreviate current char
            dfs(i + 1, cur, count + 1)
            
            # Keep current char
            num = str(count) if count > 0 else ""
            dfs(i + 1, cur + num + word[i], 0)
            
        dfs(0, "", 0)
        return res
