#linked-list #recursion #iteration

- Its all about reversing the link
- At the end of the day, the head node is the tail node
- However, if we do not reverse carefully, we might end up with a circular condition where a node points to itself
- And then, there will be no way to go to the next node
- This can be solve recursively and iteratively

## Recursively
- base case = NIL pointer
	- return
- Simple case
	- Next node points to current node
	- Current node points to NIL
	- Note: maintain the new head
- **Time complexity:** O(n)
- **Space complexity:** O(n)

## Iteratively
- create a second pointer
- make each element point to the current head of the second pointer and update the second pointer such that the current element is the new head of the second pointer
- **Note:** Do not forget to save the node to which the current element was pointing to in the first pointer
- **Time complexity:** O(n)
- **Space complexity:** O(1)

## Questions
