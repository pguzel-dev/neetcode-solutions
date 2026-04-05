class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for char in s:
            # check for '(' '[' '{'
            if char in bracket_map.values():
                stack.append(char)
            # check for ')' ']' '}'
            elif bracket_map:
                if not stack:
                    return False
                popped_char = stack.pop()
                # popped char must be equal to opening char
                # left side of the equation is closing and 
                # right side of the equation is opening
                if popped_char != bracket_map[char]:
                    return False

        return len(stack) == 0   # ensure no leftovers
        
