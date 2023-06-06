#backtracking
- Simple DFS recursive solution
- Branches are the four next possible positions and the next character to check
- The base case are:
    - Out of bounds: return false
    - Word at current position is not current character: return false
    - We have consider all the character from our word: return true
- Initial call to every possible starting position.
- Time complexity is $O(n*m*4^w)$ where n = num of rows, m = num of cols and w is the length of the word