'''
[null]

[2, 0]
keep track of min [1,0]
return stack[0]
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.fetch_min = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.fetch_min or val <= self.fetch_min[-1]:
            self.fetch_min.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.fetch_min[-1]:
                self.fetch_min.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        
    def getMin(self) -> int:
        if self.fetch_min:
            return self.fetch_min[-1]
        return None
