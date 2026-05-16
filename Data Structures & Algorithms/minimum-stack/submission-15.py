class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value_of_stack = float('inf')
    def push(self, val: int) -> None:
        self.min_value_of_stack = min(val, self.min_value_of_stack)
        self.min_stack.append(self.min_value_of_stack)
        return self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        if self.min_stack:
            self.min_value_of_stack = self.min_stack[-1]
        else:
            self.min_value_of_stack = float('inf')
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value_of_stack