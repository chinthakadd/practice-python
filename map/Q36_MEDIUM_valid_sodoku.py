from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxmap = dict()
        colmap = dict()

        for row in range(len(board)):
            rowset = set()
            for col in range(len(board[0])):

                ch = board[row][col]
                if ch == '.':
                    continue

                boxnum: int = int(3 * (row // 3)) + int(col // 3)
                colmap.setdefault(col, set())
                boxmap.setdefault(boxnum, set())

                if ch in boxmap[boxnum] or ch in colmap[col] or ch in rowset:
                    return False

                rowset.add(ch)
                colmap[col].add(ch)
                boxmap[boxnum].add(ch)

        return True