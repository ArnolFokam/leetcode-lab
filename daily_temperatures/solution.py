from typing import List


class Solution:
    """Module containing the solution
    """
        
    def solve(self, temperatures: List[int]) -> List[int]:
        """predict the number of times before we hit a higher temperature

        Args:
            temperatures (List[int]): list of daily temperatures

        Returns:
            List[int]: the number of times before we hit a higher temperature
        """
        seen = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while len(seen) > 0 and temperatures[i] > temperatures[seen[-1]]:
                idx = seen.pop()
                result[idx] = i - idx

            seen.append(i)

        return result