from collections import defaultdict
from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, strs: List[str]) -> List[List[str]]:
        """Solutoin that uses a hash map

        Args:
            strs (List[str]): list of strings
            
        Returns:
            List[List[str]]: list of groups of anagrams
        """
        anagrams = defaultdict(lambda: [])
        
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
            
        return anagrams.values()
        
    def solve(self, strs: List[str]) -> List[List[str]]:
        """Solutoin that uses a hash map

        Args:
            strs (List[str]): list of strings
            
        Returns:
            List[List[str]]: list of groups of anagrams
        """
        return self.algorithm1()
