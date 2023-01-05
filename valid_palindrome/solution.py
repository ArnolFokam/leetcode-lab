from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, s: str) -> bool:
        """O(n) using two pointers

        Args:
            s (str): suspected palindrome

        Returns:
            bool: result of the check
        """
        
        left = 0
        right = len(s) - 1

        while left < right:
            
            # skip non-alpha numeric charaters
            while not s[left].isalnum() and left < right:
                left += 1
                
            # skip non-alpha numeric charaters
            while not s[right].isalnum() and left < right:
                right -= 1

            # check the palindromic property
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        
        return True
        
    def solve(self, s: str) -> bool:
        """O(n) using two pointers

        Args:
            s (str): suspected palindrome

        Returns:
            bool: result of the check
        """
        return self.algorithm1(s)
