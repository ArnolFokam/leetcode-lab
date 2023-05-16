#sliding-window #hashing 
- We consider substring of fixed length (length of s1)
- For each substrin, we check the match
- Crux of the method is in the way we check
	- Dictionary of alphabet O(26.n) = O(n)
	- Keep track of the number of matches O(n)
- Space complexity is O(1)