#1D-DP
#1D-DP 
- You can brute force through a back track solution
- iterate from the left to right with this recurrence relation
- T[i] = max(1, 1 + T[x] {x: nums[x] > nums[i]})
	- Do not forget to check the case where we can have a palindrome with and odd or even number of strings.
- **Time complexity:** O(n\*\*2)
- **Space complexity:** O(1)
- Beware, there exists a an O(n \log n) solution.