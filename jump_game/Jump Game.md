#greedy #1D-DP 

## Dynamic Programming
- We can use dynamic programming to save sub-solution. A sub-solution checks if the last can be reach at any particular position
- Therefore, we can just loop from the end to beginning check if from position i, the last is reachable
- To check if a position is reachable we just iterate over the possible number of jumps and if when doing any of those jumps we reach a position that can reach the last cell, then this means we can also reach the last from the position before the jump.
- The time complexity of this solution can be $O(n^2)$ and the space $O(1)$ if we do in place modification.

## Greedy
- We can make our way from the goal position back to the beginning.
- Our assumption is that if the goal position is reachable from the left, then, we can update our position to the position in the left.
- The assumption helps us to move the goal position closer to the start position.
- Therefore, at each position, we check if the position with its maximum jump length gives the ability to reach the current the goal post
- If yes, we update the goal position to that position.
- The results is a conditional expression that checks if the goal position is 0 (which means that we can reach the goal post from the start position)
- The time complexity of this solution  can be $O(n)$ and the space is still $O(1)$