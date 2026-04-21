"""
166. Sudoku Solver

Time Complexity: O(9^M) where M is number of blanks
Space Complexity: O(M)
"""
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(r, c, k):
            for i in range(9):
                if board[i][c] == k or board[r][i] == k:
                    return False
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k:
                    return False
            return True
            
        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            if isValid(i, j, k):
                                board[i][j] = k
                                if backtrack():
                                    return True
                                board[i][j] = '.'
                        return False
            return True
            
        backtrack()
