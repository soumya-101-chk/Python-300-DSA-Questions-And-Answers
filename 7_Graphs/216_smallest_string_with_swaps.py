"""
216. Smallest String With Swaps

Time Complexity: O(N log N + V + E)
Space Complexity: O(V + E)
"""
from typing import List
import collections

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adj = collections.defaultdict(list)
        for u, v in pairs:
            adj[u].append(v)
            adj[v].append(u)
            
        visit = set()
        res = list(s)
        
        for i in range(len(s)):
            if i not in visit:
                chars = []
                indices = []
                
                # dfs
                stack = [i]
                visit.add(i)
                while stack:
                    node = stack.pop()
                    chars.append(s[node])
                    indices.append(node)
                    for nei in adj[node]:
                        if nei not in visit:
                            visit.add(nei)
                            stack.append(nei)
                            
                chars.sort()
                indices.sort()
                for j in range(len(indices)):
                    res[indices[j]] = chars[j]
                    
        return "".join(res)
