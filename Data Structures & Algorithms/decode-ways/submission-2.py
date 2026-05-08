# Bottom-up DP / iterative
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # base case: reaching the end is one valid decoding

        # Work backward from the last character to the first
        for i in range(len(s) - 1, -1, -1):
            # "0" cannot be decoded by itself
            if s[i] == "0":
                dp[i] = 0
            else:
                # Take one valid digit and use the result from the next index
                dp[i] = dp[i + 1]

            # Check if two digits form a valid number from 10 to 26
            if (
                i + 1 < len(s)
                and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")
            ):
                # Add ways from skipping two digits
                dp[i] += dp[i + 2]

        # Number of ways to decode the full string
        return dp[0]