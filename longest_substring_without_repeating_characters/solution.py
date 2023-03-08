class Solution:
    """Module containing the solution
    """
        
    def solve(self, s: str) -> int:
        """longest substring without repeating characters

        Args:
            s (str): string to search

        Returns:
            int: length of the longest substring without repeating characters
        """
        l, r = 0, 0
        seen = {}
        max_len = 0

        while r < len(s):

            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            else:
                max_len = max(max_len, r - l + 1)

            
            seen[s[r]] = r
            r += 1

        return max_len
