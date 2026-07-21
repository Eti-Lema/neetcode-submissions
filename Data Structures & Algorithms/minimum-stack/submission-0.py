class MinStack:

    def __init__(self):
        self.min_stack = []
        self.normal_stack = []
        

    def push(self, val: int) -> None:
        self.normal_stack.append(val)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.normal_stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.normal_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
