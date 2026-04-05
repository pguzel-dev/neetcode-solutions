# Solution with dicts and shit
# NOTE: Thought there would be other chars as well
class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for char in s:
            # check for '(' '[' '{'
            if char in map.values():
                stack.append(char)
            # check for ')' ']' '}'
            elif map:
                if not stack:
                    return False
                popped_char = stack.pop()
                # popped char must be equal to opening char
                # left side of the equation is closing and 
                # right side of the equation is opening
                if popped_char != map[char]:
                    return False

        return len(stack) == 0   # ensure no leftovers
        
