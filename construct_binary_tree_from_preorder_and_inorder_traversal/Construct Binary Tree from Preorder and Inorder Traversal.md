#trees
- recursive computation of the binary tree where
- We get the parent node in preorder
- Since after that (preorder) we have two slices where the left is the left subtree and right is the right subtree
- We need to decide where to slice
- This is where inorder array will help
- We search for that parent node and the position of that node in the inorder array will help use determine
- How many nodes node are in the left subtree and how many nodes are in the right subree.
- The space complexity is O(n) because of the tree creation
- The time complexity is O(n log n) for a balanced binary tree and O(n ^ 2) worst for a vertical tree