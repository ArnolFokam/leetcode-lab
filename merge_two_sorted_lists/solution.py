from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """Module containing the solution
    """
        
    def solve(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """merge two sorted list

        Args:
            list1 (Optional[ListNode]): first sorted list
            list2 (Optional[ListNode]): second sorted list

        Returns:
            Optional[ListNode]: merged list
        """
        result = ListNode('-inf')
        ptr = result
        
        while list1 and list2:

            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            
            ptr = ptr.next
        
        if list1:
            while list1:
                ptr.next = list1
                list1 = list1.next
                ptr = ptr.next

        if list2:
            while list2:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next

        return result.next