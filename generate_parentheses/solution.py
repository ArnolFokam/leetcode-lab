from typing import List


class Solution:
    """Module containing the solution
    """
        
    def solve(self, n: int) -> List[str]:
        """generate parantheses

        Args:
            n (int): the number of pairs of parantheses to create combinations

        Returns:
            List[str]: combinations of parantheses
        """
        result = []

        def backtrack(openP, closeP, stack):
            if openP == closeP == 0:
                result.append("".join(stack))

            if openP > 0:
                backtrack(openP - 1, closeP, stack + ['('])

            if closeP > openP:
                backtrack(openP, closeP - 1, stack + [')'])

        backtrack(n - 1, n, ['('])

        return result
