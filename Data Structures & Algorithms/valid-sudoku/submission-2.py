class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        grids = defaultdict(list)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                grid = (row // 3, col // 3)
                if val == ".":
                    continue
                if (
                    val in cols[col]
                    or val in rows[row]
                    or val in grids[grid]
                ):
                    return False
                cols[col].append(val)
                rows[row].append(val)
                grids[grid].append(val)

        return True
