class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        curr = []

        def backtrack(opening, closing):
            if closing > opening or closing > n or opening > n:
                return
            if len(curr) == 2*n:
                results.append("".join(curr))
                return
            
            if opening > closing:
                curr.append(")")
                backtrack(opening, closing+1)
                curr.pop()
            
            curr.append("(")
            backtrack(opening+1, closing)
            curr.pop()
            
        backtrack(0, 0)
        return results