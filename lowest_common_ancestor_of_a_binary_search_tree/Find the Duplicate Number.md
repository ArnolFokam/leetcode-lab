#tree
- If two nodes are garuanteed to have common ancestors, then, the path that leads to both nodes is same until those paths breaks at some points
- Where those path breaks is where we have our least common ancestors.
- We can basically loop branch through the tree to find that path and return where it breaks
- Time complexity is $O(\log n)$ and space complexity is $O(1)$