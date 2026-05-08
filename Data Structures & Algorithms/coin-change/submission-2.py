class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin_count = float("inf")
        memo = {}

        def dfs(index: int, current: List[int], total: int) -> None:
            nonlocal min_coin_count

            # Stop if this path is already worse than our best answer
            if len(current) >= min_coin_count:
                return

            # Found exact amount, update best answer
            if total == amount:
                min_coin_count = min(min_coin_count, len(current))
                return

            # Stop if out of coins or total is too large
            if index >= len(coins) or total > amount:
                return

            state = (index, total)

            # If we reached this same state before with fewer/equal coins, skip
            if state in memo and memo[state] <= len(current):
                return

            # Store best coin count seen for this state
            memo[state] = len(current)

            # Include coins[index]
            current.append(coins[index])
            dfs(index, current, total + coins[index])
            current.pop()

            # Skip coins[index]
            dfs(index + 1, current, total)

        dfs(0, [], 0)

        return min_coin_count if min_coin_count != float("inf") else -1