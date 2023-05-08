from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Module containing the solution
    """
        
    def solve(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """checks if a tree is a subtree of another tree

        Args:
            root (Optional[TreeNode]): original tree
            subRoot (Optional[TreeNode]): potential tree

        Returns:
            bool: returns the result of the check
        """
        def same(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return same(p.left, q.left) and same(p.right, q.right)
            else:
                return False

        if subRoot is None:
            return True

        if root is None:
            return False

        if same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
