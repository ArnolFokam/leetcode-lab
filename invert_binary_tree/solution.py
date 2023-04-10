from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Module containing the solution
    """
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """invert a binary tree

        Args:
            root (Optional[TreeNode]): root of the binary tree

        Returns:
            Optional[TreeNode]: inverted binary tree
        """
        
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        return root
