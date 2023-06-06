from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
                
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            
            item = cur.pop()
            
            while i < len(candidates) and candidates[i] == item :
                i += 1
            dfs(i, cur, total)
            
        dfs(0, [], 0)
        return res