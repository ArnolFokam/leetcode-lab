#greedy 
- We will start with a total and starting position at 0
- For each position i, add gas[i] - cost[i] to the total and check if it is negative
- if negative , reset the total to 0
- else, set this as starting position and continue till we run out of gas
- However, if we reach the end of the loop then, this means that that position is the solution since according to our problem:
	- There is one unique solution
	- We have already encountered previous position and just the fact that we reached this position and it was updated to a starting position means that all the previous positions are not solutions.
- The time complexity is $O(n)$
