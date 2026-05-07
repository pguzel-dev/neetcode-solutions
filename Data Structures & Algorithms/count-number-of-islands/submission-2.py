# own solution BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()  # Stores land cells we have already explored
        result = 0       # Counts the number of islands

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))  # Mark the starting land cell as visited

            while queue:
                row, col = queue.popleft()

                # Explore all 4 neighboring cells
                directions = [
                    (1, 0),   # down
                    (-1, 0),  # up
                    (0, 1),   # right
                    (0, -1)   # left
                ]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # Only visit valid, unvisited land cells
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        # Check every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # A new unvisited land cell means a new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    result += 1
                    bfs(r, c)  # Mark the entire island as visited

        return result