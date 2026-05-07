# simple solution with recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i):
            # Base cases
            if i <= 2:
                return i

            # Return saved result if already computed
            if i in memo:
                return memo[i]

            # Compute and save result
            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]

        return dfs(n)