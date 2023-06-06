#1D-DP
- base case: last and before last stairs each have 1 possible ways of climbing stairs
- sub-problem: before_last(t) = last(t - 1) + before_last(t - 1), last = before_last(t - 1)
- iteration: t go from the last 0 to the first n - 1
- Why? for each iteration we can climb the stairs in two ways:
    - Either we go one step further and we take the number of ways from the current before last
    Or we go two steps further and we take the number of ways from the current last
- Time complexity is O(n) because we iterate through stairs
- Space complexity is O(1) because we only keep track of the last and before last