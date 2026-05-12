class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(sub, left, right):
            # If we used all parentheses, add result
            if left >= n and right >= n:
                res.append(sub)
                return

            # Add "(" if we still can
            if left < n:
                dfs(sub + "(", left + 1, right)

            # Add ")" only if valid
            if right < left:
                dfs(sub + ")", left, right + 1)

        dfs("(", 1, 0)
        return res