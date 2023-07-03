#graph 
- Loop through all cells of the grid and perform this check
	- if it is a one and has not yet being visited: increment the number of island and all 4-connected ones to the visited set
	- else: just ignore that iteration of the loop or that cell
- Time complexity is $O(mn)$ and space complexity is $O(mn)$ to keep track of the visited cells
- You can directly modify cell to check if they have been visited this reduces the time complexity to $O(1)$  