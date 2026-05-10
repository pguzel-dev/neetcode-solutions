class MinStack:

    def __init__(self):
        self.regular_stack = []
        self.minimum_stack = []
        self.curr_min = float('inf')

    def push(self, val: int) -> None:
        self.regular_stack.append(val)

        if val <= self.curr_min:
            self.minimum_stack.append(val)
            self.curr_min = val
        else:
            self.minimum_stack.append(self.curr_min)
        
    def pop(self) -> None:
        del self.regular_stack[-1]
        del self.minimum_stack[-1]
        try:
            self.curr_min = self.minimum_stack[-1]
        except:
            self.curr_min = float('inf')

    def top(self) -> int:
        return self.regular_stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
