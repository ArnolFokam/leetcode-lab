#graph 
- Instead of trying to capture the surrounded regions
- Think about it the other way round
- Try to capture the surrounded region
- TIPS: Every region cell that is four connected to a border cell cannot be captured as the border cell cannot be surrounded.
- Therefore, perform DFS or BFS for all the border cells to mark the captured un-surrounded regions "O"
- Set what wasn't marked to "X"
- Set what was marked back to its original "O"
- Time complexity is $O(mn)$