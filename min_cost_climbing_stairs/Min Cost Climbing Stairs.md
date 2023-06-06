#1D-DP
- base case: last and before last stairs each have min cost as their current value
- sub-problem: cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
- iteration: i will for from the before-before-last element to the first element
- Why? for each iteration we choose the stairs the minimizes the cost:
    - either the next one
    - or the next after the next one
- The solution is basically trying to find the min between the first and second stair because we have this choice at the beginning.
- Time complexity is O(n) because we iterate through stairs
- Space complexity is O(1) because do inplace updates on the array