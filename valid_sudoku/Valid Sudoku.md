#array #matrix #hashing 
- The main problem is to detect if there are duplicates all different axis or whatever you can call them.
	- Rows
	- Columns
	- Grids
- Firstly, if we use a hashset, detecting duplicates can easily be done in $O(1)$ time for each elements.
- Secondly, we can loop over rows and columns of the board pretty easily.
- The difficulty comes when we want to detect duplicates along grids.
- To solve this, we consider the characteristics of the board.
	- It is a 9x9 board
	- The board has 9 3x3 grids

<div style="text-align:center" >
<img width="160px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" />
</div>

- Therefore, the position of each grid can be represented as a pair of indices between 0, 1 and 3 and all blocks in a specific interval will happen to be present on a specific grid.
- Therefore, we only need a way to map the block indices ($row_i$  $column_i$) to  grid indices.
- A solution would be to perform a floor division by 3.
```c
rows = {}
columns = {}
grids = {}

for row in board:
	for column in board:
		block = board(row, colum)
		if block is not empty:
			if block is already in [rows(row), columns(column), grids(row // 3, colum // 3)]:
				return False

return True
```