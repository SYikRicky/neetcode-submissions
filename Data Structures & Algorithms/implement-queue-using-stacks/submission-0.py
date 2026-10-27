class MyQueue:

    def __init__(self):
        self.stack: list[int] = []
        self.queue: list[int] = []

    def push(self, x: int) -> None:
        self.stack.append(x)        

    def pop(self) -> int:
        if self.queue:
            return self.queue.pop()
        else:
            while self.stack:
                self.queue.append(self.stack.pop())
            return self.queue.pop()

    def peek(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return self.stack[0]

    def empty(self) -> bool:
        return not (self.stack or self.queue)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()