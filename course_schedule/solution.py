

from typing import List


class Solution:
    """Module containing the solution
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Checks if the courses can be completed

        Args:
            numCourses (int): number of courses
            prerequisites (List[List[int]]): prerequisites

        Returns:
            bool: can the courses be completed?
        """

        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False

            if len(preMap[crs]) == 0:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
