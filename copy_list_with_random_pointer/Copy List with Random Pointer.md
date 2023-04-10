#two-pass #linked-list 
- Build nodes without edges... yet! in the first forward pass
- While looping, create a mapping of old to new nodes in a hashmap
- Then, loop through the original list a second time.
	- And use the hashmap to build edges from the previously built nodes
	- Using the hashmap, you will we able for each node in the old list to get
		- The corresponding new node
		- The corresponding next node
		- The corresponding random node