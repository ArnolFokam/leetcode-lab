#1D-DP
- same as [[House Robber]] but we only need to do one simple modification
- Since the left most and right most should can't be inlcuded in our  robbery touch, we will solve the problem in the same way as [[House Robber]] for each 2 subarray.
	- One where the leftmost is included and the rightmost is another
	- One where it is the contrary
- The time and space complexity is the same as that the other algorithm.