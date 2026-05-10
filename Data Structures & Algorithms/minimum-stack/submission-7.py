class MinStack:

    def __init__(self):
        self.regular_stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.regular_stack.append(val)
        val = min(val, self.minimum_stack[-1] if self.minimum_stack else val)
        self.minimum_stack.append(val)

    def pop(self) -> None:
        del self.regular_stack[-1]
        del self.minimum_stack[-1]
        self.curr_min = self.minimum_stack[-1] if self.minimum_stack else float('inf')

    def top(self) -> int:
        return self.regular_stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
