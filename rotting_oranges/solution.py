from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    fresh += 1
                    
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions= [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    # if in bounds and fresh make rotten
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
                     
            time += 1
            
        return time if fresh == 0 else -1
                     
                     