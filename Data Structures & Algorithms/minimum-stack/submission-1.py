class MinStack:

    def __init__(self):
        self.stk = [] 

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
        else:
            cur_min = min(self.stk[-1][1], val)
            self.stk.append((val, cur_min))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
