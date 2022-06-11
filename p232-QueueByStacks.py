class MyQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if len(self.queue1)==0:
            self.queue1.append(x)
            self.queue2.append(x)
        else:
            self.queue2.append(x)
            self.queue1=[]
            i=0
            while i < len(self.queue2):
                self.queue1.append(self.queue2[-i-1])
                i+=1

    def pop(self) -> int:
        value = self.queue1.pop()
        self.queue2=[]
        i=0
        while i < len(self.queue1):
            self.queue2.append(self.queue1[-i-1])
            i+=1
        return value

    def peek(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return (len(self.queue1)==0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
