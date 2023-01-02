#array  #sorting
- Anagrams are words that are invariant to the arrangements of the characters they contain.
- Therefore a nice solution would a be a transformation that map words into a unique value and is invariant to the permutations of characters. In other words, the transformation should give the same value for all words that are identified as anagrams.
- The complexity (time and space) of our solution will depend on:
	- The complexity of the transformations.
	- Thee complexity of comparing the values obtained by the transformation.

## Pseudo-code

```c
s = permutation_invariant_transformation(first word)
t = permutation_invariant_transformation(second word)
return s == t
```

A permutation-invariant transformation can be a sorting algorithm where words can be represented as a list of un-ordered characters. Therefore since characters already have a pre-defined order. Anagrams will always have the same order. The updated pseudocode is

```c
return sort(first letter) == sort(second letter)
```

The complixety of this algorithm will be the upper bound of the complexity of the sorting algorithm and the comparison (usually $O(n\log n)$).