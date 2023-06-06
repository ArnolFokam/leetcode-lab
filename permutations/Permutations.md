#backtracking
- for each value in the available list
- Pop it and append with the current subset
- Call the function with the update available list and current subset
- Do this until there is no more available number.
- Worse case time comlexity is O(n!)