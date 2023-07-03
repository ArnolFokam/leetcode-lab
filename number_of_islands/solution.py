from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0

        row = len(grid)
        col = len(grid[0])

        visited = set()

        def visit(i, j):
            if (i, j) not in visited and 0 <= i < row  and 0 <= j < col and grid[i][j] == "1":
                visited.add((i, j))
                
                visit(i - 1, j)
                visit(i + 1, j)
                visit(i, j - 1)
                visit(i, j + 1)

        for i in range(row):
            for j in range(col):

                if (i, j) not in visited and grid[i][j] == "1":
                    res += 1
                    visit(i, j)

        return res