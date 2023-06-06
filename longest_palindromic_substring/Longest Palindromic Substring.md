#1D-DP 
- the solution can be solved with bruteforce but listing all possible substrings in O(n\*\*2) and check if they are palindromes in O(n) which gives an O(n\*\*3) solution.
- A improvement would be to assume we could check if the substring is a palindrome from its middle, then loop through each character of the original input string and check if the longest palindrome from the there assuming it might be the middle.
	- Do not forget to check the case where we can have a palindrome with and odd or even number of strings.
- **Time complexity:** O(n\*\*2)
- **Space complexity:** O(1)