#hashing 
- Anagrams are words that are invariant to the arrangements of the characters they contain.
- A simple solution would be to loop over every words and for every words, check if it is an anagram to the previous ecountered words (possibly one words from the already identified anagram). 
- This solution would have a worst case of $O(nk(s))$  where $k(.)$ would return the complexity of the anagram identifier algorithm and $s$ is the expected length of words we will receive as input..
- Recall from the [Valid Anagram](https://leetcode.com/problems/valid-anagram/) problem that the key to indentify anagrams effeicietly is to build a transformation that maps anagrams to the same value.
- In this context, we can use this value as an index to a hashtable that will store anagrams in the same row.

## Pseudo-code

```c
anagrams = hashtable that will store our anagrams

for word in words:
	add word to anagrams[permutation_invariant_transformation(word)]

return all rows of 'anagrams'
```