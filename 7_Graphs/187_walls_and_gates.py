"""
187. Walls and Gates

Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""
from typing import List
import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = collections.deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
                    
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or
                        (row, col) in visit or rooms[row][col] == -1):
                        continue
                    visit.add((row, col))
                    q.append([row, col])
            dist += 1
