# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def update(r: int, c: int):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == -1 or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                update(r + 1, c)
                update(r - 1, c)
                update(r, c + 1)
                update(r, c - 1)

            dist += 1