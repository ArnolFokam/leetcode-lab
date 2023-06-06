from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                rob1, rob2 = rob2, max(rob1 + n, rob2)

            return rob2

        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])
