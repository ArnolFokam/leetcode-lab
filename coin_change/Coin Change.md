#1D-DP
- base case: for amount 0 we have 0 amount of coins
- sub-problem: coins[i] = min(1 + coins[i - {all possible coin values available}])
- The iteration is from amount of zero i = 0 to i = requirement amount
- The answer is coins[amount] and -1 if we could find a valid combination of coins
- Time complexity = O(n) loop through the amounts
- Space complexity = O(n) we keep track of the history of coins