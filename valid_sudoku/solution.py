from typing import List

class Solution:
    """Module containing the solution
    """
    
    def algorithm1(self, board: List[List[str]]) -> bool:
        """check if the board is a valid sudoku with 3 traverses

        Args:
            board (List[List[str]]): the soduku board

        Returns:
            bool: result of the check
        """
        try:
            # check rows
            for i in range(9):
                nums = [int(n) for n in board[i] if n != "."]
                assert len(set(nums)) == len(nums)

            # check columns
            for i in range(9):
                nums = [int(board[j][i]) for j in range(9) if board[j][i] != "."]
                assert len(set(nums)) == len(nums)

            # check grids
            for i in range(3):
                for j in range(3):
                    nums = [int(board[k][l]) for k in range(i*3, (i + 1) * 3)  for l in range(j*3, (j + 1) * 3) if board[k][l] != "."]
                    assert len(set(nums)) == len(nums)

        except AssertionError:
            return  False
    
    def algorithm2(self, board: List[List[str]]) -> bool:
        """check if the board is a valid sudoku

        Args:
            board (List[List[str]]): the soduku board

        Returns:
            bool: result of the check
        """
        import collections

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                # skip empty squares
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or board[r][c] in  cols[c] or board[r][c] in  grids[(r // 3, c // 3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    grids[(r // 3, c // 3)].add(board[r][c])

        return True
        
    def solve(self, board: List[List[str]]) -> bool:
        """check if the board is a valid sudoku

        Args:
            board (List[List[str]]): the soduku board

        Returns:
            bool: result of the check
        """
        return self.algorithm1(board)
