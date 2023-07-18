#greedy
- Loop through each triplet and for each triple:
    - sikp if any of its values is greater thatn the target
    - add to a set **good** the entris of that triplet that match the target at the corresponding entry
- The result returns if the set **good** is 3
- The time complexity is $O(n)$ and the space complexity is $O(1)$