from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, nums: List[int]) -> bool:
        """Algorithmic solution in O(n)

        Args:
            nums (List[int]): list of numbers

        Returns:
            bool: boolean that tells if there is any duplicate
        """
        return len(nums) != len(set(nums))
        
    def solve(self, nums: List[int]):
        """Method that encapsulates the solution

        Args:
            nums (List[int]): input of the proposed solution

        Returns:
            _type_: result of the solution
        """
        return self.algorithm1(nums)
