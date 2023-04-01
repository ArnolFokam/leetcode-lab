#linked-list #two-pointers 
- You can reverse the list and count from a new head but this solution is O(n) with 2 passes
- Another solution is to use two pointers spaced by **n**  when the right point reaches the end of list, we know that the left pointer is the element to remove
- We can remove the node if the left pointer points to that
- Therefore we need to point to the node before
- A simple remedy is to initialize the left pointer on a dummy node that points to the head of the list. This solution is still O(n) but with only one pass in the linked list.