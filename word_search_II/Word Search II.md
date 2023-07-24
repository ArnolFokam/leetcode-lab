#backtracking
- A simple solution as [[Word Search]] would work but it is inefficient since we have to do for every word.
- I would be nice to include some memory through our passes on board.
- The solution is to construct a prefix tree while marking the valid words from our sequence
- Backtrack through a single pass through the entire board ensure that for each step there is a valid branch in the trie
- Do that until you visit every node. Add the words that you encouter along the way into a set as you might encouter a word more than two time.
- The space complexity of the problem is O(k * l) where k is the world length and l is the character length.
- The time compexity is $O(mn 4^{mn})$