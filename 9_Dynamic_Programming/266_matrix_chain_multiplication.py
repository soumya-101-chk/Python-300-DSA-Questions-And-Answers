"""
266. Matrix Chain Multiplication

Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""
class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[0 for i in range(N)] for j in range(N)]
        
        for L in range(2, N):
            for i in range(1, N - L + 1):
                j = i + L - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    q = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if q < dp[i][j]:
                        dp[i][j] = q
                        
        return dp[1][N - 1]
