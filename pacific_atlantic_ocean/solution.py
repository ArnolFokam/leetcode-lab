from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        p = [[False for i in range(len(heights[0]))] for i in range(len(heights))]

        # can it reach the pacific ocean
        for i  in range(len(heights)):
            p[i][0] = True

        for j in range(len(heights[0])):
            p[0][j] = True

        queue = [(i, 0) for i in range(len(heights))] + [(0, j) for j in range(1, len(heights[0]))]
        visited = set()

        while queue:
            cell = queue.pop()

            if cell not in visited:

                i, j = cell

                if i + 1 < len(p) and heights[i + 1][j] >= heights[i][j]:
                    p[i + 1][j] = p[i + 1][j] or p[i][j]
                    queue.append((i + 1, j))

                if 0 < i and heights[i - 1][j] >= heights[i][j]:
                    p[i - 1][j] = p[i - 1][j] or p[i][j]
                    queue.append((i - 1, j))


                if j + 1 < len(p[0]) and heights[i][j + 1] >= heights[i][j]:
                    p[i][j + 1] = p[i][j + 1] or p[i][j]
                    queue.append((i, j + 1))


                if 0 < j and heights[i][j - 1] >= heights[i][j]:
                    p[i][j - 1] = p[i][j - 1] or p[i][j]
                    queue.append((i, j - 1))

                visited.add(cell)

        a = [[False for i in range(len(heights[0]))] for i in range(len(heights))]

        for i  in range(len(heights)):
            a[i][-1] = True

        for j in range(len(heights[0])):
            a[-1][j] = True

        queue = [(i, len(heights[0]) -  1) for i in range(len(heights))] + [(len(heights) -  1, j) for j in range(len(heights[0]))]
        visited = set()

        #  can it reach the atlantic ocean
        while queue:
            cell = queue.pop()

            if cell not in visited:

                i, j = cell

                if i + 1 < len(p) and heights[i + 1][j] >= heights[i][j]:
                    a[i + 1][j] = a[i + 1][j] or a[i][j]
                    queue.append((i + 1, j))

                if 0 < i and heights[i - 1][j] >= heights[i][j]:
                    a[i - 1][j] = a[i - 1][j] or a[i][j]
                    queue.append((i - 1, j))


                if j + 1 < len(a[0]) and heights[i][j + 1] >= heights[i][j]:
                    a[i][j + 1] = a[i][j + 1] or a[i][j]
                    queue.append((i, j + 1))


                if 0 < j and heights[i][j - 1] >= heights[i][j]:
                    a[i][j - 1] = a[i][j - 1] or a[i][j]
                    queue.append((i, j - 1))

                visited.add(cell)

        result = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if a[i][j] and p[i][j]:
                    result.append([i, j])

        return result