class MinStack:

    def __init__(self):
        self.li = []
        self.min = []

    def push(self, val: int) -> None:
        (self.li).append(val)
        if len(self.min)==0:
            (self.min).append(val)
        else:
            (self.min).append(min(val, (self.min)[-1]))

    def pop(self) -> None:
        self.li.pop()
        self.min.pop()

    def top(self) -> int:
        return (self.li)[-1]

    def getMin(self) -> int:
        return (self.min)[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
