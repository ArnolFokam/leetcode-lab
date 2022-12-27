from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, s: str, t: str) -> bool:
        """Check if two strings are anagrams

        Args:
            s (str): first string
            t (str): second string

        Returns:
            bool: results
        """
        return sorted(s) == sorted(t)
        
    def solve(self, s: str, t: str):
        """Uses one solutions from the stuffs

        Args:
            s (str): first string
            t (str): second string

        Returns:
            bool: results
        """
        return self.algorithm1(s, t)
