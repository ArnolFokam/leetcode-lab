#two-pointers #sorting 

- In this problem, we are asked to find lists of 3 integers that sums up to 0
- The setting is similar to [[Two Sum]]  and [[Two Sum II - Input Array Is Sorted]] problem but with two major differences
	- We are working here with three integers
	- There might be more than one solution
- The fact that duplicates are not allowed makes it trickier as we also to check (in an effiecient way) to make sure our solution will not contain duplicates.
- A kinda brute-force solution would be to list all possible three sums using 3 nested foor loop and check if they sum to one while ensuring there are no duplicates. This solution is $O(n^3)$ and can be made much more effiecient.
- Recall that we solved both Two Sum problem ([[Two Sum]], [[Two Sum II - Input Array Is Sorted]]) in $O(n)$
- If we loop over number to get the first elements of the 3 sum list, we can reduce the problem to a two sum problem when finding the 2 remaining integers.
- However, note that there is no one solution. Therefore, if we encouter one solution we do not nececessarily stop the progam but update the two pointers such that we can find all solutio for each integer we loop through
- Also, recall we should skip duplicates. Therefore, our code should take this into consideration
- In conclusion our solution will need be O(n * (complexitu needed to solve the two sum problem)) because we loop over integer and for each integers, we solve two sum problem.

## Pseudo-code

```c
for i in integers:
	solve two sums given i
```
