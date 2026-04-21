"""
259. Wildcard Matching

Time Complexity: O(S * P)
Space Complexity: O(P)
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [False] * (m + 1)
        dp[0] = True
        
        for j in range(1, m + 1):
            if p[j - 1] == "*":
                dp[j] = dp[j - 1]
                
        for i in range(1, n + 1):
            prev = dp[0]
            dp[0] = False
            for j in range(1, m + 1):
                temp = dp[j]
                if p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                    dp[j] = prev
                elif p[j - 1] == "*":
                    dp[j] = dp[j] or dp[j - 1]
                else:
                    dp[j] = False
                prev = temp
                
        return dp[m]
