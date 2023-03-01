#two-pointers 

- A brute-force solution would be to consider all the possible combinations of bars, calculate the bar area and get the max area.
- However, this solution is $O(n^2)$ and a more effiecient solution exist that uses two pointers
- We want to find the bars the gives the maximum area.
- The area is calculated as:
	- The distance between the two bars
	- The height of the shortest bar
- If we start with our two pointers at both extremities of the height list. We are sure that we have the max distance from the beginning.
- Now, we need to move a way to move  our right and left pointer such that we will eventually encounter the solution.
- Since moving the pointers closer together will always reduce the distance between the two bars, we will not aim for a bigger distance between the bar but for a higher heights of bars and moving the points will always reduce blah blah....
- So now, our criterion for moving the pointer is to find higher bars.
- Therefore, a good solution will be to move the pointer on the smaller bar closer to the other pointer
- There are three outcomes to this scenario
	- **the new bar is smaller:** we get a smaller area which we is ignore
	- **the new bar has the same height:** we get a smaller area which we is ignore
	- **the new bar is higher:** we get an area equal to or greater than the previous area
- This two pointer solution is $O(n)$.

## Pseudo-code

```c
while left < right:
	update area if we get bigger area with l and r
	if bar on r is smaller or equal:
		move r closer to l
	else
		move l closer to r
```