#binary-tree

- You could check in a breadth first search way that left and right child for each node are correct but you also need information about the ancestors to check (there might be cases where a left tree in the right branch is actually less than the node attached to to that branch. sort of)
- So instead of consedering just the parent node, we consider a range of valid values. 
- Of course the root node can be between negative and positive infinity
- The left child can be between the last left range and the parent node exclusive
- The right child can be between the last parent node and last right child
- Since we are check each node in the tree, the time complexity is $O(n)$ and we have a constant space complexity.