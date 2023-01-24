from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, numbers: List[int], target: int) -> List[int]:
        """return the index of the target

        Args:
            numbers (List[int]): sorted numobes
            target (int): target numbers

        Returns:
            List[int]: list of two indices of numbers
        """
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
    def solve(self, numbers: List[int], target: int) -> List[int]:
        """return the index of the target

        Args:
            numbers (List[int]): sorted numobes
            target (int): target numbers

        Returns:
        """ 
        return self.algorithm1()
