class Solution:
    """Module containing the solution
    """
        
    def solve(self, s: str) -> bool:
        """checks if parantheses are valid

        Args:
            s (str): string of parantheses

        Returns:
            bool: results of the check
        """
        stack = []
        check = dict(zip(['(', '{',  '['], [')', '}', ']']))
        
        s = list(s)

        while len(s) > 0:

            stack.append(s.pop(0))
            
            if len(stack) > 1 and stack[-2] in check and check[stack[-2]] == stack[-1]:
                stack.pop()
                stack.pop()

        return len(stack) == 0
