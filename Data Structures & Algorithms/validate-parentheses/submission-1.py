class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if not stack:   # avoid popping empty stack
                    return False
                popped_char = stack.pop()
                if char == ')' and popped_char != '(':
                    return False
                elif char == '}' and popped_char != '{':
                    return False
                elif char == ']' and popped_char != '[':
                    return False

        return len(stack) == 0   # ensure no leftovers