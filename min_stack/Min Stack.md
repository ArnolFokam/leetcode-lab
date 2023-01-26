#stack 

- In this problem we are asked to build a stack data structure with two additional operations
	- Get top element of the stack
	- Get min element of the stack
- The constraint here that makes thing much more difficult is that we are asked to implement all operations in $O(1)$
- For the push, pop, get top stuff, this is easy. But, things gets a little bit more complicated for the min.
- A trivial solution to get the min would have time complexity of $O(n)$ as we loop through all elements of the stack.
- However, we want all operations to $O(1)$.
- This will require an additional data structure to keep track of the minimum number.
- We can't use a heap as while retrieving the min will be consider $O(1)$, append a value will be $O(\log n)$.
- A **Solution** would be to have a data structure that keeps track of the minimum number at each index such that if we pop a value from the last index. We new last index will give us the min but at the new last index
- We just need to make sure that when we append an element, its min value at its index in the second ds is updated correctly
	- Same as previous last min if the new value is not the **min**
	- Its value otherwise as it will be the new **min**