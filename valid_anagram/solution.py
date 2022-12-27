from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, s: str, t: str) -> bool:
        """Algorithmic solution in O(n)

        Args:
            nums (List[int]): list of numbers

        Returns:
            bool: boolean that tells if there is any duplicate
        """
        assert sorted(s) == sorted(t)
        
    def solve(self, s: str, t: str):
        """Method that encapsulates the solution

        Args:
            nums (List[int]): input of the proposed solution

        Returns:
            _type_: result of the solution
        """
        return self.algorithm1(s, t)
