#linked-list 
- Simply loop over both lists such that you add both numbers and save the carry for the next pair nodes
- In some cases one number will have more nodes than the other
- This might cause an issue if the stopping condition for the loop is that the pointers on both node do not point to null values
- To solve this, you update the stoping condition such that you still loop of the list that still has nodes and carry out your addition normally.