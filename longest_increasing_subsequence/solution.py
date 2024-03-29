from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res[i] = max(res[i], 1 + res[j])

        return max(res)