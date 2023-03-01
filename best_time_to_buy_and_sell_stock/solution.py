from typing import List


class Solution:
    """Module containing the solution
    """
        
    def solve(self, prices: List[int]) -> int:
        """ calculates the max profit from buying and selling stock

        Args:
            prices (List[int]): list of prices

        Returns:
            int: max profit
        """
        buy, sell = 0, 1
        maxP = 0
        
        while sell < len(prices):
            
            while sell < len(prices) and prices[sell] < prices[buy]:
                buy, sell = sell, sell + 1
            
            if sell < len(prices):
                maxP = max(prices[sell] - prices[buy], maxP)
                sell += 1
            
        return maxP
            
            
        
