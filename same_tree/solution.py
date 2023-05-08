from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Module containing the solution
    """
        
    def solve(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Check if we have the same tree

        Args:
            p (Optional[TreeNode]): first tree
            q (Optional[TreeNode]): second tree

        Returns:
            bool: return the boolean outcome of the check
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.solve(p.left, q.left) and self.solve(p.right, q.right)
        else:
            return False