"""
253. Interleaving String

Time Complexity: O(M * N)
Space Complexity: O(N)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [False] * (len(s2) + 1)
        dp[len(s2)] = True
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[j]:
                    dp[j] = True
                elif j < len(s2) and s2[j] == s3[i + j] and dp[j + 1]:
                    dp[j] = True
                else:
                    dp[j] = False
            # Handle the empty case properly
            if i == len(s1):
                dp[len(s2)] = True
                
        return dp[0]
