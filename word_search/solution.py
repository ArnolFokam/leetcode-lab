from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        path = set()

        def search(r, c, i):
            
            # we found the word
            if i == len(word):
                return True

            # check out of bounds in row
            if r >= len(board) or r < 0:
                return False

            # check out of bounds in cols
            if c >= len(board[0]) or c < 0:
                return False

            # has this character been seen
            if (r, c) in path:
                return False

            # does character matches the current board word
            if word[i] != board[r][c]:
                return False

            # ensure we mark already visited boards
            path.add((r, c))

            res = (search(r - 1, c, i + 1) or 
                   search(r + 1, c, i + 1) or 
                   search(r, c + 1, i + 1) or 
                   search(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0): return True

        return False            