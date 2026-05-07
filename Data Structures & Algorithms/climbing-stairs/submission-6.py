# Suggested solution
class Solution:
    def climbStairs(self, n: int) -> int:
        # current represents the number of ways from the current step
        # next represents the number of ways from the next step
        current, next = 1, 1

        # Work backwards from the top until reaching the start
        for _ in range(n - 1):
            # Save the old current value before updating it
            previous_current = current

            # Ways from current = ways after taking 1 step + ways after taking 2 steps
            current = current + next
            # Move next forward to the old current value
            next = previous_current

        # current now stores the total ways to climb n stairs
        return current