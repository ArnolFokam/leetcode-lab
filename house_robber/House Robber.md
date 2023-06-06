#1D-DP
- base case: the two last are the max money if we started with those houses
- sub-problem: the max money if we got the current house money(i) + max{money(i + 2), money(i + 3)}
- We ask ourselve the question what if rob the next house or the next next house
- The iteration is the from the last house to the first house.
- The answer is the max for the first two houses at the end of the iteration
- Time complexity = O(n) loop through the houses
- Space complexity = O(1) because of in-place array modification.