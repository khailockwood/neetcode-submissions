class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
        self.size = 0

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.curr.next = newNode
        newNode.next = None
        newNode.prev = self.curr
        self.curr = newNode

    def back(self, steps: int) -> str:
        for i in range(steps):
            if(self.curr.prev == None):
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if (self.curr.next == None):
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)