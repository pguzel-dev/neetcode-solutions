class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grids = collections.defaultdict(set) # key = (row/3 , col/3)
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if ((board[row][col] in rows[row]) or
                    (board[row][col] in cols[col]) or
                    (board[row][col] in grids[(row//3,col//3)])):
                    return False
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    grids[(row//3,col//3)].add(board[row][col])
        
        return True