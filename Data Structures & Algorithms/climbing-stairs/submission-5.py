# Closer to dynamic gpt suggestion
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        # One way to stand at step 0: take no steps
        dp[0] = 1

        # Fill answers from step 1 to n
        for i in range(1, n + 1):
            # Take 1 step from i - 1
            dp[i] += dp[i - 1]

            # Take 2 steps from i - 2, if possible
            if i >= 2:
                dp[i] += dp[i - 2]

        return dp[n]