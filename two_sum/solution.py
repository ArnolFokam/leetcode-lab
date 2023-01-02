from typing import List, Tuple

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, nums: List[int], target: int) -> Tuple[int, int]:
        """Solves the two sum problem using a hashmap

        Args:
            nums (List[int]): list of numbers
            target (int): target sum

        Returns:
            Tuple[int, int]: the index of the number that will return the sum
        """
        nums2 = {}
        
        for i in range(len(nums)):
            # calculete the number to search
            other_n = target - nums[i]
            
            if other_n in nums2:
                # return indeces if pair found
                return [nums2[other_n], i]
            else:
                # add element and index if found
                nums2[nums[i]] = i
        
    def solve(self, nums: List[int], target: int):
        """Solves the two sum problem using a hashmap

        Args:
            nums (List[int]): list of numbers
            target (int): target sum

        Returns:
            Tuple[int, int]: the index of the number that will return the sum
        """
        return self.algorithm1(nums, target)
