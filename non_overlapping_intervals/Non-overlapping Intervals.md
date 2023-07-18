#interval 
- Sort intervals according to start value
- Compare adjacent pair greedily
- If the intervals overlap, remove the one with the biggest end interval
- Time complexity is $O(n \log n)$ because of the sorting
- Space complexity is $O(1)$