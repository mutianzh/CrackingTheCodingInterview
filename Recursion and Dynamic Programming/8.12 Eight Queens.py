"""
8.12 Eight Queens:Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.result = []

        def generate_results(state):
            ans = []
            for row in state:
                ans.append(''.join(row))
            self.result.append(list(ans))

        def backtrack(row, columns, diagonal, anti_diagonal, state):
            if row == n:
                generate_results(state)
                return

            # given row, try to place at each col
            for col in range(n):
                current_diag = row + col
                current_anti_diag = row - col

                if col in columns or current_diag in diagonal or current_anti_diag in anti_diagonal:
                    continue

                # place the queen
                columns.add(col)
                diagonal.add(current_diag)
                anti_diagonal.add(current_anti_diag)
                state[row][col] = 'Q'

                # go to next row
                backtrack(row + 1, columns, diagonal, anti_diagonal, state)

                # remove the queen
                columns.remove(col)
                diagonal.remove(current_diag)
                anti_diagonal.remove(current_anti_diag)
                state[row][col] = '.'

        board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)

        return self.result