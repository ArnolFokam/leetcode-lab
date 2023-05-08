from typing import List


class Solution:
    """Module containing the solution
    """
        
    def solve(self, nums: List[int]) -> int:
        """Find the duplicate in a list of numbers

        Args:
            nums (List[int]): the list of numbers

        Returns:
            int: the duplicate
        """
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
