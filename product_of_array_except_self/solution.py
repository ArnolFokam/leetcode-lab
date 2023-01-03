from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, nums: List[int]) -> List[int]:
        """solution in O(n) time complexity

        Args:
            nums (List[int]): list of numbers

        Returns:
            List[int]: list of products
        """
        # get the intial product
        products = [1] * len(nums)
        
        # calculate the left product
        for i in range(1, len(nums)):
            products[i] = products[i - 1] * nums[i - 1]

        # calculate the right product
        tmp = 1
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]
            products[i] *= tmp

        return products
        
    def solve(self, nums: List[int]) -> List[int]:

        return self.algorithm1(nums)
