#sliding-window

## My Thoughts

- Stocks obey the buy low, sell high law. 
- Therefore, a simple solution would be to calculate all the profits that can be made by testing all combinations of buy-sell we can make. But this solution runs in $O(n^2)$ where n is the number of stock prices.
- But it turns out that if we rephrase the problem different, we get a lot more interesting insight about the problem.
- This problem is equivalent to finding two numbers in a list that gives the biggest difference.
- Since the list of numbers are stocks, we know that it obeys a temporal logic therefore we can buy at a price with is at the right of our selling prices
- A first starting solution will be to consider the prices at index 0 - 1
- Since we want the biggest positive diffference between two numbers. We will first have these constrainsts:
	- buy price should always be less than sell price
- Therefore we can just through the list of numbers through a sliding window technique such that we ensure we only consider solution where the buying price is less than the selling price
- What if we encouter the sell price that is less that the buying price.
- Well, there is the possibility the we get an even better buying price.
- Therefore, we update buying price to that index and set the selling price to the next index since we can sell before buying.