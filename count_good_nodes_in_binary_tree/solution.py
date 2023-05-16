# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def get_good(node, cur_max):

            if node is None:
                return 0

            good = 0 if cur_max > node.val else 1
            curr_max = max(node.val, cur_max)
            good += get_good(node.left, curr_max)
            good += get_good(node.right, curr_max)

            return good

        return get_good(root, float('-inf'))