class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get board dimensions
        ROWS, COLS = len(board), len(board[0])

        # Keeps track of cells already used in the current path
        path = set()

        def dfs(r, c, index):
            # If we matched every character in word, we found it
            if index == len(word):
                return True

            # Stop if out of bounds, wrong character, or cell already used
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[index] != board[r][c] or
                (r, c) in path):
                return False
            
            # Mark this cell as used in the current search path
            path.add((r, c))

            # Try continuing the word in all 4 directions
            res = (dfs(r + 1, c, index + 1) or
                   dfs(r - 1, c, index + 1) or
                   dfs(r, c + 1, index + 1) or
                   dfs(r, c - 1, index + 1))

            # Backtrack: unmark this cell so other paths can use it
            path.remove((r, c))

            return res
        
        # Try starting DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        # No valid path found
        return False