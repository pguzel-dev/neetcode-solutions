# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fruits = 0

        def update(r: int, c: int):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r, c))
                    fruits += 1
                elif grid[r][c] == 1:
                    fruits += 1
        
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                fruits -= 1

                update(r + 1, c)
                update(r - 1, c)
                update(r, c + 1)
                update(r, c - 1)

            if fruits:
                time += 1
        
        return time if fruits <= 0 else -1