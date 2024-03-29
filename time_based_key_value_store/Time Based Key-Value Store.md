#binary-search 
- From this description, we see that we will potentially use another data structure for an effiecient retrieval of the timespan.
- If the timespan was auto-generated, we could just use a stack with dictionary containing timespan and their index in the dictionary
- But we are also given the timespan when ask to set a value
- The question therefore is **"How will we store timespan and element location for effiecient retrieval?"**
- Would be nice to be able to have an always sorted array according to timespan
- The time spans are strictly increasing so the new element will always be ahead of all the previous elements
- This means that if we simply store them in an array, we will never have to update the middle of the array again
	- There is no remove operation
- What is the process of geting a value using a timespan
	- I have a key
	- I index the key
	- I have a timespan
	- What can I do with it?
		- I **may** or **may not** have a value of this timestamp

### NeetCode
- The problem is to find the **greatest timespan less than or equal to the get timespan**
- easy with a linear scan but it O(n)
- Better algorithms are O(log n) and O(1)
- The O(log n) solution is to use binary search to find the **greatest timespan less than or equal to the get timespan** but to get an elment of the closest element less than itself
- Trick here is update the res value every time the middle point is less than timestamp as this is the closest element we know that is less that timestamp