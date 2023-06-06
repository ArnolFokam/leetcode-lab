from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]

        for i in range(1, amount + 1):
            tmp = float('inf')
            for c in coins:
                if c <= i:
                    tmp = min(tmp, 1 + dp[i - c])
            dp.append(tmp)

        return dp[amount] if dp[amount] != float('inf') else -1