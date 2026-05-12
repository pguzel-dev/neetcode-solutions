class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        area = 0

        def dfs(r: int, c: int):
            nonlocal area

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return

            area += 1
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
                    max_area = max(max_area, area)
                    area = 0

        return max_area