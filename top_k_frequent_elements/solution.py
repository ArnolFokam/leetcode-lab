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
        """Algorithm that solves the problem in Big O(n) inspired from bucket sort

        Args:
            nums (List[int]): list of numbers
            k (int): top k to return

        Returns:
            List[int]: top k most elements
        """
        
        # holds the count of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # holds numbers per count
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
            
        # loop from largest count to smallest 
        # count until we fill k numbers
        top_k = []
        i = len(freq) - 1
        while len(top_k) < k and i > 0:
            top_k.extend(freq[i][:k - len(top_k)])
            i -= 1
            
        return top_k
        
    def solve(self, nums: List[int], k: int) -> List[int]:
        """Algorithm that solves the problem in Big O(k log n)

        Args:
            nums (List[int]): list of numbers
            k (int): top k to return

        Returns:
            List[int]: top k most elements
        """
        return self.algorithm2(nums, k)
