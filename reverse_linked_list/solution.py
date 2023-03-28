from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Module containing the solution
    """
        
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """reverse the linked list

        Args:
            head (Optional[ListNode]): head node

        Returns:
            Optional[ListNode]: new head node
        """
        return self.recursive(head)
    
    
    def iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """reverse the linked list

        Args:
            head (Optional[ListNode]): head node

        Returns:
            Optional[ListNode]: new head node
        """
        result = None

        while head:
            
            # save next node
            tmp = head.next

            # update reversed node
            head.next = result
            result = head

            # update current node
            head = tmp

        return result

    def recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """reverse the linked list

        Args:
            head (Optional[ListNode]): head node

        Returns:
            Optional[ListNode]: new head node
        """
        if not head:
            return None 

        newHead = head
        if head.next:
            newHead = self.recursive(head.next)
            head.next.next = head
            head.next = None

        return newHead
