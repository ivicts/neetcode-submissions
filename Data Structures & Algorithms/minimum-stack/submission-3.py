class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.stack) == 1):
            self.minimums.append(val)
        elif val <= self.getMin():
            #self.minimum_2 = self.minimum
            self.minimums.append(val)


    def pop(self) -> None:
        if (self.minimums[-1] == self.stack[-1]):
            self.minimums.pop()
        self.stack = self.stack[:-1]
        print(self.stack)
        print(self.minimums)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]       
