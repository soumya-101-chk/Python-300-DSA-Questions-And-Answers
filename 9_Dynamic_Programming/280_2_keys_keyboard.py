"""
280. 2 Keys Keyboard

Time Complexity: O(N^2) or O(sqrt N) with prime factorization
Space Complexity: O(N)
"""
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)
        dp[1] = 0
        
        for i in range(2, n + 1):
            for j in range(1, 1 + (i // 2)):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
                    
        return dp[n]
