#sliding-window

## My Thoughts

- Stocks obey the buy low, sell high technique.
- Naively doing this approach would look like this:
	- Search for the lowest price
	- Searching for the hight price after the stocks were bought (index of the lowest price)
- But then, what if:
	- The highest price after the stock were bought at that lowest price does not give the maximum profit. Example: In [3,   100,  2, 4], 2 is the lowest price and the next highest price is 4 so we have a profit of 2 but we missed a profit of 97 because we tried to be greedy
- It seems like we almost need to consider the difference in the prices instead of individial value.
- Something like what is the difference between the price at indices [0, 1] and prices and indeces [0, 2] and then make a choice with respect to that.
- If we consider this solution, then how are we gonna update the indices so that we converge to a global maximum prices.
- A simple solultion will just be to calculate all the profits that can be made by testing all combinations of buy-sell we can make. But this solution runs in $O(n^2)$ where n is the number of stock prices.
- What if we start from any to pairs of prices and update things from there.
- We could start from:
	- [0 , 1]
	- [0, last price]
- If we start from any one of those we have three case
	- Prices lower than current max
	- Prices greater than current max
- We can ignore the case where the price is equal to the current max as it is not relevant.
- Therefore in this case, how should we update the indices for each case

##### Prices lower
- Therefore we need to update the indices such that we have a greater price. How?
	- Pushing the buy indice to a new lower value if possible
	- Pushing the sell indoce to a new bigger value if possible

**Note 1.1:** Pushing those prices might lead to collision if we initialize the indices using [0, 1] and we have the prices 7, 2, 1

Therefore it is advantegous to start with [0, last price] and push the indeces closer together until they meet? But is there an any with this technique?
- One I see is that what if the potentially new value is not desirable? Where do we push in such cases
	- prices[buy_index + 1]  > prices[buy_index] and  prices[sell_index - 1]  < prices[sell_index]
	- We can't abort the program because even if that's weird, there might be a spike in the middle of the prices that would potentially ignore.
- A solution to that would to just set on updating one index to be able to continue. What would be a problem to this solution?
	- Pushing the indices like this might also make us miss the maximum because of the following reasons
		- Onlyb pushing one index when we don't know what to push will make us miss the time when we needed to push the other index 
- What if we push the index such that we get the profit between our two choices...

## Neetcode
- Basically, my issue at **Note 1.1** could avoided by using just pushing the two prices index by one.
	- Example: if we have  7 1 2 ... we can just the indices from 7 1 to 1 2.
- So how do we continue from there? Is it worth check if prices[buy_index + 1]  > prices[buy_index] or prices[left_index]  > prices[buy_index] .
- **The solution to this algorithm is the later**
- The we have two alternatives:
	- prices[buy_index]  > prices[sell_index] push both indices to the right
	- prices[buy_index]  < prices[sell_index] update max profit if we found higher and push the sell index forward
		- **Why do we push sell index forward?** Well if we push the buy index we take the risk of setting a higher lower bound that automatically bounds the profit to a lower one compared to if we had some thing different.
		- **What if we get a lower value index instead?** well time to check https://www.youtube.com/watch?v=1pkOgXD63yU&t=193s