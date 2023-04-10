from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Module containing the solution
    """
        
    def  maxDepth(self, root: Optional[TreeNode]) -> int:
        """calculate the maximum depth of a tree

        Args:
            root (Optional[TreeNode]): root of the tree

        Returns:
            int: max depth of the tree
        """
        def down(node):
            if node is None:
                return 0

            return max(1 + down(node.left), 1 + down(node.right))

        return down(root)