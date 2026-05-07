class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get grid dimensions
        ROWS, COLS = len(heights), len(heights[0])

        # Sets to store cells reachable from each ocean
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            # Stop if out of bounds, already visited, or height is too low to flow backward
            if ((r, c) in visited or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return

            # Mark current cell as reachable
            visited.add((r, c))

            # Explore neighboring cells
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Start DFS from top and bottom edges
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Start DFS from left and right edges
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Collect cells that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res