# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fruits = 0

        def update(r: int, c: int):
            nonlocal fruits
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] != 1
            ):
                return

            q.append([r,c])
            grid[r][c] = 2
            fruits -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fruits += 1
        
        time = 0
        while q and fruits > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                update(r + 1, c)
                update(r - 1, c)
                update(r, c + 1)
                update(r, c - 1)

            time += 1
        
        return time if fruits <= 0 else -1