#array 
- A simple solution would have been to compute the total product of the all the elements in the array, loop over the elements and divide the product by the current element.
- Unfortunately, we are forbidden to use such method and this solution would fail for cases where there are zero.
- However, we can laverage two properties of this problem to build an O(n) algorithm:
	- At each index, we both have a left and right product
	- We can calculate both products in a cumulative way at each index.
- Therefore, our $O(n)$ solution will: 
	1. Loop over the array to build a left sum array
	2. Loop over the array a second time to build a right sum array
	3. Perform element-wise multiplication of both array to get the solution.
**Note:** We can even skip the element-wise multiplcation at the end if we directly multiply the result of 2. to 1. while traversing the array a second time.

## Pseudo-code

```c
products = [1] * len(nums)

# left product array
for i in index(from 1 to end of nums):
	products[i] = products[i - 1] * nums[i - 1]

# right product array
tmp = 1
for i in index(from before end of nums to begining):
	tmp *= nums[i + 1]
	products[i] = tmp

return product
```