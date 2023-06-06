#backtracking 
- The problem is the same as [[Subsets]] and a follow up of [[combination_sum_II/Combination Sum|Combination Sum]]
- We still care about having non duplicates
- But this time, we might have duplicates in our input which makes it harder to avoid duplicate
- Therefore we want a want  to make sure that when we skip a number, we also skip its duplicates
- This will be done by sorting the initial candidates such that the duplicates in the inputs are contiguous.
- Therefore, when we skip something, we make sure that its duplicates are also skipped by iterating to the next index until we find a i that points to a value different from the one we already know