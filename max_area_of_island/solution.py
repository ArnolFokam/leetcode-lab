from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = set()

        def get_area(i, j):
            area = 0

            if (i, j) not in visited and 0 <= i < row and 0 <= j < col and grid[i][j] == 1:
                # add area
                area += 1

                # add to visited
                visited.add((i, j))

                # get area
                area += get_area(i - 1, j)
                area += get_area(i + 1, j)
                area += get_area(i, j + 1)
                area += get_area(i, j - 1)

            return area

        res = 0
        for i in range(row):
            for j in range(col):
                area = get_area(i, j)
                res = max(res, area)

        return res