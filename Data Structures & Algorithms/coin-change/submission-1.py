class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin_count = float("inf")

        def dfs(index: int, current: List[int], total: int) -> None:
            nonlocal min_coin_count

            if len(current) >= min_coin_count:
                return

            if total == amount:
                min_coin_count = min(min_coin_count, len(current))
                return

            if index >= len(coins) or total > amount:
                return

            current.append(coins[index])
            dfs(index, current, total + coins[index])
            current.pop()

            dfs(index + 1, current, total)

        dfs(0, [], 0)

        return min_coin_count if min_coin_count != float("inf") else -1