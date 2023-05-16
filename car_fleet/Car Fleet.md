#stack
- The task can be reduced to "if we insert elements (for each car, time needed to reach the target) in a stack such that stack is only allowed to have ever increasing values (monotonic stack), how much element will remain at the end (car fleet at the end)"
- We sort the cars by order or decreasing position and their time remaining to reach the target
- If the new item time is less or equal to the previous one, there is an overlap, remove the new item and keep the old one
- We keep the old item instead of new item because:
	- the old item was slower, therefore, the new item would by force have to adjust to its speed
	- If any subsequent item overlap with the old then we know for sure that it also also with previous new item since we add things in decreasing order of distances