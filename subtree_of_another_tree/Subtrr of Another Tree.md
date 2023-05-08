#linked-list 
- Traverse the original tree recursively
- When you hit a node such that its value is the same as the value of the potential subtree
- Check that the two trees are equal using the [[Same Tree]] algothm
- The time complexity for this problem is O(s\*n) where s is the number of nodes in the subtree and n is the number of nodes in the original tree
- The space complexity is O($h_s$\*$h_n$) where $h_s$ and $h_n$ are respectively the height of the original tree and subtree.