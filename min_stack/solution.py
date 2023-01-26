class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        # append to min stack wisely
        if len(self.min_stack) > 0:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
