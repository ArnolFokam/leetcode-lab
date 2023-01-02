#array #hashing 
- A trivial solution would be to build all possible pairs in the list, calculate their sum and check if this sum is equal to the target number. The complexity of this algorithm is of $O(n^2)$
- However, this problem can be reduced into a *search the element* problem.
- Think about it, if we are asked to find a pair of numbers for which their sum is equal to a target number, therefore, for each number, there exists exactly one number that satisfies the previous requirements. If we use the appropriate data structure, we would be able to check this requirement is $O(1)$ time complexity for each element traversed in the original list of numbers given.

## Pseude-code

```c
s = set()

for every elements l in the (list of numbers)
	t = target - l
	if t is in s:
		return [index of t, index of l]
	else:
		add l to s
```