class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtracking(index, row, col):
            if (row < 0 or row >= ROWS or           # boundary?
                col < 0 or col >= COLS or           # boundary?
                (row, col) in path or               # seen?
                board[row][col] != word[index]):    # match?
                return False
            
            if index == len(word) - 1:              # word done
                return True
            
            path.add((row, col))                    # add to seen

            found = (
                backtracking(index + 1, row + 1, col) or    # right
                backtracking(index + 1, row - 1, col) or    # left
                backtracking(index + 1, row, col + 1) or    # up
                backtracking(index + 1, row, col - 1)       # down
            )

            path.remove((row, col))                 # remove from seen
            return found
        
        # try it out for everything
        for x in range(ROWS):
            for y in range(COLS):
                if backtracking(0, x, y):
                    return True

        return False