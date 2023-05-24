from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        
        subset = []
        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
            else:
                # All subsets that include nums[i]
                subset.append(nums[i])
                backtrack(i + 1)
                
                # All subsets that do not include nums[i]
                subset.pop()
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                backtrack(i + 1)
                
        
        backtrack(0)
        return res