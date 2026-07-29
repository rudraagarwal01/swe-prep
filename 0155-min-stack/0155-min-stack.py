class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.stack_min:
            curr_min = value
        else:
            curr_min = min(self.stack_min[-1], value)
        
        self.stack_min.append(curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()