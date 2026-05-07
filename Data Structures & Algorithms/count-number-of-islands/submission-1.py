# own solution DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()  # Stores land cells we have already explored
        result = 0       # Counts the number of islands

        def dfs(r, c):
            # Stop if out of bounds, water, or already visited
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == "0" or
                (r, c) in visited):
                return
            
            # Mark this land cell as visited
            visited.add((r, c))

            # Explore all 4 neighboring cells
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Check every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # A new unvisited land cell means a new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    result += 1
                    dfs(r, c)  # Mark the entire island as visited
        
        return result