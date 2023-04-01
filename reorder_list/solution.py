from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Module containing the solution
    """
        
    def solve(self, head: Optional[ListNode]) -> None:
        result = head
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        prev, s.next = None, None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        result = first
        while second:
            tmp = first.next
            first.next = second
            second = second.next
            first.next.next = tmp
            first = first.next.next

        return result
