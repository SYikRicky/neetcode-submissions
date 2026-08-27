class MinStack:

    def __init__(self):
        self.stack = []
        self.store_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.store_min) != 0:
            min_val = min(self.getMin(), val)
            self.store_min.append(min_val)
        else:
            self.store_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.store_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.store_min[-1]
