#tree 
- This problem is the same [[Maximum Depth of Binary Tree]]
- The only difference is that you need to keep track of the maximum of a variable which the diameter of the tree
- The diameter is just the longest path between any node in the tree
- It can be easily calculated by keeping track of the sum of the left sub-tree and right sub-tree in a list.
- You can do this recursively
- Time and space complexity is $O(n)$