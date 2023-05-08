from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """Module containing the solution
    """
        
    def solve(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """add two numbers from a linked list

        Args:
            l1 (Optional[ListNode]): first number
            l2 (Optional[ListNode]): second number

        Returns:
            Optional[ListNode]: the result of the addition
        """
        remainder = 0
        result = ListNode(0)
        ptr = result

        while l1 or l2 or remainder:
            tmp = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remainder
            remainder = tmp // 10
            tmp = tmp % 10

            # update numbers
            ptr.next = ListNode(tmp)

            # update pointers
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next