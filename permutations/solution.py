from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, avail):
            if len(avail) == 1:
                res.append(subset + [avail.pop(0)])
            else:
                for i in range(len(avail)):
                    dfs(subset + [avail[i]], avail[:i] + avail[i + 1:])
        dfs([], nums.copy())
        return res