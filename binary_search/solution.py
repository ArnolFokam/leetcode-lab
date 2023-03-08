from typing import List


class Solution:
    """Module containing the solution
    """
        
    def solve(self, nums: List[int], target: int) -> int:
        """returns the index of the found value in the array

        Args:
            nums (List[int]): list of numbers in the array
            target (int): target value to search

        Returns:
            int: index of the found target
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1
