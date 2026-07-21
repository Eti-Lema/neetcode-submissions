class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                val = board[i][j]
                if val in rows[i] or val in cols[j] or val in grid[(i // 3) * 3 + (j // 3)]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                grid[(i // 3) * 3 + (j // 3)].add(val)
        
        return True



