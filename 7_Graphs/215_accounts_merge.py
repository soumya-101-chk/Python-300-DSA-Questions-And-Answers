"""
215. Accounts Merge

Time Complexity: O(N * K log(N * K))
Space Complexity: O(N * K)
"""
from typing import List
import collections

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = collections.defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                email_to_name[email] = name
                
        visited = set()
        res = []
        
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
                res.append([email_to_name[email]] + sorted(component))
                
        return res
