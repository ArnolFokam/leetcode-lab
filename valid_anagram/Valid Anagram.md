#array  #sorting
- Anagrams are words that are invariant to the arrangements of the characters they contain.
- Therefore a good way to solution would a be a transformation that map words into a unique value and is invariant to the permutations of characters that is, the transformation should give the same value when receive anagrams as input.
- The complexity (time and space) of our solution will depend on::
	- The complexity of the transformations.
	- Thee complexity of comparing the values obtianed by the transformation.

## Pseudo-code

```c
s = permutation_invariant_transformation(first word)
t = permutation_invariant_transformation(second word)
return s == t
```

A permutation invariant transformation can be a sorting where words can be represented as a list of un-ordered characters. Therefore since characters already have a pre-defined order. Anagram will always have the same order. The updated pseudocode is

```c
return sort(first letter) == sort(second letter)
```

The complixety of this algorithm will be the upper bound of the complexity of the sorting algorithm and the comparison.