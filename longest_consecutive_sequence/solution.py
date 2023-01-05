from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, nums: List[int]) -> int:
        """O(n) algorithm

        Args:
            nums (List[int]): sequence

        Returns:
            int: size of the longest sequence
        """
        
        nums = set(nums)
        longest = 0

        for n in nums:
            
            # begining of sequence indentified
            if n - 1 not in nums:
                length = 1

                # search consecutive numbers
                while n + length in nums:
                    length += 1
                longest = max(longest, length)

        return longest
        
    def solve(self, nums: List[int]):
        """O(n) algorithm

        Args:
            nums (List[int]): sequence

        Returns:
            int: size of the longest sequence
        """
        return self.algorithm1(nums)
