from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """Module containing the solution
    """
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """deepcopy a list with next and random pointers

        Args:
            head (Optional[Node]): list

        Returns:
            Optional[Node]: deecopied list
        """
        old_to_new = {None: None}

        cur = head
        while cur:
            # create pointer
            tmp = Node(cur.val)

            # map address to new pointer
            old_to_new[cur] = tmp

            # update loop pointer
            cur = cur.next

        cur = head
        while cur:
            # update random pointer of all new nodes
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]

            cur = cur.next
    
        return old_to_new[head]
