class MyStack:

    def __init__(self):
        self.stack = []
        self.reverseStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.reverseStack.insert(0, x)
        print(self.stack)
        print(self.reverseStack)

    def pop(self) -> int:
        top = self.reverseStack.pop(0)
        self.stack.pop(len(self.stack)-1)
        return top

    def top(self) -> int:
        return self.reverseStack[0]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()