"""
268. Palindrome Partitioning II

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        dp = [0] * n
        
        for i in range(n):
            min_cuts = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True
                    min_cuts = 0 if j == 0 else min(min_cuts, dp[j - 1] + 1)
            dp[i] = min_cuts
            
        return dp[n - 1]
