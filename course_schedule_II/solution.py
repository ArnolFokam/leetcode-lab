from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inserted = set()
        result = []
        
        preMap = {c: set() for c in range(numCourses)}
        
        for crs, preq in prerequisites:
            preMap[crs].add(preq)
            
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False

            if crs in inserted:
                return True
            
            visited.add(crs)
            for preq in preMap[crs]:
                if not dfs(preq): return False
            visited.remove(crs)
            
            preMap[crs] = set()
            result.append(crs)
            inserted.add(crs)
            
            return True
            
        for crs in preMap:
            if not dfs(crs): return []
        
        return result
            
