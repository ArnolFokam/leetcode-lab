from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """Module containing the solution
    """
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """_summary_

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            bool: is a cycle detected?
        """
        while head:
            if head.val == float("-inf"):
                return True
            head.val = float("-inf")
            head = head.next
        return False