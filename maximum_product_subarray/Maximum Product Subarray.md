#1D-DP
- Calculate the contiguous sum of sub array such that you get the max product
- The trick if keep track of the the minimum and maximun product at each position i
- max_T[i] = max{ n[i] * max_T[i + 1],  n[i] * min_T[i + 1], n[i]}, the same equation holds for min_T[i]
- We just keep track of the max encountered so far at each iteration of i.
- Brute force is $O(n^2)$ and this solution $O(n)$