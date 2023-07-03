#graph
- create a hashmap of old node to new node
- Loop through the old nodes in the old graph using dfs or bfs
- When creating new node if you find that the old version of the node connects to the a node, either create this new node and connect the new node of the other old node to this newly created node or just connect directly if the node is already in the hash
- The time complexity of this solution is O(n)