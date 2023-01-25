from typing import List


class Solution:
    """Module containing the solution
    """
        
    def solve(self, height: List[int]) -> int:
        """returns indeces of bar that will contain the most water

        Args:
            height (List[int]): list of bar height

        Returns:
            int: max area
        """
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxArea
