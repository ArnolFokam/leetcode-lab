from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Module containing the solution
    """
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """return the left of the diameter of a binary tree

        Args:
            root (Optional[TreeNode]): root node of the binary tree

        Returns:
            int: the diameter of a tree
        """
        diameter = [0]
        
        def down(node):
            if node is None:
                return 0
            
            left_h = 1 + down(node.left)
            right_h = 1 + down(node.right)
            
            diameter[0] = max(diameter[0], left_h + right_h - 2)
            
            return max(left_h, right_h)

        down(root)

        return diameter[0]