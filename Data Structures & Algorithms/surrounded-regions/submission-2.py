# Time:  O(m * n)
# Space: O(m * n)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        reachable = set()

        def update(r: int, c: int):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != "O" or
                (r, c) in reachable
            ):
                return

            q.append([r, c])
            reachable.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                is_border = (
                    r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1
                )

                if board[r][c] == "O" and is_border:
                    q.append([r, c])
                    reachable.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                update(r + 1, c)
                update(r - 1, c)
                update(r, c + 1)
                update(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in reachable:
                    board[r][c] = "X"