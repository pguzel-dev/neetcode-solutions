# Brute force solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == "(":
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        def generate(curr):
            if len(curr) == 2 * n:
                if is_valid(curr):
                    result.append(curr)
                return

            generate(curr + "(")
            generate(curr + ")")

        generate("")
        return result