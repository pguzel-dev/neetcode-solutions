class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}  # cache results for each index

        def dfs(i):
            # Return cached answer if we already solved this index
            if i in memo:
                return memo[i]

            # Reached the end, so this is one valid decoding
            if i == len(s):
                return 1

            # A standalone "0" is invalid
            if s[i] == "0":
                return 0

            # Try decoding one digit
            res = dfs(i + 1)

            # Try decoding two digits if it forms 10–26
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)

            memo[i] = res  # save result for this index
            return res

        return dfs(0)