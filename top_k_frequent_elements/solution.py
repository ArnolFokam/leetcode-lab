from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, nums: List[int], k: int) -> List[int]:
        """Algorithm that solves the problem in Big O(k log n)

        Args:
            nums (List[int]): list of numbers
            k (int): top k to return

        Returns:
            List[int]: top k most elements
        """
        from collections import defaultdict

        nums2 = defaultdict(lambda :0)

        for n in nums:
            nums2[n] += 1

        sorted_nums  = sorted(nums2.keys(), key=lambda k: nums2[k], reverse=True)
        return sorted_nums[:k]
    
    def algorithm2(self, nums: List[int], k: int) -> List[int]:
        """Algorithm that solves the problem in Big O(k log n)

        Args:
            nums (List[int]): list of numbers
            k (int): top k to return

        Returns:
            List[int]: top k most elements
        """
        pass
        
    def solve(self,nums: List[int], k: int) -> List[int]:
        """Algorithm that solves the problem in Big O(k log n)

        Args:
            nums (List[int]): list of numbers
            k (int): top k to return

        Returns:
            List[int]: top k most elements
        """
        return self.algorithm1()
