#stack 

- For each number in the list, the problem requires us to find the first number greater than that number in the list.
- A trivial solution would be to loop through the array for each number and identity a first number greater than this number. 
- However, this solution is $O(n^2)$ as we have two for loops.
- Remark that if we can have a situation where in one region of the list, we have a decreasing sequence of numbers and the next number if greater than every number in the sequence.
- Our trivial solution will do a loop for each number in the sequence but will identify the same number everytime
- Is there way to make sure that if know that a number x is not just greater than the previous number, but greater than the previous sequence.
- Yes, If we keep a list of decreasing stack when we encounter a number greater than the top of the stack we know that we have found a number greater than a previous numbers, we popped out this previous number.
- If we can pop out the other previous numbers if they are smaller than that number as well.
- Keep a stack of indices instead of numbers will make it possible to know the difference in index between both numbers and this will used to generate our result

## Pseudo-code
```c

for each idx in list of numbers:
	while stack is not empty and top of stack is less than number at current idx
		pop out index of that number: idx2
		get the differences in position in the original list
		update result at index idx2 with the difference
	append the idx to the stack
```

## Complexity
space: $O(n)$ to keep stack and result
time: $O(n)$ push and pop from the stack at most 2 times for each elements

### Note
- Problem asking us to identity one-one relationship between number will likely require a stack