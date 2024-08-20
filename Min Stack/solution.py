class MinStack:

    def __init__(self):
        self.vals =[]
        self.min = None

    def push(self, val: int) -> None:
        self.vals.append(val)
        if len(self.vals) == 1:
            self.min = val
        elif self.min > val:
            self.min = val
        
    def pop(self) -> None:
        if len(self.vals):
            self.vals.pop()
        if len(self.vals):
            self.min = min(self.vals)
        else:
            self.min = None

    def top(self) -> int:
        return self.vals[-1]
    
    def getMin(self) -> int:
        return self.min