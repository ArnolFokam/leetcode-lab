#backtracking
- Same as [[Subsets]]
- However ever since there are duplicates we want a method that prevents us from having those duplicates.
- So the algorithm is the same, we just need to make sure that when we choose not to include the current number, we only include the next number if it is not the duplicate of the number we choose not to ommit.